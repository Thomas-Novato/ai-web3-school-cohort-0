# Agent Resource Market — 项目总结

## 一句话定位

> Agent Resource Market 是一个让 AI Agent 在安全预算内自主采购 API 和算力的经济基础设施。它展示的不是单次付款，而是完整的 Agentic Commerce 流程：**任务触发 → 资源发现 → 比价决策 → CAW 授权支付 → 服务执行 → 结果验收 → 审计追踪**。

---

## 项目简介

这是一个面向 AI Agent 的资源采购市场。用户只需要给 Agent 一个任务和预算，例如 "用 2 USDC 帮我分析某个 Web3 项目风险"。Agent 会自动判断完成任务需要哪些资源——链上数据 API、行情 API、网页抓取 API、模型推理服务或算力 Worker——然后在市场中搜索、询价、比价、选择供应商，通过 Cobo Agentic Wallet 完成真实付款，最终调用资源输出结果。

核心理念不是"人类买 API 给 Agent 用"，而是 **Agent 自己管预算、自己采购、自己付款、自己完成任务**。

---

## 核心流程

```
用户提交任务 + 预算
    ↓
Agent 拆解任务
    ↓
判断需要 API / 算力资源
    ↓
Resource Market 返回候选供应商
    ↓
Agent 比价：价格、速度、成功率、可信度、gas
    ↓
生成采购计划
    ↓
CAW Pact 限制预算、地址、token、次数、时间
    ↓
Agent 通过 CAW 支付
    ↓
API / Compute Provider 返回结果
    ↓
Agent 验收结果
    ↓
输出最终报告 + 交易记录 + 审计日志
```

---

## 项目包含的模块

| 模块 | 内容 |
|------|------|
| 用户界面 | 输入任务、预算，查看 Agent 采购过程 |
| Planner Agent | 拆解任务，判断需要什么资源 |
| Resource Registry | 存放 API 和算力供应商信息 |
| Quote Engine | 获取报价，计算总成本 |
| Buyer Agent | 根据预算、质量和 gas 做采购决策 |
| CAW Payment Layer | 用 CAW 创建 Pact、执行支付、查询交易 |
| API Providers | 提供付费数据，比如链上数据、行情、新闻 |
| Compute Providers | 提供付费算力，比如风险评分、数据分析、推理任务 |
| Procurement Ledger | 记录每次采购原因、价格、tx hash、结果 |
| Audit 展示 | 展示 CAW 审计日志和被拒绝的越权操作 |

---

## CAW 的角色

CAW 是项目的资金核心，不是展示元素。

**它负责：**

- Agent 钱包托管和资金执行
- 通过 Pact 限制 Agent 的权限
- 限制单笔金额、总预算、收款方白名单、token、链、交易次数
- 执行真实链上付款
- 拦截超预算、未知地址、非授权 token 或非授权链
- 提供交易记录和审计日志

**Demo 里最好展示两类动作：**

1. ✅ 成功支付：Agent 买 API 或算力
2. ❌ 拒绝支付：Agent 尝试超预算或给非白名单地址付款，被 CAW 拦截

---

## 解决的问题

| 问题 | 项目如何解决 |
|------|-------------|
| Agent 不能自主购买服务 | 用 CAW 钱包直接完成支付 |
| API Key 依赖人类预注册 | 改成按次付费，付款后访问 |
| Agent 花钱不可控 | Pact 限制预算、地址、token、次数 |
| 不知道买哪个资源 | Agent 自动比价和评分 |
| gas 高低影响采购 | 把 gas 纳入总成本计算 |
| 付款和服务结果难绑定 | 用 tx_hash + payment_id + job_id 绑定 |
| 供应商质量不稳定 | 建立 reputation、成功率、延迟记录 |
| 评委看不出钱包价值 | 展示真实支付、审计日志和风控拒绝 |

---

## 推荐 Demo 场景

**用户输入：**
> "帮我分析某个 Web3 项目的风险，预算 2 USDC。"

**Agent 执行流程：**

1. 发现需要链上 holder 数据
2. 在 API 市场里找到 3 个数据 API
3. 选择性价比最高的 API，支付 `0.2 USDC`
4. 拿到数据后发现还需要风险评分模型
5. 在 Compute Market 里找到 3 个 Worker
6. 选择一个 Worker，支付 `0.5 USDC`
7. Worker 返回风险评分
8. Agent 输出报告
9. 展示两笔交易 hash、CAW Pact、Agent Wallet 地址
10. 再尝试购买一个 `3 USDC` 的资源，被 CAW 拒绝

---

## 可能被问的问题与回答

| 可能问题 | 回答思路 |
|----------|----------|
| 这和普通 API 市场有什么区别？ | 普通 API 市场面向人类开发者，依赖注册、充值、API Key；这个市场面向 Agent，Agent 可以按任务自动采购和付款。 |
| CAW 在里面是不是可替换？ | 不可替换。CAW 负责真实资金执行、Pact 权限控制、安全隔离和审计日志，是 Agent 能安全花钱的基础。 |
| Agent 会不会乱花钱？ | 不会。每个任务都有 Pact，限制预算、单笔金额、收款地址、token、链和过期时间。 |
| API Provider 是真的吗？ | MVP 可以有 1 个真实付费 API + 若干模拟 Provider。关键是支付和任务流程真实，后续可以扩展真实供应商。 |
| 算力是真 GPU 吗？ | Hackathon 版本可以用自建 Compute Worker 执行真实轻任务（CSV 分析、风险评分、网页摘要）。重点是采购和结算流程，不是搭完整云平台。 |
| 是否支持跨链？ | MVP 建议统一在 Base / Base Sepolia 结算。产品设计可以支持多链报价，但 Agent 会优先选择低 gas、低风险支付路径。 |
| gas 高怎么办？ | Agent 比价时计算 `资源价格 + gas + bridge fee + 风险成本`，不是只看服务价格。高 gas 链上的便宜资源可能会被拒绝。 |
| 如何防止恶意供应商骗钱？ | MVP 用白名单和 reputation；进阶版可加 escrow、结果验收、质押和仲裁。 |
| 如何证明付款对应某个服务？ | 每次采购绑定 `task_id`、`payment_id`、`tx_hash`、`provider_id`、`job_id`。 |
| 这个项目的护城河是什么？ | Agent-native resource manifest、采购历史数据、供应商信誉、CAW Pact 模板、Agent 采购 workflow。 |

---

## 主要难点与应对

| 难点 | 风险 | 处理方式 |
|------|------|----------|
| 真实 x402 / API 支付接入 | 时间可能不够 | 做一个最小付费 endpoint，其他先模拟 |
| CAW Pact 配置 | 配错会导致支付失败 | 先限定单链、USDC、白名单地址 |
| Demo 稳定性 | 链上交易和外部 API 可能慢 | 准备预录 tx、fallback 数据和短任务 |
| Compute Provider 复杂度 | 真 GPU 不稳定 | 自建 worker，跑轻量真实任务 |
| 结果验收 | Agent 不一定判断质量 | MVP 用 schema 校验 + 简单评分 |
| 跨链和 gas | 太复杂会拖垮 Demo | MVP 单链结算，跨链只做报价展示 |
| 安全问题 | Prompt injection 诱导付款 | Pact + allowlist + budget cap + 审计日志 |

---

## 打卡记录

| 项 | 内容 |
|---|------|
| **日期** | 2026-06-04 |
| **项目** | Agent Resource Market |
| **类型** | Hackathon 项目提案 & 思路梳理 |
| **关键词** | Agent Resource Market、CAW、Pact、Agentic Commerce、机器支付、资源采购 |
