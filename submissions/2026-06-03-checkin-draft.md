# 2026-06-03 打卡草稿

## 今日学习
**主题：** Web3 Tool Use（Web3 工具调用）+ Hackathon 赛道一脑暴：Cobo Wallet 调研

### Web3 Tool Use 核心要点
- **第一性原理：** 模型可以选择工具，但工具必须用确定性边界限制模型
- **三条铁律：** 读写分离 | 参数结构化 | 日志不可省
- **8 个工具节点：** RPC Tool → Contract Read → Contract Write → Wallet Tool → Explorer Tool → DeFi Tool → Tool Permission → Tool Log
- 最大的风险点：Contract Write、Wallet Tool、DeFi Tool（直接面对资产变更）
- Bridge 核心概念全部完成 ✅

### Hackathon 赛道一脑暴：Cobo Wallet 改进方向
调研了 Cobo Wallet 产品线、技术能力和与 Fireblocks 的对比，发现：

**Cobo 的不足：**
1. 支付场景文档极少，缺乏端到端示例
2. 无 native fiat on/off ramp
3. CAW (Agentic Wallet) 刚发布，缺少 Agent 控制面板
4. 产品功能丰富但学习曲线陡峭

**推荐的 Demo 方向（方向一 + 方向四合并）：**
做一个 **Agent 间自动支付引擎**，包含：
1. 管理面板（预算、白名单、频次限制）
2. Agent A 发起支付任务给 Agent B
3. Agent B 执行后请求结算
4. Agent A 的 CAW 自动审批并扣款
5. Tool Log 记录所有操作
6. 可选集成 KYT 合规检查

## 今日产出
- ✅ 完成 Web3 Tool Use 章节学习
- ✅ 调研 Cobo Wallet 完整产品线和 API
- ✅ 与 Fireblocks 做竞品对比
- ✅ 产出 5 个可行 Demo 方向及优先级排序
- ✅ 更新 learning-plan.md（Web3 Tool Use 标记完成）
- ✅ GitHub 已推送

## 关键词
Web3 Tool Use、Cobo Wallet、CAW、Fireblocks、Hackathon 赛道一、Agent 支付、Permission 分层
