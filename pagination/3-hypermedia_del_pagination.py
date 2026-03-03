#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of data resilient to deletions.

        Args:
            index (int, optional): Start index (0‑based). Defaults to 0.
            page_size (int): Number of items requested. Defaults to 10.

        Returns:
            Dict: {
                'index': requested start index,
                'data': list of rows,
                'page_size': actual number of rows returned,
                'next_index': index to use for the next query
            }
        """
        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys()) if indexed_data else -1

        # Handle default index
        if index is None:
            index = 0

        # Validate inputs
        assert isinstance(index, int) and index >= 0 and index <= max_index, \
            "index must be a non‑negative integer within the dataset range"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data = []
        current = index

        # Collect up to page_size items, skipping missing indices
        while len(data) < page_size and current <= max_index:
            if current in indexed_data:
                data.append(indexed_data[current])
            current += 1

        next_index = current

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
