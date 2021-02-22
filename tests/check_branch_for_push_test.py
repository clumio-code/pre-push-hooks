#
# Copyright 2020. Clumio, Inc.
#
"""Test for check_branch_for_push.py"""
import unittest
import os

from pre_push_hooks import check_branch_for_push


class TestPrePushHook(unittest.TestCase):
    """Defines testcases for the pre-push-hook"""

    def test_branch(self):
        """parameterized test with different branch patterns and remote references"""
        input_patterns = ['--pattern', '^user/.*', '--pattern', '^team/.*']
        test_cases = [
            (input_patterns, 'refs/heads/master', 1),
            (input_patterns, 'refs/heads/user/one', 0),
            (input_patterns, '', 0),
            ([], 'refs/heads/master', 1),
            ([], 'refs/heads/user/one', 1),
            ([], '', 0),
        ]
        for patterns, remote_ref, expected_result in test_cases:
            with self.subTest(f'{patterns}, {remote_ref} -> {expected_result}'):
                os.environ['PRE_COMMIT_REMOTE_BRANCH'] = remote_ref
                print(patterns, remote_ref)
                if remote_ref:
                    self.assertEqual(check_branch_for_push.main(patterns), expected_result)
                else:
                    with self.assertRaises(SystemExit) as cm:
                        check_branch_for_push.main(patterns)
                    self.assertEqual(cm.exception.code, expected_result)