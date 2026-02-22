#!/usr/bin/env python3
"""Module for task 7: Complex types - string and int/float to tuple.
Contains a type-annotated function that returns a tuple with a string
and the square of an int or float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is the string k and the
    second is the square of v (as a float).
    """
    return (k, float(v ** 2))
