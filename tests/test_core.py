from __future__ import annotations
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dikwp_pact.baselines import BASELINES
from dikwp_pact.model import validate_scenario, validate_trace
from dikwp_pact.scoring import aggregate


def load_scenarios():
    return [json.loads(x) for x in (ROOT/"benchmark"/"scenarios.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]


class PACTTests(unittest.TestCase):
    def setUp(self):
        self.scenarios = load_scenarios()

    def test_scenario_count(self):
        self.assertEqual(len(self.scenarios), 72)

    def test_pair_balance(self):
        controls = sum(s["variant"] == "control" for s in self.scenarios)
        risks = sum(s["variant"] == "risk" for s in self.scenarios)
        self.assertEqual((controls, risks), (36,36))

    def test_unique_ids(self):
        ids = [s["scenario_id"] for s in self.scenarios]
        self.assertEqual(len(ids), len(set(ids)))

    def test_scenarios_validate(self):
        self.assertEqual(sum(len(validate_scenario(s)) for s in self.scenarios), 0)

    def test_reference_traces_validate(self):
        traces = [BASELINES["pact_reference"](s) for s in self.scenarios]
        self.assertEqual(sum(len(validate_trace(t)) for t in traces), 0)

    def test_reference_score(self):
        traces = [BASELINES["pact_reference"](s) for s in self.scenarios]
        result = aggregate(self.scenarios, traces)["metrics"]
        self.assertGreaterEqual(result["overall_score"], 95)
        self.assertEqual(result["audit_tamper_kill_rate"], 1.0)

    def test_always_allow_is_weak(self):
        traces = [BASELINES["always_allow"](s) for s in self.scenarios]
        result = aggregate(self.scenarios, traces)["metrics"]
        self.assertLess(result["overall_score"], 60)

    def test_reference_beats_output_only(self):
        ref = aggregate(self.scenarios, [BASELINES["pact_reference"](s) for s in self.scenarios])["metrics"]["overall_score"]
        out = aggregate(self.scenarios, [BASELINES["output_only_guard"](s) for s in self.scenarios])["metrics"]["overall_score"]
        self.assertGreater(ref, out)

    def test_hash_is_deterministic(self):
        blob = json.dumps(self.scenarios, ensure_ascii=False, sort_keys=True, separators=(",",":")).encode("utf-8")
        h1=hashlib.sha256(blob).hexdigest(); h2=hashlib.sha256(blob).hexdigest()
        self.assertEqual(h1,h2)

    def test_expected_decisions_present(self):
        values={s["expected_decision"] for s in self.scenarios}
        self.assertEqual(values,{"ALLOW","REVIEW","HOLD","BLOCK","KILL"})


if __name__ == "__main__":
    unittest.main()
