#!/usr/bin/python3
"""class: FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """store cache data in FIFO policy"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.fifo = []

    def put(self, key, item):
        """put method for FIFO caching"""
        if (key or item):
            self.cache_data[key] = item
            if (key not in self.fifo):
                self.fifo.append(key)
            if (len(self.fifo) == (BaseCaching.MAX_ITEMS) + 1):
                old = self.fifo.pop(0)
                del self.cache_data[old]
                print("DISCARD:", old)

    def get(self, key):
        """get method for FIFO caching"""
        if (key):
            return self.cache_data.get(key)
        return None
