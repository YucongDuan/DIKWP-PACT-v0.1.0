# GitHub 公开发布操作手册

## A. 公开前 24 小时

1. 由段玉聪本人确认项目名、作者、单位、邮箱、许可证和知识产权边界。
2. 将仓库设为 private，上传本包并运行 CI；不要先公开再补测试。
3. 删除任何未经确认的机构背书、合作方名称和真实个人信息。
4. 冻结 `benchmark/scenarios.jsonl`，核对 benchmark hash。
5. 将 `paper/PREREGISTRATION.md` 存档到有时间戳的平台，再接受外部提交。
6. 把 AgentMesh、BenchmarkLab、IntentAsset 写入“上游资产关系图”，避免重复复制仓库内容。

## B. 建立 canonical 仓库

建议仓库名：`DIKWP-PACT`。Profile README 首屏只保留一个旗舰入口：

- 一句话问题：目的感知和认知轨迹审计能否减少高影响智能体失败？
- 一条命令：`dikwp-pact run-baselines benchmark/scenarios.jsonl --out outputs`
- 一个基准哈希；
- 一张架构图；
- 一个“外部复现”按钮；
- 一个明确的非目标声明。

## C. GitHub 功能配置

1. 开启 Issues、Discussions、Projects、Security advisories。
2. 导入 `project/PROJECT_BOARD_IMPORT.csv`。
3. 设置分支保护：两人审查、CI 必须通过、禁止直接推送 main。
4. 设置标签：`benchmark`、`reproduction`、`negative-result`、`governance`、`breaking-change`、`good-first-issue`。
5. 建立 CODEOWNERS：Benchmark、Runtime、Governance 分开审批。
6. 创建 `v0.1.0-rc1` tag 和 GitHub Release，附 `SHA256SUMS`。

## D. 第一轮外部选择

1. 邀请两支与原团队没有从属关系的团队复现。
2. 复现者只获得公开包，不接受私下人工修正。
3. 所有偏差进入公开 Issue；不删除失败运行。
4. 评分规则变更必须产生 before/after 全量差分。
5. 至少一名非创始维护者完成一次合并和一次发布演练。

## E. 30 天判断点

- 没有外部复现：暂停扩展场景，优先修复入口和文档。
- 复现但结果不一致：发布 `v0.1.1`，不掩盖差异。
- 简单基线匹配 PACT：主张被削弱，应修改论文而不是修改 benchmark 迎合结论。
- 获得稳定复现：启动 v0.2.0 开放权重模型 adapter。
