#!/usr/bin/env python3

"""This is a module that contains a fifo class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This is the fifo class, inheriting from the basic clas
    that handle basic FIFO cache operations
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assign value to the internal
        caching directory
        param: key
        param: item
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for key, value in self.cache_data.items():
                    print(f"DISCARD {key}")
                    self.cache_data.pop(key)
                    break

    def get(self, key):
        """
        This method get the item of a specific key
        param: key
        return: A value
        """
        if key is None:
            return key
        try:
            value = self.cache_data[key]
            return value
        except KeyError:
            return None
