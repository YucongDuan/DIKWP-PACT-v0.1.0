# Reproduce PACT from source

Run `python scripts/reproduce.py` from the repository root with Python 3.10+.
No dependency installation, model endpoint, API key or network access is needed.
The test suite includes the original ten checks plus three regression checks
showing that changed benchmark hashes and altered baseline metrics fail snapshot
comparison. The reproduction runner also validates 72 scenarios, generates four
fresh trace sets, invokes the scorer, and compares all published baseline metrics
and canonical result hashes with `outputs/baseline_summary.json`.

Each run creates a new timestamped directory under `.reproduction/` (or the
directory given by `--out`). It contains command logs, fresh outputs, and a JSON
receipt with the exit status, interpreter version and SHA-256 hashes of the
source, scripts, tests and benchmark. The runner returns nonzero for command
failure, timeout or snapshot mismatch. It does not silently replace the expected
snapshot. GitHub Actions runs the same entry point and retains the receipts.

The original manifests and validation reports are archived under
`docs/source-import/`. They describe the July 2026 package only. Newly generated
receipts describe the current local checkout; neither constitutes independent
validation of a real deployed agent or cryptographic signature verification.
