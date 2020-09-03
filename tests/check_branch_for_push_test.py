#
# Copyright 2019. Clumio, Inc.
#
# Follow the Google style guide, but with COLUMN_LIMIT=100.
# https://github.com/google/styleguide/blob/gh-pages/pyguide.md
# Indent is 4 spaces, no tabs.
# yapf --style='$GOPATH/src/cdf/yapf.yaml'

import unittest
import os
from pre_push_hooks import check_branch_for_push


class TestSquare(unittest.TestCase):

    def is_not_on_branch(self):
        return check_branch_for_push.is_not_on_branch({'^user/.*'})

    def test_master_branch(self):
        os.environ['PRE_COMMIT_REMOTE_REF'] = 'refs/heads/master'
        self.assertEqual(self.is_not_on_branch(), True)

    def test_user_branch(self):
        os.environ['PRE_COMMIT_REMOTE_REF'] = 'refs/heads/user/one'
        self.assertEqual(self.is_not_on_branch(), False)

    def test_empty_branch(self):
        os.environ['PRE_COMMIT_REMOTE_REF'] = ''
        with self.assertRaises(SystemExit) as cm:
            self.is_not_on_branch()
        self.assertEqual(cm.exception.code, 0)