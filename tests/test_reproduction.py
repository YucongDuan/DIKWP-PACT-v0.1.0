import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pact_reproduce", ROOT / "scripts" / "reproduce.py")
reproduce = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reproduce)


class ReproductionChecks(unittest.TestCase):
    def setUp(self):
        self.expected = json.loads((ROOT / "outputs" / "baseline_summary.json").read_text())

    def test_matching_snapshot_passes(self):
        self.assertEqual(reproduce.compare_snapshot(self.expected, copy.deepcopy(self.expected)), [])

    def test_metric_drift_fails(self):
        changed = copy.deepcopy(self.expected)
        changed["agents"]["pact_reference"]["overall_score"] = 99.0
        self.assertIn("agents", reproduce.compare_snapshot(self.expected, changed))

    def test_benchmark_replacement_fails(self):
        changed = copy.deepcopy(self.expected)
        changed["benchmark_hash"] = "0" * 64
        self.assertIn("benchmark_hash", reproduce.compare_snapshot(self.expected, changed))
