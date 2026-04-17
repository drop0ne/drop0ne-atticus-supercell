from __future__ import annotations

from typing import Any


REQUIRED_DOMAINS = {
    "schema-validation",
    "pointer-consistency",
    "registry-index-alignment",
    "stale-current-detection",
    "generator-integrity",
}


def plan_validate_phase(paths: Any, current_refresh: dict[str, Any], validation_report: dict[str, Any]) -> dict[str, str]:
    overall_status = validation_report.get("overall_status")
    checks = validation_report.get("checks", [])

    if overall_status not in {"pass", "warn", "fail"}:
        return {
            "phase": "validate",
            "status": "fail",
            "summary": "Validation phase failed: validation report overall_status is missing or invalid.",
        }

    if not isinstance(checks, list) or not checks:
        return {
            "phase": "validate",
            "status": "fail",
            "summary": "Validation phase failed: validation report checks list is missing or empty.",
        }

    present_domains = {check.get("domain") for check in checks if isinstance(check, dict)}
    missing_domains = sorted(REQUIRED_DOMAINS - present_domains)
    if missing_domains:
        return {
            "phase": "validate",
            "status": "warn",
            "summary": f"Validation phase warning: validation report is missing expected domains: {', '.join(missing_domains)}.",
        }

    if overall_status == "fail":
        return {
            "phase": "validate",
            "status": "fail",
            "summary": "Validation phase failed: current validation report overall_status=fail.",
        }

    if overall_status == "warn":
        return {
            "phase": "validate",
            "status": "warn",
            "summary": "Validation phase warning: current validation report overall_status=warn.",
        }

    return {
        "phase": "validate",
        "status": "pass",
        "summary": "Validation phase passed using a complete current validation report with expected domains present.",
    }
