#!/usr/bin/env python3
"""Module for task 8: Complex types - functions.
Contains a type-annotated function that returns a function to multiply
a float by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
