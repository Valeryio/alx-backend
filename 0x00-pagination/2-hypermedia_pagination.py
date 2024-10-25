#!/usr/bin/env python3

"""This module contains a simple helper function for
pagination
"""
import csv
import math
from typing import List, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get a page
        param: page
        param: page_size
        return: List
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        r_index = index_range(page, page_size)
        self.dataset()
        result = []
        if r_index[0] > len(self.__dataset):
            return result
        for i in range(r_index[0], r_index[-1]):
            result.append(self.__dataset[i])
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page
        param: page
        param: page_size
        return: List
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        r_index = index_range(page, page_size)
        result_dict = {}
        data = self.get_page(page, page_size)
        total_pages = round(len(self.__dataset) / page_size)
        next_page = page + 1 if (page + 1) < total_pages else None
        prev_page = page - 1 if (page - 1) > 0 else None

        result_dict["page"] = page
        result_dict["page_size"] = page_size if page < total_pages else 0
        result_dict["data"] = data
        result_dict["total_pages"] = total_pages
        result_dict["next_page"] = next_page
        result_dict["prev_page"] = prev_page

        return result_dict
