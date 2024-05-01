#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica-Planificación

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from collections import deque

# Definición del laberinto
laberinto = {
    'entrada': ['sala1'],
    'sala1': ['sala2', 'sala3'],
    'sala2': ['sala4'],
    'sala3': ['sala5'],
    'sala4': ['sala6'],
    'sala5': ['sala6'],
    'sala6': ['salida'],
    'salida': []
}

# Función de búsqueda BFS
def bfs(inicio, objetivo):
    cola = deque([[inicio]])
    visitado = set()
    
    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]
        
        if nodo_actual == objetivo:
            return camino
        
        if nodo_actual not in visitado:
            for vecino in laberinto[nodo_actual]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
                
            visitado.add(nodo_actual)
    
    return None

# Planificación: ir de la entrada a la salida
inicio = 'entrada'
objetivo = 'salida'
camino_planificado = bfs(inicio, objetivo)

# Mostrar el plan
if camino_planificado:
    print("Plan encontrado:", camino_planificado)
else:
    print("No se encontró un plan.")
