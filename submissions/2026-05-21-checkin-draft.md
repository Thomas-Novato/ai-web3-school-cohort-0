# 2026-05-21 打卡草稿

## 今日完成内容

### 📖 对话式学习任务
通过 Hermes Agent 完成了 Week 1 的完整学习包生成，包括：
1. **7 个 Web3 关键概念解释**（用 AI 类比理解 Network、Wallet、Signature、Gas、Smart Contract、Block Explorer、Account Abstraction）
2. **本周剩余 Checklist**（按优先级排序）
3. **6 个开放问题清单**（Agent 签名、Gas 经济、合约升级、DID 等）

### 🔗 Sepolia 测试网实操
- ✅ **钱包地址**: `0x540B477667F1d70796dfEee198948bBb79fD8024`
- ✅ **测试网交易**: `0x8095821118845b742b76a216a17039e835a3ee711ed1266a3829a577680d42a6`
  - [View on Etherscan](https://sepolia.etherscan.io/tx/0x8095821118845b742b76a216a17039e835a3ee711ed1266a3829a577680d42a6)
- ✅ **合约部署**: `0x540B477667F1d70796dfEee198948bBb79fD8024`
  - [View on Etherscan](https://sepolia.etherscan.io/address/0x540B477667F1d70796dfEee198948bBb79fD8024)

### 🧠 Agent 基础概念学习

学习了 Agent 的核心本质——**被约束的执行循环**，而不是"更自主的 AI"。

#### 关键理解
- Agent 需要：目标、工具、状态、权限、停止条件
- 工具调用带来真实执行风险（不只是回答错误）
- 只读操作可自动，高风险写入需 policy 检查 + simulation + 用户确认
- 状态应外置记录，方便恢复、审计和追责

#### AI × Web3 应用边界
- Agent 可以：分析提案、读取链上信息、生成交易草稿
- Agent 不能：绕过钱包授权、绕过用户确认
- 最小实践：DAO 提案研究 Agent（只读 + 分析，不执行投票）

### 今日状态
- ✅ 对话式学习任务完成
- ✅ Web3 概念 AI 类比梳理完成
- ✅ Sepolia 测试网交易完成
- ✅ 智能合约部署完成
- ✅ Agent 基础概念学习完成
- 🔲 交叉实验（待明天）

## 学习时长
3 小时

## GitHub 仓库
https://github.com/Thomas-Novato/ai-web3-school-cohort-0

## WCB 课程链接
https://web3career.build/zh/programs/AI-Web3-School#tab=learning

## 备注
> Week 1 核心任务基本完成：测试网交互 + 合约部署 + Agent 理论。Agent 的本质不是"更像人的 AI"，而是"有边界、有权限、有记录、有停止机制的任务执行系统"。明天做最小交叉实验。
