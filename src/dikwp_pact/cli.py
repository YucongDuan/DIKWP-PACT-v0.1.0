from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
from .baselines import BASELINES
from .model import validate_scenario, validate_trace
from .scoring import aggregate
from .reporting import audit_report


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def canonical_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",",":")).encode("utf-8")).hexdigest()


def cmd_validate(args) -> int:
    scenarios = load_jsonl(Path(args.scenarios))
    errors = []
    for s in scenarios:
        errors.extend([f"{s.get('scenario_id','?')}: {e}" for e in validate_scenario(s)])
    print(json.dumps({"scenarios":len(scenarios),"errors":errors,"hash":canonical_hash(scenarios)}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


def cmd_run(args) -> int:
    scenarios = load_jsonl(Path(args.scenarios))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    summary = {"schema_version":"0.1.0","scenario_count":len(scenarios),"agents":{},"benchmark_hash":canonical_hash(scenarios)}
    leaderboard = []
    for name, fn in BASELINES.items():
        traces = [fn(s) for s in scenarios]
        result = aggregate(scenarios, traces)
        summary["agents"][name] = result["metrics"]
        (out/f"traces_{name}.json").write_text(json.dumps(traces, ensure_ascii=False, indent=2), encoding="utf-8")
        (out/f"audit_report_{name}.md").write_text(audit_report(name, result), encoding="utf-8")
        leaderboard.append({"agent_id":name, **result["metrics"]})
    leaderboard.sort(key=lambda x: x["overall_score"], reverse=True)
    summary["result_hash"] = canonical_hash(summary["agents"])
    (out/"baseline_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (out/"leaderboard.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fields = list(leaderboard[0].keys())
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(leaderboard)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def cmd_score(args) -> int:
    scenarios = load_jsonl(Path(args.scenarios))
    traces = json.loads(Path(args.traces).read_text(encoding="utf-8"))
    errors=[]
    for t in traces:
        errors.extend([f"{t.get('trace_id','?')}: {e}" for e in validate_trace(t)])
    result = aggregate(scenarios, traces)
    output = {"errors":errors, **result}
    if args.out:
        Path(args.out).write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(output["metrics"], ensure_ascii=False, indent=2))
    return 1 if errors else 0


def build_parser():
    p = argparse.ArgumentParser(prog="dikwp-pact", description="DIKWP-PACT offline benchmark and trace scorer")
    sub = p.add_subparsers(dest="cmd", required=True)
    a=sub.add_parser("validate"); a.add_argument("scenarios"); a.set_defaults(func=cmd_validate)
    b=sub.add_parser("run-baselines"); b.add_argument("scenarios"); b.add_argument("--out", default="outputs"); b.set_defaults(func=cmd_run)
    c=sub.add_parser("score"); c.add_argument("scenarios"); c.add_argument("traces"); c.add_argument("--out"); c.set_defaults(func=cmd_score)
    return p


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
