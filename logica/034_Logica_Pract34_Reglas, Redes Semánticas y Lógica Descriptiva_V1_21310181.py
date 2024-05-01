#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Reglas, Redes Semánticas y Lógica Descriptiva

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Redes Semánticas:
# Ejemplo de red semántica en Python (usando diccionarios)
red_semantica = {
    "animal": ["perro", "gato", "pájaro"],
    "mamífero": ["perro", "gato"],
    "ave": ["pájaro"]
}

# Consultar la red semántica
print(red_semantica["mamífero"])  # Salida: ['perro', 'gato']
print(red_semantica["ave"])       # Salida: ['pájaro']
