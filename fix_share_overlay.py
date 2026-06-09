#!/usr/bin/env python3
"""Remove leftover .share-guide CSS rules from all article files."""
import os
import re
import glob

BASE = "/Users/coady/WorkBuddy/Claw/novora-site"

def clean_css(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove .share-guide CSS block (one line at a time)
    content = re.sub(r'\n  \.share-guide[^\n]+\n', '\n', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned: {os.path.basename(path)}")

def main():
    files = glob.glob(os.path.join(BASE, "articles/*.html"))
    files.sort()
    for f in files:
        clean_css(f)
    print("Done!")

if __name__ == "__main__":
    main()
