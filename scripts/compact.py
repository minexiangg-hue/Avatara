#!/usr/bin/env python3
"""
Avatara Compact — 压缩经验文件

辅助脚本，处理压缩过程中机械化的部分（计数、裁剪、日期范围提取），
内容压缩提炼由 AI 完成。

用法:
  python compact.py status          查看三个文件的状态和条目数
  python compact.py trim-log        保留 operation_log.md 最近100条
  python compact.py date-range      获取 experience_stream 的日期范围
"""

import re
import sys
from pathlib import Path

AVATAR_DIR = Path("ai_avatar_persona")
STREAM_FILE = AVATAR_DIR / "business" / "00_experience_stream.md"
EVOLUTION_FILE = AVATAR_DIR / "persona" / "06_evolution_log.md"
LOG_FILE = AVATAR_DIR / "operation_log.md"
MAX_LOG_ENTRIES = 100


def count_entries(filepath):
    """统计文件中有编号/日期的条目数。"""
    if not filepath.exists():
        return 0
    content = filepath.read_text(encoding="utf-8")
    entries = re.findall(r'^###\s', content, re.MULTILINE)
    return len(entries)


def status():
    """显示三个文件的条目数和大小。"""
    for name, path in [
        ("experience_stream", STREAM_FILE),
        ("evolution_log", EVOLUTION_FILE),
        ("operation_log", LOG_FILE),
    ]:
        count = count_entries(path)
        size = path.stat().st_size if path.exists() else 0
        print(f"  {name}: {count} entries, {size} bytes")


def trim_log():
    """保留 operation_log.md 最近 MAX_LOG_ENTRIES 条记录。"""
    if not LOG_FILE.exists():
        print("  operation_log.md not found.")
        return False

    content = LOG_FILE.read_text(encoding="utf-8")
    entries = list(re.finditer(r'^### .+$', content, re.MULTILINE))

    if len(entries) <= MAX_LOG_ENTRIES:
        print(f"  Only {len(entries)} entries, no trimming needed.")
        return False

    # 保留 header（第一个 ### 之前的内容）+ 最后 MAX_LOG_ENTRIES 条
    header = content[: entries[0].start()]
    kept_start = entries[-MAX_LOG_ENTRIES].start()
    kept = content[kept_start:]

    LOG_FILE.write_text(header + kept, encoding="utf-8")
    print(f"  Trimmed from {len(entries)} to {MAX_LOG_ENTRIES} entries.")
    return True


def date_range():
    """获取 experience_stream 和 evolution_log 的日期范围。"""
    results = {}
    for name, path in [("experience_stream", STREAM_FILE),
                       ("evolution_log", EVOLUTION_FILE)]:
        if not path.exists():
            results[name] = None
            continue
        content = path.read_text(encoding="utf-8")
        # 匹配 ### [EXP-XXX] YYYY-MM-DD 或 ### YYYY-MM-DD 格式
        dates = re.findall(r'###\s+(?:\[EXP-?\d*\]\s+)?(\d{4}-\d{2}-\d{2})', content)
        if dates:
            results[name] = (dates[0], dates[-1])
        else:
            results[name] = None

    for name, dr in results.items():
        if dr:
            print(f"  {name}: {dr[0]} → {dr[1]}")
        else:
            print(f"  {name}: no dated entries found")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compact.py <status|trim-log|date-range>")
        print("")
        print("  status      查看三个文件的状态")
        print("  trim-log    保留 operation_log.md 最近100条")
        print("  date-range  获取经验文件的日期范围")
        sys.exit(1)

    command = sys.argv[1]
    cmds = {
        "status": status,
        "trim-log": trim_log,
        "date-range": date_range,
    }

    if command in cmds:
        cmds[command]()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
