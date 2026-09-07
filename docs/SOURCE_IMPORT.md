# Source-visible migration / 源码展开记录

Date: 2026-09-07.

The previous GitHub root contained only the ZIP, README and Apache-2.0 LICENSE.
The ZIP's single top-level directory has been flattened into the repository root,
making source, tests, schemas, benchmark data and documentation directly visible.

- Original file: `DIKWP_PACT_Open_Purpose_Assurance_Project_v0.1.0.zip`
- Original SHA-256: `312ad57cb529117b6381f8716d1f9ab01d219b3ceb1a9790761197e08eefe191`
- Archive: 77 entries; 1,576,257 uncompressed bytes.
- Rejected import hazards checked: traversal paths, absolute paths, symlinks,
  encrypted entries and duplicate case-folded paths. None found in this archive.
- The public full Apache-2.0 LICENSE is retained; the archive's copyright notice
  is preserved as `NOTICE`; benchmark `DATA_LICENSE.md` remains CC BY 4.0.
- Original manifests/validation reports remain under `docs/source-import/`.
- The previous short public README is preserved as `docs/PREVIOUS_PUBLIC_README.md`.

Analytical source and benchmark records are unchanged. New material adds source
navigation, reproduction checks, CI and explicit evidence boundaries. The original
ZIP remains available for archival comparison; Git history is not rewritten.

中文：此变更解决“只能下载 ZIP 才能查看源码”的问题，并增加可失败、可留回执的真实复现入口。
它不将合成数据上的参考策略得分扩大为外部模型能力或真实授权验证。
