from __future__ import annotations

from pathlib import Path
from typing import Any


def plan_refresh_phase(paths: Any, current_refresh: dict[str, Any], refresh_runner_input: dict[str, Any]) -> dict[str, str]:
    scope = refresh_runner_input.get("refresh_scope", current_refresh.get("scope", "unknown"))
    trigger = refresh_runner_input.get("trigger_event", "unknown")
    return {
        "phase": "refresh",
        "status": "planned",
        "summary": f"Refresh phase prepared for scope={scope} with trigger={trigger}.",
    }
