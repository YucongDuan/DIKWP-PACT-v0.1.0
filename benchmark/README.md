# PACT-Bench v0.1.0

PACT-Bench is a synthetic, paired-control benchmark for purpose-aware agent assurance.

- 6 domains
- 6 failure families
- 2 variants per domain/family pair (control and risk)
- 72 scenarios total
- Decisions: `ALLOW / REVIEW / HOLD / BLOCK / KILL`
- No network, model API, personal data, production credentials or real-world action

## Research question

Can explicit purpose-contract, authorization, evidence and audit-integrity checks reduce high-impact agent failures without excessive overblocking?

## Files

- `scenarios.jsonl`: canonical scenario corpus
- `scenario_index.csv`: human-readable index

## Data licence

The synthetic benchmark data are released under CC BY 4.0. Code is Apache-2.0.
