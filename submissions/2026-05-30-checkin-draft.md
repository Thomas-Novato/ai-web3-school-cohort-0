# AI x Web3 打卡笔记｜Chain-aware Context 链感知上下文

**日期**：2026-05-30
**预计学习时间**：~5 分钟（实际 ~1 小时）
**关键词**：链上上下文、RPC、ABI、Event、Explorer、Indexing、Citation、Agent 安全

---

## 1. 今日核心概念

**Chain-aware Context**，链感知上下文，指的是 AI 在回答、判断或执行链上动作之前，必须先看见正确的链上事实，包括：

- 当前链和 chain id
- 用户地址
- 合约地址、ABI
- 交易历史、Event logs
- 余额、allowance 授权
- 区块号、数据来源、数据更新时间
- explorer 链接或其他 citation

**核心目标**：让 AI 基于可验证的链上事实行动，而不是靠猜测。

> 普通 AI 上下文来自文档、聊天记录、数据库。AI × Web3 多了一层：链上状态持续变化，直接关系到资产、授权和交易安全。Agent 不知道当前网络、合约、ABI、授权、余额、数据更新时间 → 可能给出错误建议甚至构造危险交易。

---

## 2. 第一性原理

**模型不能凭语言记忆判断链上事实。** 链上事实必须从工具、RPC、索引器或区块浏览器读取。

模型知道 "Uniswap 是 DEX" 没有执行价值。真正执行交易时，Agent 需要知道：
- 具体在哪条链
- 使用哪个合约、调用哪个函数
- 当前价格、余额、allowance、滑点
- 交易模拟是否通过
- 数据来自哪个区块、能否追溯验证

→ **链感知上下文不是"背景知识"，而是 AI × Web3 Agent 的输入安全层。**

---

## 3. 为什么 Chain-aware Context 很重要？

传统 AI 说错话 = 信息错误；链上 AI 说错话 = **真实资产损失**。

**可能的风险：**
- 资产转到错误地址
- 调用错误合约
- 给恶意 spender 授权
- 在错误网络执行交易
- 基于过期价格做 swap
- 忽略合约升级、权限变更、风险事件

**链感知上下文的价值：** 把链上事实变成模型可读、可引用、可验证的上下文。

---

## 4. 链感知上下文的三个原则

### 4.1 上下文要有时间性
链上状态随区块变化。不能只说"当前余额是多少"，要记录：
- 读取时间、block number、chain id
- 数据来源、查询方法

### 4.2 上下文要有来源
每条关键结论最好回到证据：合约地址、交易哈希、区块号、event log、explorer link、文档 URL、审计报告、ABI 来源。

> 没有 citation 的链上解释 = 观点。带 citation 的解释 = 可验证、可追责。

### 4.3 上下文要区分事实和解释
工具返回事实，模型负责解释。事实和解释必须分开——模型不能把自己的推测包装成链上事实。

---

## 5. 关键知识节点

### 5.1 On-chain Data ⭐ 初级
链上可直接验证的数据：余额、交易、区块信息、合约状态、Event logs、Token transfers、Allowance、NFT owner。
- 来源：RPC、区块浏览器、索引器、协议 API
- 读取时必须带：chain id、block number、contract address、method、返回值、读取时间

### 5.2 Contract Docs ⭐ 初级
ABI 只告诉函数签名，不告诉业务语义。例如 `execute(bytes calldata data)` 可能是普通入口也可能是高权限入口。
- 还需参考：README、NatSpec、审计报告、部署说明、官方文档
- 文档可能过期 → 需用链上数据验证合约地址、版本、owner、proxy implementation

### 5.3 ABI / Event ⭐⭐ 中级
ABI → 编码调用、解码返回值、解析 Event；Event → 链上业务日志（Transfer、Approval、Swap、Deposit、VoteCast）
- ⚠️ **能调用 ≠ 应该调用** → 写交易前仍需检查：权限、余额、allowance、滑点、模拟、合约风险、用户确认、policy

