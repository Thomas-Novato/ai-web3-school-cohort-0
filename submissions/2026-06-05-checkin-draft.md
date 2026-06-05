# 2026-06-05 打卡草稿

## 今日学习
**主题：** 钱包与权限：执行型 Agent 的安全地基

### 核心理解
AI x Web3 产品最危险的地方不是模型会回答错误，而是模型的错误判断可能被执行成真实链上操作——一次错误授权、转账或 swap 往往是不可逆的。钱包与权限层是所有执行型 Agent 的基础设施，决定了 Agent 能读还是能写、用户是否看得懂授权了什么、出错后能否撤销。

核心原则六条：
1. 权限要具体
2. 签名前要可理解
3. 执行前要可模拟
4. 执行中要可限制
5. 执行后要可追溯
6. 长期权限必须可撤销

### 今日学习内容

**1. AI Wallet UX — 让每次确认都有意义**
AI Wallet 的 UX 重点不是把聊天框接到钱包，而是让用户清楚知道：Agent 正在执行什么任务、为什么要执行、下一步会发生什么、需要什么权限、签名后资产如何变化、最坏情况损失多少、如何停止或撤销。
一个合格的 AI Wallet 界面至少展示：用户目标 → 行动计划 → 权限请求 → 交易解释 → 风险提示 → 撤销入口。目标不是"减少确认次数"，而是让每一次确认都有意义。

**2. Permission Policy — 给系统执行的规则**
Policy 是程序可执行的规则，不是用户愿望，不能靠模型自觉遵守。常见维度：
- 资产范围：只允许 USDC，不允许 ETH 或 NFT
- 金额上限：单笔、每日、每周、总额度
- 目标合约：只能调用白名单协议
- 函数范围：允许指定 swap 函数，禁止任意 approve
- 价格与滑点：超过阈值必须重新确认
- 时间窗口：权限几小时或几天后自动失效
- 频率限制：防止 Agent 短时间连续执行
AI 可以协助生成 policy 草稿，但真正执行必须由钱包、智能账户、后端 guard 或合约模块校验。

**3. Session Key Flow — 临时受限执行**
Session Key 是给特定任务临时使用的受限 key，适合低风险高频操作：小额支付、游戏动作、重复查询、白名单范围内的小额交易。
基本流程：用户用主钱包创建 session key → 设置权限范围 → Agent 使用 session key 发起操作 → 钱包或 smart account 校验 policy → 到期/额度用完/手动撤销后失效。
价值是减少重复签名，但不能绕过风控——额度太大、时间太长、函数太宽，本质上只是把主钱包风险换了个名字。

**4. Safe Guard — 交易前的确定性检查器**
Guard 不关心模型为什么建议这笔交易，只关心交易是否符合规则。在 Agent 场景中可以检查：
- 目标地址是否在白名单
- calldata 是否调用了允许的函数
- token approval 是否超过额度
- swap 滑点是否过大
- 接收地址是否属于用户或授权对象
- 交易模拟结果是否符合预期
- 操作频率是否异常
设计原则：用确定性规则拦住不该发生的动作，用人工确认处理规则覆盖不了的灰区。

**5. ERC-4337 Workflow — 可编程账户体系**
ERC-4337 让账户不再只是 EOA 私钥，而可以变成可编程的 smart account。对 AI Agent 的价值：
- 权限可以进入账户层
- gas 可以由 paymaster 处理
- 多步操作可以批量执行
- 账户恢复和风控逻辑可以模块化
- Agent 不需要直接持有主私钥
简化流程：Agent 生成交易意图 → 包装成 UserOperation → Smart account 校验签名/nonce/权限 → Bundler 打包提交给 EntryPoint → Paymaster 代付 gas → 链上执行后记录结果和失败原因。
重点不是"让 Agent 更方便转账"，而是让账户本身拥有可编程的权限和安全边界。

**6. Pre-transaction Simulation — 签名前模拟**
这是 Agent 钱包必须具备的基础能力。模型解释 calldata 只能作为辅助，真正的安全判断来自结构化解析和链上模拟。
模拟需要回答：会改变哪些 token 余额、会产生哪些授权、会调用哪些合约、是否可能失败或 revert、价格/滑点/手续费是否符合预期、是否会产生无限授权等额外风险。
模拟结果需要翻译成人能理解的语言，但关键字段不能靠模型自由发挥，必须来自链上模拟和结构化解析。

