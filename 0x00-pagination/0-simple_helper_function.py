#!/usr/bin/env python3

"""This module contains a simple helper function for
pagination
"""


def index_range(page: int, page_size: int):
    """THis function is a simple helper
    param: page
    param: page_size
    return: A tuple
    """

    end_index = page_size * page
    start_index = (page - 1) * page_size

    result = (start_index, end_index)
    return result
