import csv
import math
from typing import List, Tuple


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
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        result: List[List[str]] = self.dataset()
        index = index_range(page, page_size)
        length = len(result)
        if (index[0] > length or index[1] > length):
            return []
        return result[index[0]:index[1]]
