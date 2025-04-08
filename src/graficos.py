import matplotlib.pyplot as plt
import os
from datetime import datetime
import networkx as nx
import tkinter as tk
from tkinter import ttk

# Paleta de colores por rango
COLORES_POR_RANGO = {
    "0-9": "#FF9999",
    "10-19": "#FFCC99",
    "20-29": "#FFFF99",
    "30-39": "#CCFF99",
    "40-49": "#99FFCC",
    "50-59": "#99FFFF",
    "60-69": "#99CCFF",
    "70-79": "#9999FF",
    "80-89": "#CC99FF",
    "90-99": "#FF99CC"
}

def agrupar_similitudes(similitudes):
    rangos = {f"{i}-{i+9}": [] for i in range(0, 100, 10)}
    for doc1, doc2, sim in similitudes:
        porcentaje = sim * 100
        for rango in rangos.keys():
            inicio, fin = map(int, rango.split('-'))
            if inicio <= porcentaje < fin:
                rangos[rango].append((doc1, doc2, porcentaje))
                break
    return rangos

def mostrar_tabla(documentos):
    ventana = tk.Tk()
    ventana.title("Documentos Comparados")
    ventana.geometry("700x400")

    # Filtros
    frame_filtros = tk.Frame(ventana)
    frame_filtros.pack(fill="x", padx=10, pady=5)

    tk.Label(frame_filtros, text="Buscar documento:").pack(side="left")
    entrada_busqueda = tk.Entry(frame_filtros)
    entrada_busqueda.pack(side="left", padx=5)

    tk.Label(frame_filtros, text="Similitud mínima (%):").pack(side="left")
    entrada_similitud = tk.Entry(frame_filtros, width=5)
    entrada_similitud.insert(0, "0")
    entrada_similitud.pack(side="left", padx=5)

    # Tabla
    tabla = ttk.Treeview(ventana, columns=("doc1", "doc2", "sim"), show="headings")
    tabla.heading("doc1", text="Documento 1")
    tabla.heading("doc2", text="Documento 2")
    tabla.heading("sim", text="Similitud (%)")
    tabla.pack(expand=True, fill="both")

    def aplicar_filtro():
        filtro_doc = entrada_busqueda.get().lower()
        try:
            filtro_sim = float(entrada_similitud.get())
        except ValueError:
            filtro_sim = 0

        for row in tabla.get_children():
            tabla.delete(row)

        for doc1, doc2, sim in documentos:
            if filtro_doc in doc1.lower() or filtro_doc in doc2.lower():
                if sim >= filtro_sim:
                    tabla.insert("", "end", values=(doc1, doc2, f"{sim:.2f}"))

    boton_filtrar = tk.Button(frame_filtros, text="Filtrar", command=aplicar_filtro)
    boton_filtrar.pack(side="left", padx=10)

    aplicar_filtro()
    ventana.mainloop()

def seleccionar_rangos_disponibles(rangos_disponibles):
    seleccionados = []

    def aceptar():
        for i, var in enumerate(vars_rangos):
            if var.get():
                seleccionados.append(rangos_disponibles[i])
        root.destroy()

    root = tk.Tk()
    root.title("Seleccionar rangos de similitud")
    vars_rangos = []
    for rango in rangos_disponibles:
        var = tk.BooleanVar(value=True)
        chk = tk.Checkbutton(root, text=rango, variable=var)
        chk.pack(anchor='w')
        vars_rangos.append(var)

    tk.Button(root, text="Mostrar grafo", command=aceptar).pack(pady=10)
    root.mainloop()
    return seleccionados

def generar_grafo(similitudes):
    rangos = agrupar_similitudes(similitudes)

    # Filtro previo
    rangos_disponibles = [r for r, docs in rangos.items() if docs]
    if not rangos_disponibles:
        print("No hay documentos suficientes para graficar.")
        return

    rangos_seleccionados = seleccionar_rangos_disponibles(rangos_disponibles)

    G = nx.Graph()

    for rango in rangos_seleccionados:
        docs = rangos[rango]
        if not docs:
            continue
        G.add_node(rango, size=len(docs), docs=docs)

    pos = nx.spring_layout(G, seed=42)
    sizes = [G.nodes[n]['size'] * 100 for n in G.nodes]
    colors = [COLORES_POR_RANGO.get(n, '#cccccc') for n in G.nodes]

    fig, ax = plt.subplots(figsize=(10, 8))
    nodes = nx.draw_networkx_nodes(G, pos, ax=ax, node_size=sizes, node_color=colors, alpha=0.8)
    labels = nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold')

    # Interactividad de clic
    def on_click(event):
        if event.inaxes == ax:
            x, y = event.xdata, event.ydata
            for node, (nx_pos, ny_pos) in pos.items():
                dx, dy = x - nx_pos, y - ny_pos
                dist = (dx**2 + dy**2)**0.5
                if dist < 0.05:
                    mostrar_tabla(G.nodes[node]['docs'])
                    break

    fig.canvas.mpl_connect('button_press_event', on_click)

    ax.set_title("Similitud de documentos agrupados por porcentaje")
    plt.axis('off')

    os.makedirs('resultados/graficos', exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'resultados/graficos/grafo_similitudes_{timestamp}.png'

    plt.savefig(filename)
    plt.show()