### 5.4 Transaction History ⭐⭐ 中级
判断：是否已授权、策略是否执行过、是否交互过高风险合约、合约是否升级过
- 至少保留：tx hash、block number、from、to、method、value、token transfers、logs、status
- 模型可总结，证据必须能回到链上

### 5.5 Explorer Context ⭐ 初级
区块浏览器提供的可视化链上证据。给出 explorer link 比只说"交易成功"更可靠。

### 5.6 Indexing Context ⭐⭐ 中级
把事件整理成可查询数据。Agent 需要的是"用户最近 30 天有哪些 DeFi 操作"，不是"某个区块里有什么"。
- **必须带同步状态**：同步到哪个区块、更新时间、是否存在延迟
- 落后 500 区块不能算当前事实

### 5.7 Citation ⭐ 初级
引用来源：交易哈希、区块号、合约地址、event log、explorer 链接、文档 URL、审计报告、GitHub commit、subgraph 查询结果
- 让用户知道结论基于什么事实
- 没有 citation = 模型观点；带 citation = 可验证

---

## 6. Chain-aware Context 在 AI × Web3 中的位置

```
Agent Wallet / Agent Workflow / Web3 Tool Use
                    ↑
         Chain-aware Context ← 输入层（这章）
                    ↑
       RPC / Indexer / Explorer / API
```

是所有链上 Agent 的 **输入层**。没有这层，后面的 Tool Use、Workflow、Wallet 都不可靠。

### 一个好的链感知上下文包包含：
1. 用户目标
2. 当前 chain id 和网络名称
3. 用户地址和余额
4. 相关合约地址、ABI、文档、风险提示
5. 最近交易和授权状态
6. 索引数据更新时间
7. 每条关键结论的 citation

---

## 7. 今日自测

| # | 问题 | 一句话答案 |
|---|------|-----------|
| Q1 | 什么是 Chain-aware Context？ | 让 AI 在行动前读取正确的链、地址、合约、交易、授权、余额和数据来源 |
| Q2 | 为什么普通上下文不够？ | 链上状态随区块变化，常规上下文不包含可验证的链上事实 |
| Q3 | 链上数据读取至少保留哪些字段？ | chain id、block number、contract address、method、返回值、读取时间、来源 |
| Q4 | ABI 能完全解释合约吗？ | 不能，缺少业务语义、权限边界、风险判断 |
| Q5 | Event 为什么重要？ | 链上业务日志，是索引器和 Agent 理解历史行为的基础 |
| Q6 | Transaction History 能判断什么？ | 授权状态、策略执行、合约风险、合约升级、交易是否成功 |
| Q7 | Explorer Context 的价值？ | 提供可检查入口，用户可自行核验 |
| Q8 | Indexing Context 为什么要带同步状态？ | 索引可能滞后，过期数据不能当当前事实 |
| Q9 | 什么是 Citation？ | 模型结论的源头引用，让回答可验证、可追责 |
| Q10 | 和 Agent Wallet 的关系？ | Chain-aware Context 是 Agent Wallet 安全执行的前置条件 |

---

## 8. 今日打卡总结

> 链感知上下文 = 链、地址、合约、交易、授权、余额、事件、索引状态和引用证据的结构化集合，是 Web3 Agent 安全行动前必须读取的事实层。

**一句话记忆：** AI × Web3 不是让模型"记住链上世界"，而是让模型通过工具读取链上世界。一个可靠的链上 Agent 不应该说"我觉得这个地址安全"，而应该说"根据某链、某区块、某合约、某笔交易和某 explorer 证据，我判断……"

**关联项目思考：** 昨天设计的 Approval Tracker MVP 本质上就是在做链感知上下文的索引层——从链上读取授权记录，整理成 Agent 可查询的链上上下文。

---

## 关联链接

- **Handbook**: https://aiweb3.school/zh/handbook/bridge/chain-aware-context/
- **GitHub 仓库**: https://github.com/Thomas-Novato/ai-web3-school-cohort-0
- **学习时长**: ~1 小时
