import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.hash_table import HashTable

class TestHashTable:
    def test_initialization(self):
        ht = HashTable()
        assert len(ht.table) == 0

    def test_insert_new_gram(self):
        ht = HashTable()
        test_gram = "new ngram"
        ht.insert(test_gram)
        assert ht.get(test_gram) == 1
        assert test_gram in ht.keys()

    def test_insert_duplicate_gram(self):
        ht = HashTable()
        test_gram = "duplicate gram"
        
        # First insert
        ht.insert(test_gram)
        assert ht.get(test_gram) == 1
        
        # Second insert
        ht.insert(test_gram)
        assert ht.get(test_gram) == 2

    def test_get_non_existent_gram(self):
        ht = HashTable()
        assert ht.get("missing") == 0

    def test_keys_method(self):
        ht = HashTable()
        grams = ["gram1", "gram2", "gram3"]
        
        for gram in grams:
            ht.insert(gram)
            
        keys = ht.keys()
        assert len(keys) == 3
        for gram in grams:
            assert gram in keys