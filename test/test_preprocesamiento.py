import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import tempfile
from src.preprocesamiento import cargar_documentos, tokenizar

class TestPreprocesamiento:
    @classmethod
    def setup_class(cls):
        # Create temporary test files
        cls.temp_dir = tempfile.mkdtemp()
        cls.txt_file1 = os.path.join(cls.temp_dir, "doc1.txt")
        cls.txt_file2 = os.path.join(cls.temp_dir, "doc2.txt")
        cls.non_txt_file = os.path.join(cls.temp_dir, "ignore.pdf")
        
        with open(cls.txt_file1, 'w', encoding='utf-8') as f:
            f.write("Este es un documento de prueba.")
        
        with open(cls.txt_file2, 'w', encoding='utf-8') as f:
            f.write("Otro documento con diferentes palabras.")
            
        with open(cls.non_txt_file, 'w', encoding='utf-8') as f:
            f.write("Este no debería cargarse.")

    def test_cargar_documentos(self):
        docs = cargar_documentos(self.temp_dir)
        assert len(docs) == 2
        assert "doc1.txt" in docs
        assert "doc2.txt" in docs
        assert "ignore.pdf" not in docs

    def test_tokenizar_bigrams(self):
        text = "Hola mundo! ¿Cómo estás?"
        tokens = tokenizar(text)
        expected = [('hola', 'mundo'), ('mundo', 'cómo'), ('cómo', 'estás')]
        assert tokens == expected

    def test_tokenizar_trigrams(self):
        text = "Esto es una prueba"
        tokens = tokenizar(text, n=3)
        expected = [('esto', 'es', 'una'), ('es', 'una', 'prueba')]
        assert tokens == expected

    def test_tokenizar_empty(self):
        assert tokenizar("") == []
        assert tokenizar("   ") == []
        assert tokenizar("palabra") == []

    @classmethod
    def teardown_class(cls):
        # Clean up temporary files
        for f in [cls.txt_file1, cls.txt_file2, cls.non_txt_file]:
            try:
                os.remove(f)
            except:
                pass
        os.rmdir(cls.temp_dir)