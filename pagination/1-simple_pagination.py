#!/usr/bin/env python3
"""
Simple pagination of a baby names dataset.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for a given pagination page.

    Args:
        page (int): Page number (1‑indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset (without header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]          # skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data.

        Args:
            page (int): Page number (1‑indexed). Defaults to 1.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            List[List]: The rows for the requested page, or an empty list if
                        the page is out of range.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end]
