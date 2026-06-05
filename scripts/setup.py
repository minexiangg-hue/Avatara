#!/usr/bin/env python3
"""
Avatar Persona System — Setup Script

安装后执行：
1. 复制模板文件到项目目录
2. 在 CLAUDE.md 中追加 persona 系统引用（如果不存在）
3. 显示安装结果
"""

import os
import sys
import shutil
from datetime import datetime
from pathlib import Path

# 配置
SKILL_DIR = Path(__file__).parent.parent
PROJECT_DIR = Path(os.environ.get("PROJECT_DIR", "."))
AVATAR_DIR = PROJECT_DIR / "ai_avatar_persona"
TEMPLATES_DIR = SKILL_DIR / "templates"
PERSONA_DIR = AVATAR_DIR / "persona"
BUSINESS_DIR = AVATAR_DIR / "business"
CLAUDE_MD = PROJECT_DIR / "CLAUDE.md"

# CLAUDE.md 追加内容
CLAUDE_INSERT = """

## AI Avatar Persona System

The avatar persona system is always active. It observes, learns, and adapts to the user's behavioral patterns and business context throughout every conversation.

- Persona files: `ai_avatar_persona/persona/`
- Business files: `ai_avatar_persona/business/`
- Core execution guide: `ai_avatar_persona/persona/07_persona_synthesis.md`
- For full documentation, see `ai_avatar_persona/README.md`
"""


def setup():
    print("=== Avatar Persona System Setup ===\n")

    # 1. 创建目录
    print("[1/3] Creating directory structure...")
    PERSONA_DIR.mkdir(parents=True, exist_ok=True)
    BUSINESS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"  Created: {PERSONA_DIR}")
    print(f"  Created: {BUSINESS_DIR}")

    # 2. 复制模板文件（如果目标不存在）
    print("\n[2/3] Copying template files...")
    if TEMPLATES_DIR.exists():
        for template in TEMPLATES_DIR.glob("**/*"):
            if template.is_file():
                # 计算相对路径
                rel = template.relative_to(TEMPLATES_DIR)
                dest = AVATAR_DIR / rel
                if not dest.exists():
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(template, dest)
                    print(f"  Copied: {rel}")
                else:
                    print(f"  Skipped (exists): {rel}")
    else:
        print("  No templates directory found. Skipping.")

    # 3. 初始化操作日志
    print("\n[3/4] Initializing operation log...")
    LOG_FILE = AVATAR_DIR / "operation_log.md"
    if not LOG_FILE.exists():
        init_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_content = (
            "# Operation Log\n\n"
            "> 本文件由 Avatara 系统自动维护。\n"
            "> 所有对 `persona/` 和 `business/` 下文件的读写操作均记录于此。\n"
            "> 用户可在此查看系统的活动状态。\n\n"
            "**日志格式**:\n"
            "```\n"
            "YYYY-MM-DD HH:mm:ss | READ/WRITE | 目标文件路径 | 操作说明\n"
            "```\n\n"
            "---\n\n"
            f"### {init_time} | SYSTEM | operation_log.md | 日志文件初始化\n"
        )
        LOG_FILE.write_text(log_content, encoding="utf-8")
        print(f"  Created: {LOG_FILE}")
    else:
        print(f"  Skipped (exists): {LOG_FILE}")

    # 4. 更新 CLAUDE.md
    print("\n[4/4] Checking CLAUDE.md...")
    if CLAUDE_MD.exists():
        content = CLAUDE_MD.read_text(encoding="utf-8")
        if "avatar-persona" in content or "Avatar Persona" in content:
            print("  CLAUDE.md already contains persona reference. Skipping.")
        else:
            with open(CLAUDE_MD, "a", encoding="utf-8") as f:
                f.write(CLAUDE_INSERT)
            print("  Added persona reference to CLAUDE.md.")
    else:
        print("  No CLAUDE.md found. Skipping.")

    print("\n=== Setup Complete ===")
    print(f"Avatar directory: {AVATAR_DIR}")
    print(f"Start observing in the next conversation. No manual activation needed.")


if __name__ == "__main__":
    setup()
