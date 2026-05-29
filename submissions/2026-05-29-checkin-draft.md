# 打卡草稿 — 2026-05-29

## 今日完成

- ✅ 学习 Agent Wallet 章节：理解 AI Agent 的受限授权原则
- ✅ 设计 Approval Tracker MVP：从概念到可落地的技术方案
- ✅ 明确核心技术路线：Etherscan logs.getLogs + eth_call allowance() 双重验证
- ✅ 制定风险评级规则（Critical → High → Medium → Low）
- ✅ 确定工程结构和双入口（CLI + Telegram Bot）
- ✅ 明确环境变量策略：ETHERSCAN_API_KEY 必需，BOT_TOKEN 按需，LLM key 可选
- ✅ 通过规则模板兜底，无 LLM key 也不影响 Demo 展示
- ✅ 明确安全边界和安全红线

## 学习收获

**核心认知：**
> AI 可以执行任务，但不能无边界地控制资产。

Agent Wallet 讨论的是如何安全授权，Approval Tracker 解决更前置的问题——用户到底已经给出过哪些权限？如果用户看不见自己的授权状态，后面谈 Session Key、Policy、Guard、Revocation 都会很抽象。

**技术亮点：**
- logs.getLogs + allowance() 双重验证，避免误报已失效授权
- 风险评级不简单判恶意，而是用多因子规则
- LLM 只能改写解释，不能新增事实 — 所有数据来自 API 和本地标签库
- 无 LLM key 时规则模板兜底，Demo 不受影响

**安全边界：**
❌ 不碰私钥 / 助记词 / 签名 / 交易 / revoke / 自动监控
✅ 只做 ERC-20 Approval 扫描 + allowance 校验 + 风险评级 + 中文报告

**项目路径：** `E:\歪脖3\AIWEB3\Hackthon\approval-tracker\`

**黑客松展示思路：**
1. CLI 扫描一个真实地址 → 展示风险表格
2. Telegram Bot /scan 命令 → 展示中文摘要
3. 强调安全边界：不签交易，只帮用户看清权限

## 明日计划

- [ ] 开始写 Approval Tracker：项目初始化 + 核心扫描逻辑

## 学习时长

~2 小时

## 仓库链接

https://github.com/Thomas-Novato/ai-web3-school-cohort-0

## Handbook 链接

https://aiweb3.school/zh/handbook/bridge/agent-wallet/
