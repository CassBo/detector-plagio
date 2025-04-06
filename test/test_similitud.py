import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.similitud import calcular_similitud
from src.hash_table import HashTable

class TestSimilitud:
    def test_identical_documents(self):
        ht1 = HashTable()
        ht2 = HashTable()
        compared = set()
        
        # Add same n-grams to both tables
        for gram in ["a b", "b c", "c d"]:
            ht1.insert(gram)
            ht2.insert(gram)
            
        similarity = calcular_similitud(ht1, ht2, compared)
        assert similarity == 1.0

    def test_different_documents(self):
        ht1 = HashTable()
        ht2 = HashTable()
        compared = set()
        
        ht1.insert("a b")
        ht1.insert("b c")
        ht2.insert("x y")
        ht2.insert("y z")
            
        similarity = calcular_similitud(ht1, ht2, compared)
        assert similarity == 0.0

    def test_partial_similarity(self):
        ht1 = HashTable()
        ht2 = HashTable()
        compared = set()
        
        # Shared n-grams
        ht1.insert("a b")
        ht1.insert("b c")
        ht2.insert("a b")
        ht2.insert("x y")
            
        similarity = calcular_similitud(ht1, ht2, compared)
        assert similarity == pytest.approx(1/3)

    def test_duplicate_pair_detection(self):
        ht1 = HashTable()
        ht2 = HashTable()
        compared = set()
        
        # First comparison should work
        assert calcular_similitud(ht1, ht2, compared) is not None
        
        # Second comparison should return None
        assert calcular_similitud(ht1, ht2, compared) is None

    def test_empty_documents(self):
        ht1 = HashTable()
        ht2 = HashTable()
        compared = set()
        
        # Both empty
        assert calcular_similitud(ht1, ht2, compared) == 0
        
        # One empty
        ht1.insert("a b")
        assert calcular_similitud(ht1, ht2, compared) == 0
        assert calcular_similitud(ht2, ht1, compared) == 0