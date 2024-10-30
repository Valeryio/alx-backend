#!/usr/bin/env python3

"""This is a module about a simple basic cache
class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This is the basic cache class of the first tasks to
    get basic caching operations

    Attributes:
        cache_data: dict
    """

    def put(self, key, item):
        """
        This method allow the class to set new item
        to the cache attribute
        param: key
        param: item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
