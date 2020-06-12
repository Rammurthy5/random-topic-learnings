"""
Demonstrating the purpose of context manager, and how to create one.

"""

import os
from contextlib import contextmanager


@contextmanager
def cd(dirname):
    original = os.getcwd()
    os.chdir(dirname)
    try:
        yield
    finally:
        os.chdir(original)


with cd('/Users/rammurthys'):
    print(os.getcwd())

print(os.getcwd())

