#!/usr/bin/env python3
"""Basics caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Reps an object that allows storing and
    recover items from a dictionary.
    """
    def put(self, key, item):
        """inserts an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Recovers an item by key.
        """
        return self.cache_data.get(key, None)
