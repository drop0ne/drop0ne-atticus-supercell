from __future__ import annotations

from typing import Any


REQUIRED_KEYS = [
    "refresh_id",
    "trigger_event",
    "refresh_scope",
    "source_repo",
    "source_branch",
    "affected_projects",
    "expected_current_resume_packets",
    "expected_current_baseline_cells",
]


def plan_refresh_phase(paths: Any, current_refresh: dict[str, Any], refresh_runner_input: dict[str, Any]) -> dict[str, str]:
    missing = [key for key in REQUIRED_KEYS if key not in refresh_runner_input]
    if missing:
        return {
            "phase": "refresh",
            "status": "fail",
            "summary": f"Refresh phase failed: missing required refresh-runner keys: {', '.join(missing)}.",
        }

    affected_projects = refresh_runner_input.get("affected_projects", [])
    expected_packets = refresh_runner_input.get("expected_current_resume_packets", [])
    expected_cells = refresh_runner_input.get("expected_current_baseline_cells", [])

    if not affected_projects or not expected_packets or not expected_cells:
        return {
            "phase": "refresh",
            "status": "warn",
            "summary": "Refresh phase warning: refresh-runner input is present but one or more expected project/packet/cell lists are empty.",
        }

    scope = refresh_runner_input.get("refresh_scope", current_refresh.get("scope", "unknown"))
    trigger = refresh_runner_input.get("trigger_event", "unknown")
    return {
        "phase": "refresh",
        "status": "pass",
        "summary": f"Refresh phase passed for scope={scope} with trigger={trigger} and {len(affected_projects)} affected project(s).",
    }
