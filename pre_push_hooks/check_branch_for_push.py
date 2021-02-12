#
# Copyright 2021. Clumio, Inc.
#
# Follow the Google style guide, but with COLUMN_LIMIT=100.
# https://github.com/google/styleguide/blob/gh-pages/pyguide.md
# Indent is 4 spaces, no tabs.

"""pre-push hook to limit pushes to specific branches."""
import argparse
import os
import re
import sys
from typing import AbstractSet, Optional, Sequence


def is_push_to_branch_allowed(
        patterns: AbstractSet[str] = frozenset(),
) -> bool:
    """Checks if the remote branch is in the list of allowed patterns"""
    ref = os.environ['PRE_COMMIT_REMOTE_BRANCH']
    if not ref:
        sys.exit(0)
    remote_ref = '/'.join(ref.strip().split('/')[2:])
    return not any(
        re.match(p, remote_ref) for p in patterns
    )

def main(argv: Optional[Sequence[str]] = None) -> int:
    """Reads the patterns from .pre-commit-config.yaml and 
    checks if the remote branch matches the pattern.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--pattern', action='append',
        help=(
            'regex patterns of branch names to match'
        ),
    )
    args = parser.parse_args(argv)

    patterns = frozenset(args.pattern or ())
    return int(is_push_to_branch_allowed(patterns))


if __name__ == '__main__':
    sys.exit(main())
