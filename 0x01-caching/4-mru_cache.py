#!/usr/bin/python3
"""class: MRUCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """store cache data in MRU policy"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """put method for MRU caching"""
        if (key or item):
            if (len(self.cache_data) == (BaseCaching.MAX_ITEMS)):
                if (key not in self.mru):
                    old = self.mru.pop(-1)
                    del self.cache_data[old]
                    print("DISCARD:", old)
            self.cache_data[key] = item
            if (key not in self.mru):
                self.mru.append(key)
            else:
                index = self.mru.index(key)
                self.mru.pop(index)
                self.mru.append(key)

    def get(self, key):
        """get method for LRU caching"""
        if (key):
            val = self.cache_data.get(key)
            if (val):
                index = self.mru.index(key)
                self.mru.pop(index)
                self.mru.append(key)
                return val
        return None
