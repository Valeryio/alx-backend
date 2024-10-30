#!/usr/bin/env python3

"""This is a module that contains a lifo class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assign value to the internal
        caching directory
        param: key
        param: item
        """

        if key is not None and item is not None:

            try:
                value = self.cache_data[key]
                self.cache_data.pop(key)
            except KeyError:
                pass

            self.cache_data[key] = item
            last_item = 0

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for key, value in self.cache_data.items():
                    last_item += 1
                    if last_item == len(self.cache_data) - 1:
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
