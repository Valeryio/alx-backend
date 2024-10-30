#!/usr/bin/env python3

"""This is a module that contains a mru class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    This is the LFU class, that handle basic
    LFU cache operations
    """
    def __init__(self):
        super().__init__()
        self.freq_cache = {}

    def put(self, key, item):
        """Assign value to the internal
        caching directory
        param: key
        param: item
        """

        if key is not None and item is not None:

            try:
                # If the key is found the count is incremented
                value = self.cache_data[key]
                self.cache_data[key] = item
                self.freq_cache[key] += 1
            except KeyError:
                # if the key is not found, the count is set to 1
                self.cache_data[key] = item
                self.freq_cache[key] = 1

                if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                    # find the minimum freq in the values
                    min_freq = min([x for x in self.freq_cache.values()])
                    key_to_delete = ''

                    # find the first key (least used), with the min freq
                    for key, value in self.freq_cache.items():
                        if value == min_freq:
                            key_to_delete = key
                            break

                    print(f"DISCARD: {key_to_delete}")
                    self.cache_data.pop(key_to_delete)
                    self.freq_cache.pop(key_to_delete)

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

            # if the key is used, its count is incremented
            self.freq_cache[key] += 1
            return value
        except KeyError:
            return None