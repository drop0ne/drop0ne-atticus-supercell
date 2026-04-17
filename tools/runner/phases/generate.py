from __future__ import annotations

from typing import Any


REQUIRED_KEYS = [
    "generator_run_id",
    "target_scope",
    "project_id",
    "mode",
    "objective",
]


def plan_generate_phase(paths: Any, current_refresh: dict[str, Any], generator_input: dict[str, Any]) -> dict[str, str]:
    missing = [key for key in REQUIRED_KEYS if key not in generator_input]
    if missing:
        return {
            "phase": "generate",
            "status": "fail",
            "summary": f"Generation phase failed: missing required generator-input keys: {', '.join(missing)}.",
        }

    max_cells = generator_input.get("max_cells")
    max_chars = generator_input.get("max_chars")
    if not isinstance(max_cells, int) or not isinstance(max_chars, int):
        return {
            "phase": "generate",
            "status": "warn",
            "summary": "Generation phase warning: generator-input is present but max_cells/max_chars bounds are missing or invalid.",
        }

    if max_cells < 1 or max_chars < 1000:
        return {
            "phase": "generate",
            "status": "warn",
            "summary": f"Generation phase warning: bounds may be too restrictive (max_cells={max_cells}, max_chars={max_chars}).",
        }

    target_scope = generator_input.get("target_scope", "unknown")
    project_id = generator_input.get("project_id", "unknown")
    return {
        "phase": "generate",
        "status": "pass",
        "summary": f"Generation phase passed for target_scope={target_scope} project_id={project_id} with bounds max_cells={max_cells} max_chars={max_chars}.",
    }
