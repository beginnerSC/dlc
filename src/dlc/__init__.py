"""
dlc - Dynamic Leetcode C++ algorithms

A Python package with C++ extensions for various algorithms and data structures.
"""

try:
    from .dlc_core import *
except ImportError as e:
    import warnings
    warnings.warn(
        f"Failed to import C++ extension module 'dlc_core': {e}. "
        "You may need to build the package first with 'poetry build'.",
        ImportWarning
    )