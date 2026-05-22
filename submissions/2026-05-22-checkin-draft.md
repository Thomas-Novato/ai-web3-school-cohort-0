# 2026-05-22 打卡提交草稿

## 今日学习

**主题**: AI 应用工程化：MCP 与 Eval

**学习时长**: 2.5 小时
**完成度**: 85%

### 学习内容

1. **MCP（Model Context Protocol）**
   - Server/Client 架构
   - Tool Schema 设计规范
   - Permission 权限管理（最易被低估）
   - Server 的边界设计原则

2. **Eval（评估体系）**
   - Harness 测试框架
   - Golden Set 黄金测试集（30-100 条高质量样本）
   - LLM-as-Judge（规则+LLM+人工三级配合）
   - Regression 回归测试（修 A 坏 B 的应对策略）
   - Observability 可观测性（线上行为反哺 Eval）

3. **AI × Web3 中的位置**
   - MCP 负责工具发现和调用格式
   - Eval 负责持续发现系统不可靠场景
   - Web3 账户系统负责最终权限和执行边界
   - ⚠️ MCP ≠ 钱包安全，Eval ≠ 权限控制

### 最小实践方案
- 搭建只读 MCP Server（search_docs / get_file）
- 准备 30 条 Eval 样本覆盖正常/边界/历史 bug/注入场景

## GitHub 仓库
https://github.com/Thomas-Novato/ai-web3-school-cohort-0

## 学习日志

- 笔记: https://github.com/Thomas-Novato/ai-web3-school-cohort-0/blob/master/notes/
- 今日笔记: daily/2026-05-22.md
