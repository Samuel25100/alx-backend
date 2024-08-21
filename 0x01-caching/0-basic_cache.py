#!/usr/bin/env python3
""""class: BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """have put and get method for caching"""

    def put(self, key, item):
        """puts cached data as key and items in cached_data"""
        if (key or item):
            self.cache_data[key] = item

    def get(self, key):
        """get data from cached_data using key"""
        if (key):
            return (self.cache_data.get(key))
