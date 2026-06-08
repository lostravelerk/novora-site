#!/usr/bin/env python3
"""同步 QQ 邮箱订阅者到 subscribers.json，并推送到 GitHub。
用法: python3 sync_subscribers.py /path/to/new_subscribers.json
new_subscribers.json 格式: [{"name":"张三","email":"xx@xx","message":"hi"}]
"""
import json, sys, os, subprocess
from datetime import date, datetime

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(SITE_DIR, "subscribers.json")
TODAY = date.today().isoformat()

def load_existing():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH) as f:
            data = json.load(f)
    else:
        data = {"subscribers": []}
    return data

def save(data):
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def git_commit_push(msg):
    subprocess.run(["git", "add", "subscribers.json"], cwd=SITE_DIR, check=True)
    subprocess.run(["git", "commit", "-m", msg], cwd=SITE_DIR, check=False)
    subprocess.run(["git", "push", "origin", "main"], cwd=SITE_DIR, check=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: sync_subscribers.py <new_subscribers.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        new_list = json.load(f)

    existing = load_existing()
    emails = {s["email"].strip().lower() for s in existing["subscribers"]}
    added = 0

    for entry in new_list:
        email = entry.get("email", "").strip().lower()
        if not email:
            continue
        if email in emails:
            continue  # skip duplicates
        existing["subscribers"].append({
            "name": entry.get("name", "").strip(),
            "email": email,
            "message": entry.get("message", "").strip(),
            "subscribed": TODAY
        })
        emails.add(email)
        added += 1

    save(existing)
    print(f"同步完成: {added} 新增, 总计 {len(existing['subscribers'])} 人")

    if added > 0:
        git_commit_push(f"订阅者同步: +{added}人 ({TODAY})")

if __name__ == "__main__":
    main()
