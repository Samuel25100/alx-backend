#!/usr/bin/env python3
"""class: Server"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """return start and end index based on what page and size of total page"""
    start: int = ((page - 1) * page_size)
    end: int = start + page_size
    return tuple([start, end])


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return list of list from dataset based on start and end"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        result: List[List[str]] = self.dataset()
        index = index_range(page, page_size)
        length = len(result)
        if (index[0] > length or index[1] > length):
            return []
        return result[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary"""
        result = {}
        result['page_size'] = page_size
        result['page'] = page
        start, end = index_range(page, page_size)
        result['data'] = self.get_page(page, page_size)
        total_items: int = len(self.__dataset)
        total_pages = (total_items + page_size - 1) // page_size
        result['next_page'] = page + 1 if page < total_pages else None
        result['prev_page'] = page - 1 if page > 1 else None
        result['total_pages'] = total_pages
        return result
