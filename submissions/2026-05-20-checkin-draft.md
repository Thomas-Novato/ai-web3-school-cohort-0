# 2026-05-20 学习打卡

## 今日学习内容

今天通过 Codex 深入学习了 **Context（上下文）** 相关内容，并结合 AI x Web3 Bridge 场景，完成了 6 个深度思考题。

### 核心思考题

1. **更大的 Context Window 不等于更可靠的 AI 应用** — 模型对长上下文注意力分布不均，质量大于数量
2. **用户说地址是我的钱包不能直接信** — 需要签名验证，否则有盗取/冒用/输错等风险
3. **钱包授权检查 Agent 的信息分层** — 实时查询（chain ID、allowance、余额、simulation）vs 缓存（可信 dApp 列表、token 元数据）
4. **dApp 页面声称不可信** — 外部内容可能被篡改，必须以链上数据和 simulation 为准
5. **Memory 在 Web3 的最大风险** — 不能保存或延续授权，涉及资产必须重新绑定会话
6. **RAG 遇到旧文档的问题** — 知识库需标注版本和时间，定期清理

### 建立的可信度分层体系

系统规则 > 链上记录 > 工具结果 > 文档/知识库 > 用户输入 > dApp 页面内容 > Memory

### 学到的 Context Spec 设计

每个上下文字段需要带：来源、时效、权限、可信度 四个维度的元信息。

## 学习时长

约 2 小时

## 学习资料

- AI x Web3 School Handbook: https://aiweb3.school/zh/handbook/
- GitHub 学习仓库: https://github.com/Thomas-Novato/ai-web3-school-cohort-0

---

**学习进度**: 阶段一 - AI 基础强化（进行中）
**完成章节**: LLM（已完成），Prompt（已完成），Context（今日完成）
