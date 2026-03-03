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
            # truncated_dataset = dataset[:1000]  # kept for compatibility
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of data resilient to deletions.

        The method returns a dictionary with the following keys:
            - index: the current start index of the return page (requested index)
            - next_index: the next index to query (first index after the last item on the current page)
            - page_size: the actual number of items in the current page
            - data: the list of rows for the current page

        Args:
            index (int, optional): The start index for the page (0‑based). Defaults to 0.
            page_size (int, optional): The number of items requested. Defaults to 10.

        Returns:
            Dict: A dictionary containing the pagination information.

        Raises:
            AssertionError: If index is not a valid integer within the dataset range,
                            or if page_size is not a positive integer.
        """
        # Ensure the indexed dataset is built
        indexed_data = self.indexed_dataset()
        # Determine the maximum valid index
        max_index = max(indexed_data.keys())

        # Set default index to 0 if None
        if index is None:
            index = 0

        # Validate arguments
        assert isinstance(index, int) and index >= 0 and index <= max_index, \
            "index must be a non‑negative integer within the dataset range"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data = []
        current = index

        # Collect page_size items, skipping missing indices
        while len(data) < page_size and current <= max_index:
            if current in indexed_data:
                data.append(indexed_data[current])
            current += 1

        # The next index to query is the first index after the last considered item
        next_index = current

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
