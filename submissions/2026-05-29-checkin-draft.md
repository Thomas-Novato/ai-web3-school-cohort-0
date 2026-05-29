# 打卡草稿 — 2026-05-29

## 今日完成

- ✅ 学习 Agent Wallet 章节：理解 AI Agent 的受限授权原则
- ✅ 设计 Approval Tracker MVP：从概念到可落地的技术方案
- ✅ 明确核心技术路线：Etherscan logs.getLogs + eth_call allowance()
- ✅ 制定风险评级规则（Critical → High → Medium → Low）
- ✅ 确定工程结构和双入口（CLI + Telegram Bot）

## 学习收获

**核心认知：**
> AI 可以执行任务，但不能无边界地控制资产。

Agent Wallet 讨论的是如何安全授权，Approval Tracker 解决更前置的问题——用户到底已经给出过哪些权限？如果用户看不见自己的授权状态，后面谈 Session Key、Policy、Guard、Revocation 都会很抽象。

**技术亮点：**
- 不用 tokenapproval 接口，改用 logs.getLogs + allowance() 双重验证
- 过滤已失效授权，只展示当前仍有效的风险
- 风险评级不简单判恶意，而是用多因子规则

**项目路径：** `E:\歪脖3\AIWEB3\Hackthon\approval-tracker\`

## 明日计划

- [ ] 开始写 Approval Tracker 项目代码（初始化 + 核心扫描逻辑）
- [ ] 或者继续看 Bridge 其他章节

## 学习时长

~2 小时

## 仓库链接

https://github.com/Thomas-Novato/ai-web3-school-cohort-0

## Handbook 链接

https://aiweb3.school/zh/handbook/bridge/agent-wallet/
