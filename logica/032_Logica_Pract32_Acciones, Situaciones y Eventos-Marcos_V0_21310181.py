#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Acciones, Situaciones y Eventos: Marcos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

# Definir un diccionario para representar un marco de acción
accion_marco = {
    "nombre": "ir_al_supermercado",
    "actor": "yo",
    "objetivo": "comprar alimentos",
    "recursos": ["dinero", "lista de compras"],
    "efectos": ["adquirir alimentos", "gastar dinero"],
    "duración": "1 hora"
}

# Función para imprimir un marco de acción
def imprimir_marco(marco):
    print("Nombre:", marco["nombre"])
    print("Actor:", marco["actor"])
    print("Objetivo:", marco["objetivo"])
    print("Recursos:", marco["recursos"])
    print("Efectos:", marco["efectos"])
    print("Duración estimada:", marco["duración"])

# Imprimir el marco de acción
print("Marco de acción:")
imprimir_marco(accion_marco)
