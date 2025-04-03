from src.preprocesamiento import cargar_documentos, tokenizar
from src.hash_table import HashTable
from src.bloom_filter import BloomFilter
from src.similitud import calcular_similitud
from src.sorting import merge_sort
from src.graficos import generar_graficos

def main():
    # Paso 1: Cargar los Documentos
    documentos = cargar_documentos('documentos/')
    
    # Paso 2: Preprocesamiento del Texto
    n_gramas = {doc: tokenizar(texto) for doc, texto in documentos.items()}
    
    # Paso 3: Crear una Tabla Hash y Filtro de Bloom
    hash_tables = {doc: HashTable() for doc in n_gramas}
    bloom_filters = {doc: BloomFilter() for doc in n_gramas}
    
    for doc, n_gram in n_gramas.items():
        for n in n_gram:
            hash_tables[doc].insert(n)
            bloom_filters[doc].add(n)
    
        # Paso 4: Comparar Documentos y Calcular Similitud
    similitudes = []
    compared_pairs = set()  # Initialize the set to track compared pairs
    documentos_list = list(n_gramas.keys())  # Convert the keys to a list for indexing

    for i in range(len(documentos_list)):
        for j in range(i + 1, len(documentos_list)):  # Start from i + 1 to avoid redundancy
            doc1 = documentos_list[i]
            doc2 = documentos_list[j]
            sim = calcular_similitud(hash_tables[doc1], hash_tables[doc2], compared_pairs)
            if sim is not None:
                similitudes.append((doc1, doc2, sim))

    # Paso 5: Ordenar los Resultados
    similitudes_ordenadas = merge_sort(similitudes, key=lambda x: x[2], reverse=True)
    
    # Paso 6: Mostrar los N Documentos Más Similares
    N = 5  # Cambia este valor según sea necesario
    for doc1, doc2, sim in similitudes_ordenadas[:N]:
        print(f"Similitud entre {doc1} y {doc2}: {sim:.2f}")
    
    # Generar gráficos
    generar_graficos(similitudes_ordenadas)

if __name__ == "__main__":
    main()