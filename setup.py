#!/usr/bin/env python3

'''Setup script'''

from setuptools import setup

setup(
    name="hangman",
    version="1.0",
    author="Nikita Podlozhnyy",
    author_email="podlozhnyy.ne@phystech.edu",
    url="https://github.com/NPodlozhniy/HangMan",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
        "tests",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
