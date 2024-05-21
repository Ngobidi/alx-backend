#!/usr/bin/env python3
"""BaseCaching approach.
"""


class BaseCaching():
    """Base_Caching define:
      - constant of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """set-up the cache.
        """
        self.cache_data = {}

    def print_cache(self):
        """display the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """insert an item in the cache.
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """Recover an item by key.
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
