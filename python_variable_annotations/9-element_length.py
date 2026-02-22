#!/usr/bin/env python3
"""Module for task 9: Let's duck type an iterable object.
Contains an annotated function that returns a list of tuples containing
elements and their lengths.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing an element from the iterable
    and its length.
    """
    return [(i, len(i)) for i in lst]
