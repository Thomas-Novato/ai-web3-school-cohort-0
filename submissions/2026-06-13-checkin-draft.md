# WCB 打卡草稿 — 2026-06-13

## 今日学习内容

- **主题**: The Agent Economy Live 黑客松项目完整上传至 GitHub 组织仓库
- **核心认知**:
  - 项目定位为 **"AI Agent 的资本市场"**：围观全网 agent 经济 → 投资/下注看好的 agent → Cobo Agentic Wallet 在 MPC 签名前强制执行业务授权
  - **双层架构**: 宏观 Live（舞台）展示所有 ERC-8004/8183 agent → 可投资层（交易所）只有装 Cobo 钱包的 agent 能投
  - **三把锁机制**: Cobo Pact 防盗、AgentVault 强制分润、Cobo Owner 审批提供人类背书
  - 技术栈：Next.js 15 + Foundry 合约（16/16 测试通过） + Cobo Agentic Wallet + MCP Server
  - 合约已部署至 Base Sepolia（MockUSDC / VaultFactory / AgentMarket / FPMM）
  - text-swarm-hero 分支包含 171 个文件变更，23,934 行新增：Swarm 动效、排行榜、策略工作室、TG Bot、AgentJob 合约等

## 学习感悟

一个有真实技术深度和产品闭环的黑客松项目，比堆砌功能重要得多。The Agent Economy Live 的亮点不在于它有多少页面，而在于**整个信任模型是自洽的**：Cobo 在签名前强制执行策略、Vault 在合约层面保障分润、Owner 审批提供人类背书——这三个环节缺一不可，Cobo Agentic Wallet 是其中不可替代的核心。

## 今日实操成果

| 操作 | 状态 |
|------|------|
| 项目推送至 GitHub 组织仓库 `HelloAIxWeb3/The-Agent-Economy-Live` | ✅ |
| 分支 `new` 包含 text-swarm-hero 全栈版本已上传（5 commits 领先 main） | ✅ |
| 新增首页项目引导页 + 导航重构 | ✅ |
| 撰写今日 daily note | ✅ |

## GitHub 仓库

- **AIWeb3 学习打卡**: https://github.com/Thomas-Novato/ai-web3-school-cohort-0
- **黑客松项目仓库**: https://github.com/HelloAIxWeb3/The-Agent-Economy-Live
- **主要开发分支**: https://github.com/HelloAIxWeb3/The-Agent-Economy-Live/tree/new
