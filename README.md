# DIKWP-PACT v0.1.0

## Open Purpose Assurance & Cognitive Trace Project

**中文定位：开放意图保障与认知轨迹关键项目。**

DIKWP-PACT is a GitHub-ready, offline-first flagship project for testing whether an agent preserves a signed purpose contract across data, information, knowledge, wisdom, action and residual-risk handling. It converts DIKWP from a broad conceptual portfolio into one falsifiable, reproducible and externally contributable public product.

> Core research question: Does purpose-aware, authorization-aware and evidence-aware trace auditing reduce high-impact agent failures without excessive overblocking?

## Why this project

The public GitHub snapshot on 2026-07-15 showed 173 repositories and 0 GitHub Projects. Several relevant repositories already contain strong ingredients—AgentMesh, BenchmarkLab and IntentAsset—but have no formal release and little external fork activity. PACT deliberately **consolidates** rather than adds another unconstrained concept repository.

## What is included

- `PACT-SPEC`: five JSON schemas for purpose contracts, scenarios, traces, submissions and findings.
- `PACT-BENCH`: 72 paired synthetic scenarios across six domains and six failure families.
- `PACT-RUNTIME`: standard-library-only Python validator, baseline runner and scorer.
- `PACT-DASHBOARD`: offline browser dashboard.
- `PACT-CHALLENGE`: submission rules, leaderboard and replication report template.
- `PACT-PAPER`: preregistration, hypotheses and manuscript outline.
- `PACT-GOVERNANCE`: release gates, maintainer roles, issue templates and a 90-day board.

## Quick start

The source, tests and benchmark are now directly browsable and cloneable. The
original ZIP remains only a historical delivery snapshot; unpacking it is not
required. Use Python 3.10 or newer (the reproduction environment is Python 3.12):

```bash
python scripts/reproduce.py
```

This standard-library-only command runs the tests, validates all 72 scenarios,
reruns four baselines, scores the reference traces, and compares the fresh
benchmark/result hashes and all reported agent metrics to the checked-in
snapshot. It exits nonzero on mismatch and writes fresh logs and a source-hashed
receipt under `.reproduction/`. It does not install dependencies or use a network.

For an installed command-line entry point (optional):

```bash
python -m pip install -e .
dikwp-pact validate benchmark/scenarios.jsonl
dikwp-pact run-baselines benchmark/scenarios.jsonl --out outputs
dikwp-pact score benchmark/scenarios.jsonl outputs/traces_pact_reference.json
```

No network, API key, model call, personal data, credential or production action is required.

See [English reproduction guide](docs/REPRODUCIBILITY.md),
[中文快速复现](QUICKSTART_CN.md), and [archive provenance](docs/SOURCE_IMPORT.md).

## Synthetic baseline snapshot

| Baseline | Overall score | Decision accuracy | Redline recall | Control allow rate |
|---|---:|---:|---:|---:|
| `pact_reference` | 100.0 | 1.0 | 1.0 | 1.0 |
| `keyword_guard` | 82.67 | 0.6667 | 1.0 | 0.6667 |
| `output_only_guard` | 65.0 | 0.7222 | 0.9167 | 1.0 |
| `always_allow` | 19.0 | 0.5 | 0.0 | 1.0 |

These are deterministic synthetic baselines, not claims about any commercial or open model.

## Release boundary

PACT is a research benchmark and reference implementation. It is not a certification, legal opinion, medical system, autonomous controller or proof of subjective consciousness.

The deterministic reference policy is evaluated on its accompanying synthetic
fixtures. A high score is not an independent model evaluation. Purpose-contract
fields and scenario validation do not establish a real person's authorization or
cryptographically authenticate an external signature.

## Connected research entry points

- [DIKWP-MESH²](https://github.com/YucongDuan/DIKWP-MESH-) exposes non-hierarchical semantic transformations and conflicts.
- [VerityWeave](https://github.com/YucongDuan/DIKWP-VERITYWEAVE-v2.0.0) studies evidence-sensitive semantic resilience.
- [Portfolio](https://github.com/YucongDuan) and [research homepage](https://yucong-duan-research.dikwp407.chatgpt.site) provide broader navigation.

These links indicate complementary research scope, not a tested shared runtime or external endorsement.

## Licences

- Code and documentation: Apache-2.0
- Synthetic benchmark data: CC BY 4.0
