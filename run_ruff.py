#!/usr/bin/env python3

import json
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile


def get_staged_python_files():
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'], capture_output=True, text=True
    )
    return [f for f in result.stdout.strip().splitlines() if f.endswith('.py')]


def get_changed_lines(file_path):
    result = subprocess.run(['git', 'diff', '--cached', '-U0', file_path], capture_output=True, text=True)
    lines = []
    for line in result.stdout.splitlines():
        if line.startswith('@@'):
            parts = line.split(' ')
            added = parts[2]  # e.g., '+10,2' or '+5'
            start, _, count = added[1:].partition(',')
            start = int(start)
            count = int(count) if count else 1
            lines.extend(range(start, start + count))
    return set(lines)


def apply_fixes_to_changed_lines(file_path, changed_lines):
    # Create a backup
    original = Path(file_path).read_text()

    # Let Ruff fix the whole file into a temp file
    with NamedTemporaryFile('w+', delete=False) as temp:
        temp_path = temp.name
    shutil.copyfile(file_path, temp_path)
    subprocess.run(['ruff', 'check', '--fix', '--select', 'Q', temp_path], capture_output=True)

    original_lines = original.splitlines()
    fixed_lines = Path(temp_path).read_text().splitlines()

    # Apply only the fixed lines that are within changed lines
    new_lines = []
    for i, (orig, fixed) in enumerate(zip(original_lines, fixed_lines), start=1):
        if i in changed_lines and orig != fixed:
            new_lines.append(fixed)
        else:
            new_lines.append(orig)

    Path(file_path).write_text('\n'.join(new_lines) + '\n')
    subprocess.run(['git', 'add', file_path])


def main():
    staged_files = get_staged_python_files()

    if not staged_files:
        sys.exit(0)

    for file in staged_files:
        changed_lines = get_changed_lines(file)
        if not changed_lines:
            continue

        apply_fixes_to_changed_lines(file, changed_lines)

    print('✅ Ruff autofix applied to changed lines only.')
    sys.exit(0)


if __name__ == '__main__':
    main()
