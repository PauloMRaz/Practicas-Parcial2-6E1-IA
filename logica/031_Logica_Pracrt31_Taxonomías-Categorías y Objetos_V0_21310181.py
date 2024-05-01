#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Taxonomías: Categorías y Objetos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

# Definir la taxonomía como un diccionario
taxonomia = {
    "animales": ["perro", "gato", "pájaro"],
    "frutas": ["manzana", "banana", "naranja"],
    "colores": ["rojo", "verde", "azul"]
}

# Función para imprimir la taxonomía
def imprimir_taxonomia(taxonomia):
    for categoria, objetos in taxonomia.items():
        print(categoria + ":")
        for objeto in objetos:
            print("  -", objeto)

# Imprimir la taxonomía
print("Taxonomía:")
imprimir_taxonomia(taxonomia)
