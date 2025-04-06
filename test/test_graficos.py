import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import shutil
from unittest.mock import patch, MagicMock
from src.graficos import generar_graficos

class TestGraficos:
    @classmethod
    def setup_class(cls):
        # Clear any existing test results
        if os.path.exists('resultados'):
            shutil.rmtree('resultados')

    def test_empty_input(self):
        with patch('matplotlib.pyplot.show'):
            # Should not raise errors with empty input
            generar_graficos([])
            
        # No files should be created
        assert not os.path.exists('resultados/graficos')

    def test_single_document(self):
        test_data = [("doc1.txt", "doc2.txt", 0.75)]
        
        with patch('matplotlib.pyplot.show'):
            with patch('matplotlib.pyplot.savefig') as mock_save:
                generar_graficos(test_data)
                
                # Verify save was called
                assert mock_save.called
                filename = mock_save.call_args[0][0]
                assert filename.startswith('resultados/graficos/similitudes_')
                assert filename.endswith('.png')

    def test_multiple_documents(self):
        test_data = [
            ("doc1.txt", "doc2.txt", 0.25),
            ("doc1.txt", "doc3.txt", 0.50),
            ("doc2.txt", "doc3.txt", 0.75)
        ]
        
        with patch('matplotlib.pyplot.show'):
            with patch('matplotlib.pyplot.barh') as mock_barh:
                generar_graficos(test_data)
                
                # Verify correct number of bars
                args, kwargs = mock_barh.call_args
                assert len(args[0]) == 3  # 3 document pairs
                assert len(args[1]) == 3  # 3 similarity scores

    def test_directory_creation(self):
        test_data = [("doc1.txt", "doc2.txt", 0.5)]
        
        with patch('matplotlib.pyplot.show'):
            generar_graficos(test_data)
            
        # Verify directory was created
        assert os.path.exists('resultados/graficos')

    @classmethod
    def teardown_class(cls):
        # Clean up
        if os.path.exists('resultados'):
            shutil.rmtree('resultados')