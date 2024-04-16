#Paulo Enrique Muñoz Razón    21310181_E1      9/Abril/2024
#Inteligencia artificial
#Busqueda en grafos

#Busqueda informada-Búsqueda Voraz Primero el Mejor

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import heapq

def greedy_best_first_search(grafo, inicio, objetivo, heuristica):
    cola_prioridad = [(heuristica(inicio, objetivo), inicio)]
    visitado = set()
    
    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)  # Desempaquetar la tupla correctamente
        
        if nodo_actual == objetivo:
            return True  # Se encontró el objetivo
        
        visitado.add(nodo_actual)
        
        for vecino in grafo[nodo_actual]:
            if vecino not in visitado:
                heapq.heappush(cola_prioridad, (heuristica(vecino, objetivo), vecino))
    
    return False  # No se encontró el objetivo

# Ejemplo de función heurística (en este caso, distancia euclidiana)
def distancia_euclidiana(nodo, objetivo):
    # Suponiendo que los nodos son coordenadas en un espacio bidimensional
    x1, y1 = nodo
    x2, y2 = objetivo
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'

# Ejecutar la búsqueda
if greedy_best_first_search(grafo, inicio, objetivo, distancia_euclidiana):
    print(f"Se encontró un camino desde {inicio} hasta {objetivo}")
else:
    print(f"No se encontró un camino desde {inicio} hasta {objetivo}")



