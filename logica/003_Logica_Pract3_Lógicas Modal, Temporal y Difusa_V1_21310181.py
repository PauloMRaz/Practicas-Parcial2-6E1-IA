#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica-Lógicas Modal, Temporal y Difusa

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Lógica Temporal
class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

class Transicion:
    def __init__(self, estado_origen, estado_destino, accion):
        self.estado_origen = estado_origen
        self.estado_destino = estado_destino
        self.accion = accion

# Crear estados y transiciones
estado_1 = Estado("Estado 1")
estado_2 = Estado("Estado 2")
transicion_1_2 = Transicion(estado_1, estado_2, "A")

# Verificar si hay una transición válida desde el estado 1 al estado 2
print("¿Hay una transición válida desde el estado 1 al estado 2?", transicion_1_2.estado_origen == estado_1 and transicion_1_2.estado_destino == estado_2)

