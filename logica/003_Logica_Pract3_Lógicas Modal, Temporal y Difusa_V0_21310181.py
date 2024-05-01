#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica-Lógicas Modal, Temporal y Difusa

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Lógica Modal
class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre

class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conoce = set()

    def conoce_mundo(self, mundo):
        self.conoce.add(mundo.nombre)

# Crear mundos y agentes
mundo_a = Mundo("A")
mundo_b = Mundo("B")
agente_1 = Agente("Agente 1")

# El agente 1 conoce el mundo A
agente_1.conoce_mundo(mundo_a)

# Verificar si el agente conoce el mundo B
print("¿El agente 1 conoce el mundo B?", mundo_b.nombre in agente_1.conoce)
