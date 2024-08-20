#!/usr/bin/python3
"""class: LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """store cache data in LIFO policy"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.lifo = []

    def put(self, key, item):
        """put method for LIFO caching"""
        if (key or item):
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                if (key not in self.lifo):
                    old = self.lifo.pop(-1)
                    del self.cache_data[old]
                    print("DISCARD:", old)
            self.cache_data[key] = item
            if (key not in self.lifo):
                self.lifo.append(key)
            elif (key in self.lifo):
                index = self.lifo.index(key)
                self.lifo.pop(index)
                self.lifo.append(key)

    def get(self, key):
        """get method for FIFO caching"""
        if (key):
            return self.cache_data.get(key)
        return None
