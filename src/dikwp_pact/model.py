from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

DECISIONS = ["ALLOW", "REVIEW", "HOLD", "BLOCK", "KILL"]
STAGES = ["D", "I", "K", "W", "P", "R"]


def validate_scenario(s: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ["scenario_id", "domain", "family", "variant", "purpose_contract", "signals", "expected_decision", "gold_dikwp_trace"]
    for key in required:
        if key not in s:
            errors.append(f"missing scenario field: {key}")
    if s.get("expected_decision") not in DECISIONS:
        errors.append("invalid expected_decision")
    if s.get("variant") not in {"control", "risk"}:
        errors.append("invalid variant")
    return errors


def validate_trace(t: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ["trace_id", "scenario_id", "agent_id", "decision", "confidence", "stages", "residuals", "recovery_plan"]
    for key in required:
        if key not in t:
            errors.append(f"missing trace field: {key}")
    if t.get("decision") not in DECISIONS:
        errors.append("invalid decision")
    stages = {x.get("stage") for x in t.get("stages", []) if isinstance(x, dict)}
    unknown = stages - set(STAGES)
    if unknown:
        errors.append(f"unknown stages: {sorted(unknown)}")
    return errors
