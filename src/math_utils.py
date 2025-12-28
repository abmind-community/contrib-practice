"""A small module containing intentionally poorly formatted code.

This file contains several Python functions with style problems such as
missing whitespace, inconsistent indentation and unused imports. Use this
file to practise fixing style issues using Ruff and pre-commit. Do not
change the behaviour of the functions; focus only on formatting and style.
"""

import sys  # noqa: F401  # unused imports for demonstration purposes


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
