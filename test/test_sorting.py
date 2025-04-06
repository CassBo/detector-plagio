import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.sorting import merge_sort

class TestMergeSort:
    def test_sort_numbers_ascending(self):
        arr = [5, 2, 8, 1, 9]
        expected = [1, 2, 5, 8, 9]
        assert merge_sort(arr) == expected

    def test_sort_numbers_descending(self):
        arr = [5, 2, 8, 1, 9]
        expected = [9, 8, 5, 2, 1]
        assert merge_sort(arr, reverse=True) == expected

    def test_sort_strings(self):
        arr = ["banana", "apple", "cherry"]
        expected = ["apple", "banana", "cherry"]
        assert merge_sort(arr) == expected

    def test_custom_key(self):
        arr = [("a", 3), ("b", 1), ("c", 2)]
        expected = [("b", 1), ("c", 2), ("a", 3)]
        assert merge_sort(arr, key=lambda x: x[1]) == expected

    def test_empty_list(self):
        assert merge_sort([]) == []

    def test_single_element(self):
        assert merge_sort([42]) == [42]

    def test_duplicate_values(self):
        arr = [3, 1, 2, 1, 3]
        expected = [1, 1, 2, 3, 3]
        assert merge_sort(arr) == expected

    def test_sort_tuples(self):
        arr = [(1, 3), (2, 1), (1, 2)]
        expected = [(1, 2), (1, 3), (2, 1)]
        assert merge_sort(arr, key=lambda x: (x[0], x[1])) == expected