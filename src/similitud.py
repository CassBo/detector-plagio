def calcular_similitud(hash_table_a, hash_table_b, compared_pairs):
    doc_pair = (id(hash_table_a), id(hash_table_b))
    reverse_doc_pair = (id(hash_table_b), id(hash_table_a))

    if doc_pair in compared_pairs or reverse_doc_pair in compared_pairs:
        return None 

    compared_pairs.add(doc_pair)

    intersection = 0
    union = len(hash_table_a.keys()) + len(hash_table_b.keys())
    
    for key in hash_table_a.keys():
        if hash_table_b.get(key) > 0:
            intersection += 1
    
    union -= intersection
    return intersection / union if union > 0 else 0