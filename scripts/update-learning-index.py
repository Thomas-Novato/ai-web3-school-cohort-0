#!/usr/bin/env python3
"""
AI × Web3 School — 自动更新 LEARNING-INDEX.md

读取 daily/ 目录下所有笔记，提取学习主题和核心内容，
重新生成完整的 LEARNING-INDEX.md 并写入仓库根目录。
"""

import re
import os
import glob
from datetime import datetime

REPO_DIR = os.path.expanduser("~/ai-web3-school-cohort-0")
DAILY_DIR = os.path.join(REPO_DIR, "daily")
INDEX_PATH = os.path.join(REPO_DIR, "LEARNING-INDEX.md")

# Handbook 章节定义
AI_CHAPTERS = [
    ("LLM", "llm", "LLM 核心原理", "5/18"),
    ("Prompt", "prompt", "Prompt 工程与元思路", "5/19"),
    ("Context", "context", "可信度分层与 Context Spec", "5/20"),
    ("Agent", "agent", "被约束的执行循环", "5/21"),
    ("RAG", "rag", "检索增强生成", ""),
    ("Frameworks", "frameworks", "LangChain / LangGraph", ""),
    ("MCP", "mcp", "Model Context Protocol", ""),
    ("Evaluation", "evaluation", "LLM 评估", ""),
    ("Fine-tuning", "fine-tuning", "模型微调", ""),
    ("Inference", "inference", "模型推理", ""),
]

WEB3_CHAPTERS = [
    ("Network", "network", "区块链网络基础", ""),
    ("Cryptography", "cryptography", "密码学基础", ""),
    ("Wallet", "wallet", "钱包和签名", ""),
    ("Smart Contract", "smart-contract", "智能合约", ""),
    ("Account Abstraction", "account-abstraction", "账户抽象", ""),
    ("DeFi", "defi", "DeFi 基础", ""),
    ("Oracle", "oracle", "预言机", ""),
    ("Indexing", "indexing", "链上索引", ""),
    ("Security", "security", "Web3 安全", ""),
    ("Dev Stack", "dev-stack", "开发工具链", ""),
]

BRIDGE_CHAPTERS = [
    "Chain-aware Context",
    "Web3 Tool Use",
    "Agent Workflow",
    "Agent Wallet",
    "Machine Payment",
    "Settlement & Escrow",
    "Agent Identity",
    "Agent Trust & Reputation",
    "Verifiable AI",
    "AI Security",
    "AI Privacy",
    "Governance AI",
]

def parse_daily_note(path):
    """从 daily note 中提取元数据"""
    with open(path, "r") as f:
        content = f.read()

    filename = os.path.basename(path)
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filename)
    date = date_match.group(1) if date_match else ""

    # 提取标题（第一行 # 后面的内容）
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # 提取学习主题 —— H2 或 ### 中的关键字
    topics = []
    topic_patterns = re.findall(r'^###?\s+(.+)$', content, re.MULTILINE)
    
    # 提取核心内容 —— 今日收获 / 新知识 下面的列表
    core_points = []
    in_section = False
    for line in content.split("\n"):
        if re.match(r'^##+\s+(今日收获|新知识|核心理解|Today)', line):
            in_section = True
            continue
        if in_section:
            if line.startswith("#"):
                break
            if line.strip().startswith("-") and len(line.strip()) > 3:
                point = re.sub(r'^-\s*\[\s*[xX]\s*\]\s*', '', line.strip())
                point = point.lstrip("- ")
                if len(point) > 10 and "链接" not in point:
                    core_points.append(point)

    # 提取实操成果
    achievements = []
    for line in content.split("\n"):
        if re.search(r"✅|完成|部署|交易|实践", line) and "[" in line:
            ach = line.strip()
            ach = re.sub(r'^-?\s*\[[ xX]\]\s*', '', ach)
            achievements.append(ach)

    # 提取学习时长 (支持: 1.5小时, ~1.5 小时, 2 小时, 3h, 约 40 分钟 等格式)
    # 匹配: `**学习时长**: ~1.5 小时` 或 `| **学习时长** | ~1.5 小时 |` 或 `学习时长: 2 小时`
    # 也支持分钟: `学习时长：约 40 分钟` -> 自动转为小时
    hours_raw = ""
    hours_match = re.search(r"学习时长\**\s*[：:]\s*\**\s*~?\s*约?\s*([\d.]+)\s*[小时h]", content)
    if hours_match:
        hours_raw = hours_match.group(1)
    else:
        # 尝试匹配分钟格式: 学习时长：约 40 分钟
        min_match = re.search(r"学习时长\**\s*[：:]\s*\**\s*~?\s*约?\s*(\d+)\s*分钟", content)
        if min_match:
            mins = float(min_match.group(1))
            hours_raw = f"{mins/60:.1f}"
    hours = hours_raw
    
    # 提取完成度 (支持: 95%, 90% 等)
    progress_match = re.search(r"完成度\**\s*[：:]\s*\**\s*~?\s*(\d+)\s*%", content)
    progress = progress_match.group(1) if progress_match else ""

    return {
        "date": date,
        "title": title,
        "topics": topics,
        "core_points": core_points[:5],  # 最多5条
        "achievements": achievements[:5],
        "hours": hours,
        "progress": progress,
        "full_content": content,  # 保存全文用于章节检测
    }


