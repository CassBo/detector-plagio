import csv
import os
from datetime import datetime

def exportar_similitudes_a_csv(similitudes, carpeta='resultados/csv'):
    os.makedirs(carpeta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{carpeta}/similitudes_{timestamp}.csv"

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Documento 1', 'Documento 2', 'Similitud (%)'])

        for doc1, doc2, sim in similitudes:
            writer.writerow([doc1, doc2, f"{sim:.2f}"])

    print(f"[✔] Similitudes exportadas a: {nombre_archivo}")
