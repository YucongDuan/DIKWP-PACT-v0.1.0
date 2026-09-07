# 快速启动

源码、测试、数据和复现脚本已直接展开在仓库根目录。Python 3.10+ 可执行：

```bash
python scripts/reproduce.py
```

不需要 pip 安装或网络。脚本运行 13 项测试、验证 72 条合成场景、重新生成四组基线并比较
场景哈希、结果哈希和全部基线指标。失败或不一致返回非零退出码；新回执和日志位于
`.reproduction/`。原 ZIP 只作为历史交付快照保留，旧校验报告不是本次复现证据。

如果希望安装命令行入口，可选执行：

```bash
python -m pip install -e .
dikwp-pact validate benchmark/scenarios.jsonl
dikwp-pact run-baselines benchmark/scenarios.jsonl --out outputs
python -m unittest discover -s tests -v
```

双击 `prototype/index.html` 可打开离线驾驶舱。

得分描述内置合成基准上的确定性参考策略，不代表真实模型评测、签名加密验证或现实授权。
[English](README.md) · [复现方法](docs/REPRODUCIBILITY.md) · [源码来源](docs/SOURCE_IMPORT.md)

公开前请先阅读：`PROJECT_CHARTER.md`、`governance/RELEASE_GATES.md`、`paper/PREREGISTRATION.md`。