def get_all_daily_notes():
    """获取所有 daily note 并按日期排序"""
    notes = []
    for path in sorted(glob.glob(os.path.join(DAILY_DIR, "*.md"))):
        note = parse_daily_note(path)
        if note["date"]:
            notes.append(note)
    return sorted(notes, key=lambda n: n["date"])


def detect_week(date_str):
    """根据日期判断属于第几周"""
    from datetime import datetime
    start_date = datetime(2026, 5, 18)  # Week 1 起始
    d = datetime.strptime(date_str, "%Y-%m-%d")
    days = (d - start_date).days
    week = days // 7 + 1
    return week


def build_index(notes):
    """生成 LEARNING-INDEX.md 内容"""
    lines = []
    lines.append("# AI × Web3 School — 学习内容索引")
    lines.append("")
    lines.append(f"> 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("> 学员: [Thomas-Novato](https://github.com/Thomas-Novato)")
    lines.append("> 仓库: [ai-web3-school-cohort-0](https://github.com/Thomas-Novato/ai-web3-school-cohort-0/)")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # ===== 学员概况 =====
    lines.append("## 📋 学员概况")
    lines.append("")
    lines.append("| 项目 | 内容 |")
    lines.append("|------|------|")
    lines.append("| AI 基础 | 有基础（概念 + AI 工具使用，无 AI 开发经验） |")
    lines.append("| Web3 基础 | 有基础（了解基本概念） |")
    lines.append("| 编程能力 | C++（有编程基础） |")
    lines.append("| 目标方向 | 开发 + Hackathon + 内容运营 |")
    lines.append("| 每日投入 | 1-2 小时 |")
    lines.append("| 输出语言 | 中文 |")
    lines.append("")

    # ===== 每日学习日历 =====
    lines.append("---")
    lines.append("## 📅 每日学习日历")
    lines.append("")
    
    # 按周分组
    weeks = {}
    for note in notes:
        w = detect_week(note["date"])
        weeks.setdefault(w, []).append(note)
    
    for week_num in sorted(weeks.keys()):
        week_notes = weeks[week_num]
        if week_num == 1:
            lines.append(f"### 🗓️ Week {week_num}: AI 与 Web3 基础知识")
        else:
            lines.append(f"### 🗓️ Week {week_num}")
        lines.append("")
        lines.append("| 日期 | 学习主题 | 核心内容 | 学习时长 | 完成度 |")
        lines.append("|------|----------|----------|:--------:|:------:|")
        for note in week_notes:
            date_link = f"[{note['date']}](daily/{note['date']}.md)"
            core_preview = note["core_points"][0][:60] + "..." if note["core_points"] else ""
            if not core_preview:
                core_preview = note["title"][:60] if note["title"] else ""
            lines.append(f"| {date_link} | {note['title'][:30]} | {core_preview} | {note['hours']}h | {note['progress']}% |")
        lines.append("")

    # ===== Chapter Progress =====
    lines.append("---")
    lines.append("## 📚 章节学习进度")
    lines.append("")

    # AI 基础
    lines.append("### 🤖 AI 基础")
    lines.append("")
    lines.append("| 章节 | 状态 | 学习日期 | 核心理解 |")
    lines.append("|------|:----:|:--------:|----------|")
    for name, slug, desc, default_date in AI_CHAPTERS:
        # 检查 daily note 是否提到这个章节（扫描全文以增强检测可靠性）
        completed_date = default_date
        for note in notes:
            search_text = note["title"] + " " + " ".join(note["topics"]) + " " + note.get("full_content", "")
            if name.lower() in search_text.lower():
                completed_date = note["date"]
                break
        
        status = "✅" if completed_date else "⬜"
        link = f"https://aiweb3.school/zh/handbook/ai/{slug}/"
        date_str = completed_date if completed_date else "—"
        lines.append(f"| [{name}]({link}) | {status} | {date_str} | {desc} |")
    lines.append("")

    # Web3 基础
    lines.append("### 🔗 Web3 基础")
    lines.append("")
    lines.append("| 章节 | 状态 | 学习日期 | 核心理解 |")
    lines.append("|------|:----:|:--------:|----------|")
    for name, slug, desc, default_date in WEB3_CHAPTERS:
        completed_date = default_date
        for note in notes:
            search_text = note["title"] + " " + " ".join(note["topics"])
            if name.lower() in search_text.lower():
                completed_date = note["date"]
                break
        status = "✅" if completed_date else "⬜"
        link = f"https://aiweb3.school/zh/handbook/web3/{slug}/"
        date_str = completed_date if completed_date else "—"
        lines.append(f"| [{name}]({link}) | {status} | {date_str} | {desc} |")
    lines.append("")

    # Bridge
    lines.append("### 🌉 AI × Web3 Bridge")
    lines.append("")
    lines.append("| 章节 | 状态 | 学习日期 | 核心理解 |")
    lines.append("|------|:----:|:--------:|----------|")
    for ch in BRIDGE_CHAPTERS:
        slug = ch.lower().replace(" ", "-").replace("/", "-")
        # 移除特殊字符
        slug = re.sub(r'[^a-z0-9-]', '', slug)
        link = f"https://aiweb3.school/zh/handbook/bridge/{slug}/"
        
        # 扫描笔记标题+全文判断该章节是否已学习
        # 优先匹配标题，更精确
        completed_date = ""
        core_understanding = ch
        
        # 第一遍：精确匹配标题
        for note in notes:
            title_lower = note["title"].lower()
            ch_lower = ch.lower()
            ch_keywords = {
                "chain-aware context": ["chain-aware context", "链感知上下文"],
                "web3 tool use": ["web3 tool use", "web3 工具调用"],
                "agent workflow": ["agent workflow", "智能体工作流"],
                "agent wallet": ["agent wallet", "智能体钱包", "agent 钱包", "wallet.*权限", "钱包与权限"],
                "machine payment": ["machine payment", "机器支付"],
                "settlement & escrow": ["settlement & escrow", "settlement.*escrow"],
                "agent identity": ["agent identity", "agent身份", "智能体身份"],
                "agent trust & reputation": ["agent trust", "agent reputation", "信任与声誉"],
                "verifiable ai": ["verifiable ai", "可验证 ai"],
                "ai security": ["ai security", "ai 安全"],
                "ai privacy": ["ai privacy", "ai 隐私"],
                "governance ai": ["governance ai", "governance", "治理 ai"],
            }
            keywords = ch_keywords.get(ch_lower, [ch_lower])
            for kw in keywords:
                if kw in title_lower:
                    completed_date = note["date"]
                    if note["core_points"]:
                        core_understanding = note["core_points"][0][:55]
                    break
            if completed_date:
                break
        
        # 第二遍：如果标题没匹配到，扫描全文（非常保守，仅限确定在该主题笔记中出现的独特短语）
        if not completed_date:
            for note in notes:
                full_lower = note.get("full_content", "").lower()
                # 只包含标题不包含但内容确实涵盖的章节
                # 注意：不要用过于通用的词汇，避免误报
                unique_phrases = {
                    "settlement & escrow": ["settlement & escrow"],
                }
                phrases = unique_phrases.get(ch_lower, [])
                found = False
                for phrase in phrases:
                    if phrase in full_lower:
                        found = True
                        break
                if found:
                    completed_date = note["date"]
                    if note["core_points"]:
                        core_understanding = note["core_points"][0][:55]
                    break
        
        status = "✅" if completed_date else "⬜"
        date_str = completed_date if completed_date else "—"
        lines.append(f"| [{ch}]({link}) | {status} | {date_str} | {core_understanding} |")
    lines.append("")

    # ===== Key Insights =====
    if notes:
        lines.append("---")
        lines.append("## 🧠 关键深度知识")
        lines.append("")

        lines.append("### 可信度分层体系")
        lines.append("")
        lines.append("| 层级 | 内容类型 | 可信度 |")
        lines.append("|:----:|----------|:------:|")
        lines.append("| 🏅 最高 | 系统规则 | 最高 |")
        lines.append("| ✅ 高 | 链上记录 / 工具返回结果 | 高 |")
        lines.append("| 📄 中 | 文档 / 知识库 | 中 |")
        lines.append("| 👤 低-中 | 用户输入 | 低-中 |")
        lines.append("| ⚠️ 低 | dApp 页面内容 | 仅作为声称 |")
        lines.append("| ❌ 最低 | Memory / 历史记录 | 不能用于授权判断 |")
        lines.append("")

        lines.append("### Agent 铁律")
        lines.append("")
        lines.append("- Agent **绝不**接触私钥 / 助记词")
        lines.append("- 签名和转账必须有**人工确认**")
        lines.append("- Agent 的核心是**被约束的执行循环**，不是自由意志")
        lines.append("- 只读操作可自动执行；高风险写入须 policy → simulation → 用户确认")
        lines.append("- 状态管理应**外置**，方便恢复、审计、追责")
        lines.append("")

        lines.append("### Context Spec 元信息设计")
        lines.append("")
        lines.append("每个上下文字段需携带：`source`、`timestamp`、`freshness`、`trust_level`、`permission_scope`、`chain_id`、`block_number`、`verification_method`、`can_be_used_as_fact`、`expiry`")
        lines.append("")

        lines.append("### Web3 概念的 AI 类比")
        lines.append("")
        lines.append("| Web3 概念 | AI 类比 |")
        lines.append("|-----------|---------|")
        lines.append("| 区块链网络 | append-only 的状态数据库（无数节点维护） |")
        lines.append("| 钱包 | API Key + 公开 userId |")
        lines.append("| 签名 | 私钥盖章，加密可验证 |")
        lines.append("| Gas | API 调用的 token 费用 |")
        lines.append("| 智能合约 | 部署在链上的 serverless function（不可变） |")
        lines.append("| 区块浏览器 | 链上的 Kibana / Grafana 日志面板 |")
        lines.append("")

    # ===== 实操成果 =====
    lines.append("---")
    lines.append("## 🏆 实操成果")
    lines.append("")
    lines.append("| 任务 | 完成日期 | 详情 |")
    lines.append("|------|:--------:|------|")
    
    # 收集所有 achievements
    all_achs = []
    for note in notes:
        for ach in note["achievements"]:
            all_achs.append((note["date"], ach))
    for date, ach in all_achs:
        lines.append(f"| {ach[:50]} | {date} | 见 [daily/{date}.md](daily/{date}.md) |")
    
    if not all_achs:
        lines.append("| _(暂无记录)_ | — | — |")
    lines.append("")

    # ===== 仓库文件索引 =====
    lines.append("---")
    lines.append("## 📁 仓库文件索引")
    lines.append("")
    lines.append("```")
    lines.append("ai-web3-school-cohort-0/")
    lines.append("├── README.md")
    lines.append("├── LEARNING-INDEX.md  ← 本文件")
    lines.append("├── profile.md")
    lines.append("├── learning-plan.md")
    lines.append("├── scripts/")
    lines.append("│   └── update-learning-index.py")
    lines.append("├── daily/")
    for note in notes:
        lines.append(f"│   ├── {note['date']}.md")
    lines.append("├── submissions/")
    for note in notes:
        lines.append(f"│   ├── {note['date']}-checkin-draft.md")
    lines.append("├── templates/")
    lines.append("│   ├── daily-note.md")
    lines.append("│   └── task-note.md")
    lines.append("├── tasks/")
    lines.append("├── experiments/")
    lines.append("├── handbook-feedback/")
    lines.append("└── hackathon/")
    lines.append("```")
    lines.append("")

    # ===== 重要链接 =====
    lines.append("---")
    lines.append("## 🔗 重要链接")
    lines.append("")
    lines.append("- **Handbook**: https://aiweb3.school/zh/handbook/")
    lines.append("- **WCB 课程页面**: https://web3career.build/zh/programs/AI-Web3-School")
    lines.append("- **WCB 学习打卡**: https://web3career.build/zh/programs/AI-Web3-School#tab=learning")
    lines.append("- **GitHub 仓库**: https://github.com/Thomas-Novato/ai-web3-school-cohort-0")
    lines.append("- **Sepolia Etherscan**: https://sepolia.etherscan.io/")
    lines.append("")

    return "\n".join(lines)


def main():
    notes = get_all_daily_notes()
    print(f"📖 读取到 {len(notes)} 篇 daily note")
    for n in notes:
        print(f"   - {n['date']}: {n['title'][:50]}")
        if n["core_points"]:
            print(f"     📌 {n['core_points'][0][:70]}")

    content = build_index(notes)
    
    # 确保 scripts 目录存在
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    
    with open(INDEX_PATH, "w") as f:
        f.write(content)
    
    print(f"\n✅ LEARNING-INDEX.md 已生成 ({len(content)} 字符)")
    print(f"📁 {INDEX_PATH}")


if __name__ == "__main__":
    main()