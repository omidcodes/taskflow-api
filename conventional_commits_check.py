#!/usr/bin/env python3
import argparse
import re
import string
import sys


RED = "\033[31m"

COMMIT_TYPES = {
    'feat': r'^feat(\(.+\))?:',
    'fix': r'^fix(\(.+\))?:',
    'docs': r'^docs(\(.+\))?:',
    'style': r'^style(\(.+\))?:',
    'refactor': r'^refactor(\(.+\))?:',
    'perf': r'^perf(\(.+\))?:',
    'test': r'^test(\(.+\))?:',
    'build': r'^build(\(.+\))?:',
    'ci': r'^ci(\(.+\))?:',
    'chore': r'^chore(\(.+\))?:',
    'revert': '^revert: ',
}

EMOJIS = {
    'feat': '✨',
    'fix': '🐛',
    'docs': '📚',
    'style': '💅',
    'refactor': '🧹',
    'perf': '🚀',
    'test': '🧪',
    'build': '🏗️',
    'ci': '👷',
    'chore': '♻️',
    'revert': '⏪',
    'merge': '🔀',
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('commit_message_file')
    args = parser.parse_args()

    with open(args.commit_message_file) as file:
        commit_message = file.read()

    commit_message = commit_message.strip(string.whitespace + ''.join(EMOJIS.values()))

    commit_type = None
    for commit, pattern in COMMIT_TYPES.items():
        if re.match(pattern, commit_message):
            commit_type = commit
            break

    if not commit_type:
        print(
            f'{RED}Commit message does not follow Conventional Commits rules.\n' \
            f'It must begin with : {", ".join(COMMIT_TYPES.keys())}'
        )
        sys.exit(1)

    emoji = EMOJIS.get(commit_type)

    if emoji:
        new_commit_message = f'{emoji} {commit_message}'
        with open(args.commit_message_file, 'w') as file:
            file.write(new_commit_message)

    print('Commit message follows Conventional Commits rules and has been updated with an emoji.')
    sys.exit(0)


if __name__ == '__main__':
    main()
