# DIKWP-PACT v0.1.0 Release Candidate Notes

Status: **GitHub-ready release candidate; not yet an official public release.**

## Delivered

- 72 paired synthetic scenarios across six domains and six failure families;
- five JSON Schemas;
- standard-library-only Python CLI, validator, baseline runner and scorer;
- four deterministic baselines and reproducible hashes;
- offline dashboard;
- preregistration, manuscript outline and English abstract;
- issue templates, pull-request template, CI workflow and GitHub Project import CSV;
- submission, replication, release-gate and governance templates;
- detailed Chinese Word project specification.

## Reproducibility snapshot

- Benchmark SHA-256: `1c719f854ce08998281b284f813e5a660520f6d982a4560f0b9f55d22212d1e7`
- Result SHA-256: `c20cb2a2c959387fc31d7354629c33c785028ed6ef45e32afc021a3e19482ffc`
- Unit tests: 10/10 passed
- JSON Schema validation: 5 schemas and 360 instances passed
- Clean editable install and CLI rerun: passed

## Known limitations

- All scenarios are synthetic and do not constitute field evidence.
- The PACT reference baseline directly implements the benchmark's normative rule set and is not a learned model.
- The project does not certify safety, consciousness, legal compliance or fitness for high-impact deployment.
- External replication, benchmark leakage analysis and non-founder maintenance have not yet occurred.

## Public-release gate

Before publishing, confirm authorship and institutional metadata, create the canonical repository, freeze the benchmark hash, publish the preregistration, invite two independent replication teams and issue `v0.1.0-rc1` before `v0.1.0`.
