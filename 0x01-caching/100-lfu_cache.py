#!/usr/bin/python3
"""class: LFUCache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """store cache data in LFU policy"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.lfu = {"key": [], "freq": []}

    def put(self, key, item):
        """put method for LFU caching"""
        if (key or item):
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                freq = min(self.lfu['freq'])
                index = self.lfu['freq'].index(freq)
                self.lfu['freq'].pop(index)
                old = self.lfu['key'].pop(index)
                del self.cache_data[old]
                print("DISCARD:", old)

            self.cache_data[key] = item
            if (key in self.lfu['key']):
                ind = self.lfu['key'].index(key)
                self.lfu['freq'][ind] += 1
            else:
                self.lfu['key'].append(key)
                self.lfu['freq'].append(0)

    def get(self, key):
        """get method for LFU caching"""
        if (key):
            val = self.cache_data.get(key)
            if (val):
                ind = self.lfu['key'].index(key)
                self.lfu['freq'][ind] += 1
            return val
        return None
