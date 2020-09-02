#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="pre-push-hooks",
    description="Pre-push hooks to apply rules before a code push to github.",
    url="https://github.com/surafelabebe/pre-push-hooks",
    version="1.0.0",
    author="Surafel Worku",
    author_email="surafel@clumio.com",
    packages=["pre_push_hooks"],
    install_requires=["ruamel.yaml>=0.15"],
    entry_points={
        "console_scripts": [
            "check-branch-for-push = pre_push_hooks.check_branch_for_push:main",
        ]
    },
)
