#!/usr/bin/env python3
"""Bump version tag in all HTML files."""
import glob, re

for f in glob.glob('/Users/coady/WorkBuddy/Claw/novora-site/articles/*.html'):
    with open(f) as fh:
        c = fh.read()
    c = c.replace('content="20260609v25"', 'content="20260609v26"')
    with open(f, 'w') as fh:
        fh.write(c)
    print(f'Bumped: {f}')

# Also bump index.html
idx = '/Users/coady/WorkBuddy/Claw/novora-site/index.html'
with open(idx) as fh:
    c = fh.read()
c = c.replace('content="20260609v25"', 'content="20260609v26"')
with open(idx, 'w') as fh:
    fh.write(c)
print(f'Bumped: index.html')
print('Done!')
