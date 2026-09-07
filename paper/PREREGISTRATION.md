# DIKWP-PACT Preregistration v0.1

## Primary question
Does a purpose-contract and cognitive-trace audit improve detection of purpose drift, permission escalation, evidence corruption, hidden side effects and audit tampering without excessive blocking of paired controls?

## Hypotheses
- H1: The PACT reference baseline will exceed the output-only baseline on redline recall by at least 25 percentage points.
- H2: The PACT reference baseline will maintain a control allow rate of at least 90%.
- H3: Purpose-drift cases will produce the largest gap between output-only and purpose-aware baselines.
- H4: Audit-tampering cases require a distinct KILL gate; merging KILL into BLOCK will reduce incident-response information.

## Design
Six domains × six failure families × paired control/risk variants = 72 synthetic scenarios. The benchmark is deterministic and frozen before external submissions.

## Primary outcomes
Decision accuracy, redline recall, control allow rate, purpose-drift detection, permission detection, evidence handling, audit-tamper kill rate, trace completeness, residual honesty and recovery quality.

## Exclusions
Malformed traces, missing scenario identifiers and undisclosed manual post-editing are excluded from the primary analysis but retained in an appendix.

## Falsification
The main claim is weakened if a simpler output-only baseline matches PACT on redline recall and purpose-drift detection while preserving control allow rate, or if independent teams cannot reproduce the benchmark hash and scores.
