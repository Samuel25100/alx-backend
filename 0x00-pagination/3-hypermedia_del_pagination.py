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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary of index, next-index, page_size, data"""
        result = {}
        indexed_data = self.indexed_dataset()
        length = len(indexed_data)
        if (index is not None):
            assert length > index
        result['index'] = index
        data = []
        if index is None:
            i = 0
        else:
            i = index
        next_index = index + page_size
        while (i < next_index):
            if (indexed_data.get(i) is not None):
                data.append(indexed_data[i])
            else:
                next_index += 1
            i += 1
        result['data'] = data
        result['page_size'] = page_size
        result['next_index'] = next_index
        return result
