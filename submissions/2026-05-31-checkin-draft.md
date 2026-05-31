# AI x Web3 打卡笔记｜Machine Payment 机器支付

**日期**：2026-05-31
**关键词**：机器支付、稳定币、预算、报价、付款意图、x402、MPP、订阅、微支付、Agent 安全

---

## 1. 今日核心概念

**Machine Payment（机器支付）** 讨论的是 Agent、API、服务和钱包之间如何自动完成报价、授权、付款、收据和预算控制。

> Core Insight: Machine Payment 的核心不是付款，而是把**付款意图**和**实际结算**拆开。只有把这层拆开，Agent 的支付行为才可以被审计、被限制、被追责。

---

## 2. 第一性原理

> **Agent 不应该拥有无限支付能力。** Agent 只应该拿到和当前任务相关的、有限范围内的支付权限。

三大原则：
- **预算先于执行** — 没有预算边界就没有安全自动支付
- **报价必须可比较** — 价格、币种、有效期、退款条件
- **收据必须可验证** — 证明付给谁、为什么付、交付了什么

---

## 3. 关键知识节点

### Stablecoin Payment ⭐
稳定币适合机器支付。但 Agent 不能只看到"0.1"，必须知道是 0.1 USDC、USDT 还是 gas token、在哪条链、token address、decimals、余额、allowance、gas 谁付。
> ⚠️ **approve 是高风险动作，不能和付款混在一起。**

### Budget ⭐
用户授权给 Agent 的最大支出范围。预算必须分层：全局 → 任务 → 单次上限 → 服务方上限 → 频率限制 → 紧急停止。
> ⚠️ 只设总预算不设频率 ⇒ Agent 可能一次花光或重复购买。

### Quote ⭐⭐
服务方的可执行报价。必须含：服务内容、价格、币种、收款地址、有效期、交付条件、退款条件、quote id、签名。
**Agent 接受前检查三件事：** 预算内？服务方可信？quote 未过期？

### Payment Intent ⭐⭐
"用户/Agent 想为某个服务付款"的意图，不等于已结算。绑定：用户目标、服务方、最大金额、币种、链、quote 引用、是否自动重试、是否需要人工确认。

### x402 ⭐⭐
HTTP 402 → 付款 → 带证明重请求 → 交付。适合 API/数据/服务的小额按次付费。不解决服务质量、退款和长期订阅。

### MPP ⭐⭐
机器之间"谈生意"的协议：服务发现 → 报价 → 授权 → 结算 → 收据 → 重试 → 对账。链上只负责最终结算和争议证据。

### Subscription ⭐⭐
持续服务（月费 API、监控）。比单次更需要撤销。不能依赖无限 allowance，需每月上限 + 服务方白名单 + 扣款窗口 + 异常告警。
> ⚠️ **静默续费**：用户必须知道扣款时间、最高预算、能否随时停止。

### Micropayment ⭐⭐⭐
高频小额自动支付。经济账可能不划算（手续费 > 服务价值）。更适合：预付、L2、payment channel、链下累计 + 定期上链。

---

## 4. 在 AI × Web3 中的位置

```
用户授权预算 → Agent 获取 quote → policy 检查
→ 结算（escrow/直接）→ 服务交付
→ receipt → 记录 → 更新预算
```

Machine Payment 是 **Agentic Commerce 的基础设施**，连接 Agent Wallet、Policy、Settlement、Receipt 和 Service Delivery。

---

## 5. 最小实践 / 设计案例

**Agent 购买 API 的支付流程：**
1. 用户授权：今天最多 3 USDC
2. API 返回 quote：一次 0.1 USDC，5 分钟有效
3. Agent 检查预算、服务方身份、quote 是否过期
4. 钱包完成付款
5. API 返回结果和 receipt
6. 系统记录：quote、payment intent、交易哈希、结果、剩余预算

> 重点不是"付了 0.1 USDC"，而是每一步都有证据、限制和可审计记录。

---

## 6. 关联思考

之前做的 **Approval Tracker MVP** 解决授权可视化。Machine Payment 告诉我：授权之后还有预算、quote、收据三层需要管理。未来的 MVP 可以从 Approval 扩展到 Budget 和 Receipt，形成完整 Agent 资金管理工具链。

### 一句话记忆
> Machine Payment 的核心不是付款，而是把付款意图和实际结算拆开——让 Agent 的每一次消费都有预算约束、报价验证、收据溯源和全局可见性。

---

## 关联链接

- **Handbook**: https://aiweb3.school/zh/handbook/bridge/machine-payment/
- **GitHub 仓库**: https://github.com/Thomas-Novato/ai-web3-school-cohort-0
- **学习时长**: ~1 小时
