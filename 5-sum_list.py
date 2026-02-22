#!/usr/bin/env python3
"""Module for task 5: Complex types - list of floats.
Contains a type-annotated function that sums a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in the input list."""
    return sum(input_list)
