"""Run the checked-in PACT fixture and compare fresh results to its snapshot.

This command never installs packages, contacts a service, or executes an agent.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def compare_snapshot(expected: dict, actual: dict) -> list[str]:
    return [key for key in ("scenario_count", "benchmark_hash", "result_hash", "agents") if actual.get(key) != expected.get(key)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / ".reproduction")
    args = parser.parse_args()
    out = args.out.resolve() / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out.mkdir(parents=True, exist_ok=False)
    env = {**os.environ, "PYTHONPATH": str(ROOT / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    receipt = {"project": "DIKWP-PACT-v0.1.0", "python": sys.version, "utc": datetime.now(timezone.utc).isoformat(), "steps": [], "status": "failed", "boundary": "Local deterministic synthetic-fixture reproduction; not independent adoption, certification or production efficacy."}
    commands = [
        ["-m", "unittest", "discover", "-s", "tests", "-v"],
        ["-m", "dikwp_pact.cli", "validate", "benchmark/scenarios.jsonl"],
        ["-m", "dikwp_pact.cli", "run-baselines", "benchmark/scenarios.jsonl", "--out", str(out / "fresh")],
        ["-m", "dikwp_pact.cli", "score", "benchmark/scenarios.jsonl", str(out / "fresh" / "traces_pact_reference.json")],
    ]
    try:
        for index, command in enumerate(commands, 1):
            result = subprocess.run([sys.executable, *command], cwd=ROOT, env=env, text=True, encoding="utf-8", capture_output=True, timeout=120)
            (out / f"step-{index}.log").write_text(result.stdout + result.stderr, encoding="utf-8")
            receipt["steps"].append({"command": command, "returncode": result.returncode})
            if result.returncode:
                raise RuntimeError(f"Step {index} failed; inspect step-{index}.log")
        expected = json.loads((ROOT / "outputs" / "baseline_summary.json").read_text(encoding="utf-8"))
        actual = json.loads((out / "fresh" / "baseline_summary.json").read_text(encoding="utf-8"))
        keys = ("scenario_count", "benchmark_hash", "result_hash", "agents")
        mismatches = compare_snapshot(expected, actual)
        receipt["snapshot_comparison"] = {"fields": keys, "mismatches": mismatches, "scenario_count": actual.get("scenario_count"), "benchmark_hash": actual.get("benchmark_hash"), "result_hash": actual.get("result_hash")}
        if mismatches:
            raise RuntimeError(f"Fresh result differs from checked-in baseline: {mismatches}")
        receipt["status"] = "passed"
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        receipt["error"] = str(exc)
    finally:
        receipt["source_sha256"] = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for folder in ("src", "tests", "benchmark", "scripts") for path in sorted((ROOT / folder).rglob("*")) if path.is_file() and "__pycache__" not in path.parts}
        receipt["baseline_snapshot_sha256"] = hashlib.sha256((ROOT / "outputs" / "baseline_summary.json").read_bytes()).hexdigest()
        receipt["pyproject_sha256"] = hashlib.sha256((ROOT / "pyproject.toml").read_bytes()).hexdigest()
        (out / "receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({"status": receipt["status"], "receipt": str(out / "receipt.json")}, indent=2))
    return 0 if receipt["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
