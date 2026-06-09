#!/usr/bin/env python3
"""Fix duplicated closeShareOverlay in all article files."""
import glob

for f in glob.glob('/Users/coady/WorkBuddy/Claw/novora-site/articles/*.html'):
    with open(f) as fh:
        c = fh.read()

    # Fix duplicated closeShareOverlay with orphaned }
    old = '''function closeShareOverlay(){
  document.getElementById('share-overlay').classList.remove('show');
}
}
function closeShareOverlay(){
  document.getElementById('share-overlay').classList.remove('show');
}'''

    new = '''function closeShareOverlay(){
  document.getElementById('share-overlay').classList.remove('show');
}'''

    if old in c:
        c = c.replace(old, new)
        with open(f, 'w') as fh:
            fh.write(c)
        print(f'Fixed: {f}')
    else:
        print(f'OK: {f}')

print('Done!')
