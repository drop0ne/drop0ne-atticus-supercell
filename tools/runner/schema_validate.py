from __future__ import annotations

from datetime import datetime
from typing import Any


def validate_payload_against_schema(schema: dict[str, Any], payload: Any) -> list[str]:
    errors: list[str] = []
    _validate_node(schema, payload, "$", errors)
    return errors


def _validate_node(schema: dict[str, Any], payload: Any, path: str, errors: list[str]) -> None:
    expected_type = schema.get("type")
    if expected_type is not None and not _matches_type(expected_type, payload):
        errors.append(f"{path}: expected type {_render_type(expected_type)}, got {_python_type_name(payload)}")
        return

    if "enum" in schema and payload not in schema["enum"]:
        errors.append(f"{path}: value {payload!r} is not in enum {schema['enum']!r}")
        return

    if schema.get("format") == "date-time" and isinstance(payload, str):
        if not _is_datetime_string(payload):
            errors.append(f"{path}: value {payload!r} is not a valid date-time string")
            return

    schema_type = _first_type(expected_type)

    if schema_type == "object" and isinstance(payload, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in payload:
                errors.append(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        additional_properties = schema.get("additionalProperties", True)
        if additional_properties is False:
            allowed_keys = set(properties.keys())
            extra_keys = sorted(set(payload.keys()) - allowed_keys)
            for key in extra_keys:
                errors.append(f"{path}: additional property {key!r} is not allowed")

        for key, subschema in properties.items():
            if key in payload:
                _validate_node(subschema, payload[key], f"{path}.{key}", errors)
        return

    if schema_type == "array" and isinstance(payload, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for idx, item in enumerate(payload):
                _validate_node(item_schema, item, f"{path}[{idx}]", errors)
        return

    if schema_type == "integer":
        minimum = schema.get("minimum")
        if minimum is not None and isinstance(payload, int) and not isinstance(payload, bool) and payload < minimum:
            errors.append(f"{path}: integer value {payload} is less than minimum {minimum}")
        return


def _matches_type(expected_type: str | list[str], payload: Any) -> bool:
    allowed_types = expected_type if isinstance(expected_type, list) else [expected_type]
    return any(_matches_single_type(t, payload) for t in allowed_types)


def _matches_single_type(expected_type: str, payload: Any) -> bool:
    if expected_type == "object":
        return isinstance(payload, dict)
    if expected_type == "array":
        return isinstance(payload, list)
    if expected_type == "string":
        return isinstance(payload, str)
    if expected_type == "integer":
        return isinstance(payload, int) and not isinstance(payload, bool)
    if expected_type == "boolean":
        return isinstance(payload, bool)
    if expected_type == "null":
        return payload is None
    return True


def _first_type(expected_type: str | list[str] | None) -> str | None:
    if isinstance(expected_type, list):
        for candidate in expected_type:
            if candidate != "null":
                return candidate
        return expected_type[0] if expected_type else None
    return expected_type


def _render_type(expected_type: str | list[str]) -> str:
    if isinstance(expected_type, list):
        return " or ".join(expected_type)
    return expected_type


def _python_type_name(payload: Any) -> str:
    if payload is None:
        return "null"
    if isinstance(payload, bool):
        return "boolean"
    if isinstance(payload, int):
        return "integer"
    if isinstance(payload, str):
        return "string"
    if isinstance(payload, list):
        return "array"
    if isinstance(payload, dict):
        return "object"
    return type(payload).__name__


def _is_datetime_string(value: str) -> bool:
    candidate = value.replace("Z", "+00:00")
    try:
        datetime.fromisoformat(candidate)
        return True
    except ValueError:
        return False