**7. Recovery / Revocation — 撤销从第一天开始**
只要给 Agent 权限，就必须设计恢复和撤销。用户应该能在一个地方看到：
- 当前有哪些 Agent 或 session key
- 每个权限能操作哪些资产和合约
- 已经使用了多少额度
- 权限什么时候过期
- 最近执行过哪些动作
- 如何暂停、撤销、轮换或恢复账户
更高价值场景还需要考虑：guardian、多签、延迟执行、社交恢复、硬件钱包确认、异常冻结。不要等事故发生后才补撤销入口。

### AI x Web3 安全分级
钱包与权限是执行型 Agent 的地基。没有权限层 Agent 只能停留在问答阶段；权限层做错又会直接威胁资产安全。应按风险逐步开放能力：

| 阶段 | 能力 | 说明 |
|:--|:--|:--|
| 第一阶段 | 只读 | Agent 只能读取链上数据、余额、交易记录、授权状态 |
| 第二阶段 | 生成交易草稿 | Agent 可以生成交易建议，但必须由用户手动签名 |
| 第三阶段 | 小额自动执行 | 允许小额、白名单、短期 session key 自动执行 |
| 第四阶段 | 复杂自动化 | guard + simulation + 日志 + 审计 + 撤销 + 人工确认 + 异常处理 |

### 最小实践：AI 自动小额换币助手

**✅ 允许操作**
- 允许 token：USDC、ETH、DAI
- 目标 DEX：Uniswap、1inch 等白名单协议
- 最大单笔金额：50 USDC
- 每日总额度：200 USDC
- 最大滑点：1%
- session key 有效期：24 小时

**❌ 禁止操作**
- 禁止无限 approve
- 禁止调用非白名单合约
- 禁止转账给非用户授权地址
- 禁止操作 NFT
- 禁止跨链桥转账
- 禁止超过额度后继续执行

**⚠️ 必须重新确认的情况**
- 单笔金额超过上限
- 每日额度即将耗尽
- 目标合约不在白名单
- 滑点超过 1%
- 模拟结果显示余额变化异常
- 出现新的 token approval
- 交易接收地址不是用户本人或白名单地址

**交易模拟需要展示**
输入资产和数量、输出资产和预估数量、最大损失、滑点、gas 费用、目标合约、调用函数、是否产生授权、失败或 revert 风险。

**执行日志需要记录**
Agent 为什么发起这笔交易、使用了哪个 session key、调用了哪个合约和函数、实际花费了多少、模拟结果和真实执行结果是否一致、用户是否可以撤销相关权限。

### 今日总结
这一节的核心不是"Agent 怎么拥有钱包"，而是"Agent 如何在不直接控制用户资产的情况下安全执行任务"。真正靠谱的 Agent 钱包设计不依赖模型自律，而依赖：可编程账户、有边界的权限、session key、guard、交易模拟、撤销机制、人类可理解的 UX。最终目标是让 Agent 具备执行能力，但不让它拥有无限权力。

## 与项目关联
Agent Resource Market 中 CAW Payment Layer 和 Pact 控制器的设计直接对应今天所学：
- Pact 限制 = Permission Policy（预算上限、收款地址白名单、token 限制、交易次数限制）
- CAW 拦截 = Safe Guard（超预算拦截、未知地址拒绝、非授权 token 拒绝）
- 审计追踪 = Tool Log（采购原因、tx hash、执行结果、被拒绝记录）
- 钱包界面 = AI Wallet UX（展示任务目标、行动计划、风险提示、撤销入口）
- Pact 撤销机制 = Recovery / Revocation

## 今日产出
- ✅ 完成钱包与权限章节完整学习
- ✅ 掌握 7 个核心知识节点：AI Wallet UX、Permission Policy、Session Key Flow、Safe Guard、ERC-4337 Workflow、Pre-transaction Simulation、Recovery/Revocation
- ✅ 理解安全分级框架：只读 → 草稿 → 小额自动 → 复杂自动化
- ✅ 设计"AI 自动小额换币助手"完整权限策略案例（允许/禁止/重确认三个维度）
- ✅ 将所学知识与 Agent Resource Market 项目做关联映射（Pact/Permission Policy、CAW/Guard、审计/Tool Log）
- ✅ 和团队讨论 Hackathon 任务分配方向
- ✅ Daily note + GitHub 已推送

## 关键词
钱包与权限、AI Wallet UX、Permission Policy、Session Key、Safe Guard、ERC-4337、Transaction Simulation、Recovery、Revocation、Agent Resource Market、Pact、CAW、Agentic Wallet

## 本周学习路线图
```
已完成    5/30  Chain-aware Context
已完成    5/31  Machine Payment
已完成    6/1   Agent Workflow
已完成    6/3   Web3 Tool Use
今日完成  6/5   钱包与权限：执行型 Agent 的安全地基 ← 🆕
下一步    6/6+  技术方案设计 / AI Security & AI Privacy
```
