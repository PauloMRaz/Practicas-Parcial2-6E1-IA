#Paulo Enrique Muñoz Razón    21310181_E1      9/Abril/2024
#Inteligencia artificial
#Busqueda en grafos

#Busqueda no informada-Búsqueda en Profundidad Limitada

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def dlfs(nodo, grafo, visitado, limite):#Búsqueda en Profundidad Limitada (DLFS por sus siglas en inglés, Depth-Limited Search)
    if limite >= 0:
        if nodo not in visitado:
            print(nodo)  # Aquí podrías realizar cualquier operación con el nodo
            visitado.add(nodo)
            for vecino in grafo[nodo]:
                dlfs(vecino, grafo, visitado, limite - 1)

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
visitado = set()
limite_profundidad = 2
print(f"Recorrido Busqueda en profundidad Limitado a Profundidad {limite_profundidad}:")
dlfs(inicio, grafo, visitado, limite_profundidad)
