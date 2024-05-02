#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Planificación-Redes Jerárquicas de Tareas

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

# Definición de la red jerárquica de tareas
tareas = {
    'Proyecto': {
        'Investigación': {
            'Recopilar información': None,
            'Revisar literatura': None
        },
        'Desarrollo': {
            'Diseñar prototipo': None,
            'Implementar funcionalidades': None
        },
        'Pruebas': {
            'Ejecutar pruebas unitarias': None,
            'Realizar pruebas de integración': None
        }
    }
}

# Función para imprimir la red jerárquica de tareas
def imprimir_tareas(tareas, nivel=0):
    for tarea, sub_tareas in tareas.items():
        print('  ' * nivel + tarea)
        if sub_tareas:
            imprimir_tareas(sub_tareas, nivel + 1)

# Imprimir la red jerárquica de tareas
imprimir_tareas(tareas)
