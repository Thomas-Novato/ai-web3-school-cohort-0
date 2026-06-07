# 2026-06-07 打卡草稿

## 今日学习：AI Security — 八大知识节点

### 核心收获
AI 安全的本质是**纵深防御架构**——不能指望模型自己识别所有攻击，而是在模型周围建多层防线。

### 学到的关键概念
1. **Prompt Injection** — 恶意内容改变模型任务，防护靠分层标注上下文可信级别
2. **Tool Abuse** — 工具被滥用，防护靠 rate limit、budget、simulation
3. **Malicious Context** — 上下文包含误导数据/错误事实
4. **Key Safety** — API key/private key/session key 安全
5. **Permission Isolation** — 不同操作不同权限级别
6. **Sandbox** — 执行环境隔离
7. **Audit Log** — 完整操作追溯
8. **Alert** — 异常行为实时通知

### 与项目的关联
Agent Resource Market 中：资源查询走只读流程、采购走权限隔离+Pact 预算控制、Pact 修改走人工确认+Audit Log、供应商注册走 Malicious Context 防护。

### 一句话总结
> AI 安全的本质不是让模型更聪明地拒绝攻击，而是在模型周围建多层防线——输入隔离、权限分级、沙箱执行、操作审计、实时告警。
