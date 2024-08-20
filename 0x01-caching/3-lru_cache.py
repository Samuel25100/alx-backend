#!/usr/bin/python3
"""class: LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """store cache data in LRU policy"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """put method for LRU caching"""
        if (key or item):
            self.cache_data[key] = item
            if (key not in self.lru):
                self.lru.append(key)
            else:
                index = self.lru.index(key)
                self.lru.pop(index)
                self.lru.append(key)
            if (len(self.cache_data) == (BaseCaching.MAX_ITEMS + 1)):
                old = self.lru.pop(0)
                del self.cache_data[old]
                print("DISCARD:", old)

    def get(self, key):
        """get method for LRU caching"""
        if (key):
            val = self.cache_data.get(key)
            if (val):
                index = self.lru.index(key)
                self.lru.pop(index)
                self.lru.append(key)
                return val
        return None
