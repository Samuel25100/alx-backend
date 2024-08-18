#!/usr/bin/env python3
"""function: index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """return start and end index based on what page and size of total page"""
    start: int = ((page - 1) * page_size)
    end: int = start + page_size
    return tuple([start, end])
