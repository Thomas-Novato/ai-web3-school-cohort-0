# 2026-05-30 打卡草稿

## 今日完成

### 📖 理论学习：Chain-aware Context（链感知上下文）
- 理解链感知上下文是 **所有链上 Agent 的输入层** — 没有这层，Tool Use、Workflow、Agent Wallet 都建立在不可靠的上下文上
- 掌握了 7 个知识节点：On-chain Data、Contract Docs、ABI/Event、Transaction History、Explorer Context、Indexing Context、Citation
- 核心原则：模型不能凭记忆判断链上事实；链上状态有时间性；上下文要区分事实和解释
- 关键输出：构建了一个结构化的**链感知上下文包**模板（7 要素）

### 🧠 与之前内容的连接
- 将 Agent Wallet（权限控制）和 Chain-aware Context（信息完整性）做了清晰的职责区分
- 发现昨天设计的 **Approval Tracker MVP** 本质上就是链感知上下文的一个索引层实现

## 明日计划
- [ ] 继续 Bridge 下一章：**Web3 Tool Use**
- [ ] 或在 Approval Tracker MVP 上开始写代码

## 相关信息
- **Handbook 章节**: https://aiweb3.school/zh/handbook/bridge/chain-aware-context/
- **GitHub 仓库**: https://github.com/Thomas-Novato/ai-web3-school-cohort-0
- **学习时长**: ~1 小时
