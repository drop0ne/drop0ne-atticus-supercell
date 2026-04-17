from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from phases.generate import plan_generate_phase
from phases.refresh import plan_refresh_phase
from phases.validate import plan_validate_phase


@dataclass(frozen=True)
class RunnerPaths:
    repo_root: Path
    current_refresh: Path
    refresh_runner_input: Path
    session_state_generator_input: Path
    validation_report: Path
    output_record: Path


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_json_or_empty(path: Path, role: str, repo_root: Path) -> tuple[dict[str, Any], dict[str, str]]:
    rel = str(path.relative_to(repo_root))
    if not path.exists():
        return {}, {
            "role": role,
            "path": rel,
            "status": "fail",
            "detail": f"Missing required input for role={role}: {rel}",
        }

    try:
        return _load_json(path), {
            "role": role,
            "path": rel,
            "status": "pass",
            "detail": f"Loaded JSON input for role={role} from {rel}.",
        }
    except json.JSONDecodeError as exc:
        return {}, {
            "role": role,
            "path": rel,
            "status": "fail",
            "detail": f"Invalid JSON for role={role}: {rel} ({exc})",
        }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def _resolve_paths(repo_root: Path, output: str | None) -> RunnerPaths:
    current_refresh = repo_root / "CURRENT_REFRESH.json"
    if not current_refresh.exists():
        raise FileNotFoundError(f"Missing current refresh pointer: {current_refresh}")

    refresh_doc = _load_json(current_refresh)
    pointers = refresh_doc.get("current_pointers", {})

    refresh_runner_input = repo_root / pointers.get(
        "refresh_runner_input_current",
        "docs/REFRESH_RUNNER_INPUT.current.json",
    )
    session_state_generator_input = repo_root / pointers.get(
        "session_state_generator_input_current",
        "docs/SESSION_STATE_GENERATOR_INPUT.current.json",
    )
    validation_report = repo_root / pointers.get(
        "validation_report_current",
        "docs/VALIDATION_REPORT.current.json",
    )
    output_record = repo_root / (output or "docs/AUTOMATION_RUNNER_EXECUTION_RECORD.generated.json")

    return RunnerPaths(
        repo_root=repo_root,
        current_refresh=current_refresh,
        refresh_runner_input=refresh_runner_input,
        session_state_generator_input=session_state_generator_input,
        validation_report=validation_report,
        output_record=output_record,
    )


def _resolve_pointer_status(repo_root: Path, current_refresh_doc: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    current_pointers = current_refresh_doc.get("current_pointers", {})
    resolved_pointer_keys = [
        "refresh_manifest_schema",
        "session_state_generator_input_schema",
        "session_state_bundle_schema",
        "validation_report_schema",
        "automation_runner_execution_record_schema",
    ]

    resolved: list[dict[str, str]] = []
    checks: list[dict[str, str]] = []

    for key in resolved_pointer_keys:
        if key not in current_pointers:
            checks.append({
                "pointer": key,
                "path": "",
                "status": "fail",
                "detail": f"Missing current pointer: {key}",
            })
            continue

        rel_path = current_pointers[key]
        resolved.append({"pointer": key, "path": rel_path})
        target = repo_root / rel_path
        if not target.exists():
            checks.append({
                "pointer": key,
                "path": rel_path,
                "status": "fail",
                "detail": f"Missing pointer target for {key}: {rel_path}",
            })
        else:
            checks.append({
                "pointer": key,
                "path": rel_path,
                "status": "pass",
                "detail": f"Pointer target exists for {key}: {rel_path}",
            })

    return resolved, checks


def _build_execution_record(paths: RunnerPaths) -> dict[str, Any]:
    current_refresh_doc = _load_json(paths.current_refresh)
    current_refresh_rel = str(paths.current_refresh.relative_to(paths.repo_root))

    refresh_runner_input_doc, refresh_check = _load_json_or_empty(
        paths.refresh_runner_input,
        "refresh_runner_input",
        paths.repo_root,
    )
    generator_input_doc, generator_check = _load_json_or_empty(
        paths.session_state_generator_input,
        "session_state_generator_input",
        paths.repo_root,
    )
    validation_report_doc, validation_check = _load_json_or_empty(
        paths.validation_report,
        "validation_report",
        paths.repo_root,
    )

    resolved_current_pointers, pointer_checks = _resolve_pointer_status(paths.repo_root, current_refresh_doc)

    refresh_phase = plan_refresh_phase(paths, current_refresh_doc, refresh_runner_input_doc)
    generate_phase = plan_generate_phase(paths, current_refresh_doc, generator_input_doc)
    validate_phase = plan_validate_phase(paths, current_refresh_doc, validation_report_doc)

    phase_records = [refresh_phase, generate_phase, validate_phase]
    input_checks = [
        {
            "role": "current_refresh",
            "path": current_refresh_rel,
            "status": "pass",
            "detail": f"Loaded current refresh pointer from {current_refresh_rel}.",
        },
        refresh_check,
        generator_check,
        validation_check,
    ]

    failing_input_checks = [check for check in input_checks if check["status"] == "fail"]
    failing_pointer_checks = [check for check in pointer_checks if check["status"] == "fail"]

    status = "pass"
    if failing_input_checks or failing_pointer_checks:
        status = "fail"
    elif any(p["status"] == "fail" for p in phase_records):
        status = "fail"
    elif any(p["status"] == "warn" for p in phase_records):
        status = "warn"

    record = {
        "record_version": "v1",
        "runner_run_id": f"runner-{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}",
        "current_refresh_id": current_refresh_doc.get("current_refresh_id", "unknown"),
        "resolved_inputs": [
            {"role": "current_refresh", "path": current_refresh_rel},
            {"role": "refresh_runner_input", "path": str(paths.refresh_runner_input.relative_to(paths.repo_root))},
            {"role": "session_state_generator_input", "path": str(paths.session_state_generator_input.relative_to(paths.repo_root))},
            {"role": "validation_report", "path": str(paths.validation_report.relative_to(paths.repo_root))},
        ],
        "input_checks": input_checks,
        "resolved_current_pointers": resolved_current_pointers,
        "pointer_checks": pointer_checks,
        "planned_phases": [phase["phase"] for phase in phase_records],
        "phase_results": phase_records,
        "status": status,
        "notes": [
            "Generated by the concrete ATTICUS supercell runner scaffold.",
            "This implementation is intentionally non-mutating and performs basic live file-existence checks.",
            *[check["detail"] for check in failing_input_checks],
            *[check["detail"] for check in failing_pointer_checks],
            *[phase["summary"] for phase in phase_records],
        ],
    }
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description="ATTICUS supercell runner scaffold")
    parser.add_argument("--repo-root", default=".", help="Path to repo root")
    parser.add_argument("--output", default=None, help="Relative output path for generated execution record")
    parser.add_argument("--print-json", action="store_true", help="Print execution record to stdout")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    paths = _resolve_paths(repo_root, args.output)
    record = _build_execution_record(paths)
    _write_json(paths.output_record, record)

    if args.print_json:
        print(json.dumps(record, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
