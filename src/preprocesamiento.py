import os
import re

def cargar_documentos(carpeta):
    documentos = {}
    for filename in os.listdir(carpeta):
        if filename.endswith('.txt'): 
            with open(os.path.join(carpeta, filename), 'r', encoding='utf-8') as file:
                documentos[filename] = file.read()
    return documentos

def tokenizar(texto, n=2):
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    palabras = texto.split()
    return [tuple(palabras[i:i+n]) for i in range(len(palabras)-n+1)]