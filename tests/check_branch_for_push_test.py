import unittest
import os
from pre_push_hooks import check_branch_for_push


class TestSquare(unittest.TestCase):

    def is_on_branch(self):
        return check_branch_for_push.is_on_branch({'^user/.*'})

    def test_master_branch(self):
        os.environ['PRE_COMMIT_REMOTE_REF'] = 'refs/heads/master'
        self.assertEqual(self.is_on_branch(), True)

    def test_user_branch(self):
        os.environ['PRE_COMMIT_REMOTE_REF'] = 'refs/heads/user/one'
        self.assertEqual(self.is_on_branch(), False)

    def test_empty_branch(self):
        os.environ['PRE_COMMIT_REMOTE_REF'] = ''
        with self.assertRaises(SystemExit) as cm:
            self.is_on_branch()
        self.assertEqual(cm.exception.code, 0)