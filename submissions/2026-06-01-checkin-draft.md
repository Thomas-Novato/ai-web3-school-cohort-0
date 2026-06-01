# 2026-06-01 打卡草稿

## 今日学习主题：Agent Workflow（智能体工作流）

### 核心理解
Agent Workflow 的本质，是把概率模型放进确定性流程里。Web3 Agent 的成熟标志不是能不能自动操作，而是能不能在每一次操作前后都证明：为什么这样做、依据是什么、风险在哪里、谁确认了、失败后如何停止。

### 今日学习内容
1. **AI x Web3：Agent Workflow**
   - Task Graph：把目标拆成可控制的节点
   - State Machine：让执行过程有明确状态
   - Human-in-the-loop：按风险分层确认
   - Retry/Fallback：交易 pending 不能重复发送
   - Trace：记录每一步输入、判断和结果
   - Evaluation Harness：测试异常场景下是否安全停止
   - Regression Set：防止升级后安全性退化

2. **AI 应用实践：IELTS_Training / BandPath**
   - 设计了一个雅思备考工作台（非单点工具，而是学习陪跑系统）
   - 功能：Daily Mission + Adaptive Study Path + Practice/Review 闭环 + Mock Tests + Progress + Library
   - 面向中国大陆的生产架构：Next.js + NestJS + PostgreSQL + AI feedback adapter
   - AI 角色：结构化反馈、路径调整、复盘生成（非随便预测分数）

### 关键洞察
> Web3 Agent 不能只有"下一步推理"，必须有明确的状态、边界和停止条件。越接近真实资产，越需要显式流程、状态管理、人工确认、trace 和评估集。

### 学习时长
~1 小时

### Handbook 章节
https://aiweb3.school/zh/handbook/bridge/agent-workflow/

### GitHub 仓库
https://github.com/Thomas-Novato/ai-web3-school-cohort-0
