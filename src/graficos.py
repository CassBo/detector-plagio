import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def generar_graficos(similitudes):
    # Extraer los nombres de los documentos y los niveles de similitud
    documentos = [f"{doc1} - {doc2}" for doc1, doc2, _ in similitudes]
    scores = [sim * 100 for _, _, sim in similitudes]  # Convertir a porcentaje

    # Definir una lista de colores para cada barra
    colores = ['skyblue', 'lightgreen', 'salmon', 'gold', 'lightcoral', 'lightpink', 'lightyellow', 'lightblue']

    # Configuración del gráfico
    plt.figure(figsize=(10, 6))

    # Creación del gráfico de barras horizontales con colores personalizados
    plt.barh(documentos, scores, color=colores[:len(documentos)])  # Asegúrate de que haya suficientes colores

    # Etiquetas y título
    plt.xlabel('Nivel de Similitud (%)')
    plt.title('Niveles de Similitud entre Documentos')

    # Limitar el eje x de 0 a 100%
    plt.xlim(0, 100)

    # Añadir etiquetas de porcentaje en las barras
    for i, score in enumerate(scores):
        plt.text(score + 2, i, f'{score:.1f}%', va='center')

    # Crear el directorio para guardar gráficos si no existe
    os.makedirs('resultados/graficos', exist_ok=True)

    # Generar un nombre de archivo único basado en la fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'resultados/graficos/similitudes_{timestamp}.png'

    # Guardar el gráfico
    plt.tight_layout()  # Ajustar el diseño para que no se solapen elementos
    plt.savefig(filename)
    plt.show()