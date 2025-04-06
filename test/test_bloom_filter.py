import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.bloom_filter import BloomFilter

class TestBloomFilter:
    def test_initialization_default_size(self):
        bf = BloomFilter()
        assert len(bf.bit_array) == 1000
        assert sum(bf.bit_array) == 0

    def test_initialization_custom_size(self):
        bf = BloomFilter(size=500)
        assert len(bf.bit_array) == 500
        assert sum(bf.bit_array) == 0

    def test_add_and_check(self):
        bf = BloomFilter()
        test_gram = "test ngram"
        
        # Should not exist before adding
        assert not bf.check(test_gram)
        
        # Add and verify exists
        bf.add(test_gram)
        assert bf.check(test_gram)

    def test_hash_consistency(self):
        bf = BloomFilter()
        test_gram = "consistent hash"
        hash1 = bf._hash(test_gram)
        hash2 = bf._hash(test_gram)
        assert hash1 == hash2

    def test_false_positives(self):
        bf = BloomFilter(size=10)  # Small size to increase collision chance
        gram1 = "gram one"
        gram2 = "gram two"
        
        bf.add(gram1)
        # There's a chance this could be a false positive
        assert bf.check(gram1)
        
        # This might be a false positive due to small size
        print(f"False positive check for gram2: {bf.check(gram2)}")