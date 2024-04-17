#Paulo Enrique Muñoz Razón    21310181_E1      17/Abril/2024
#Inteligencia artificial
#Busqueda en grafos

#Utilidad y Toma de Decisiones-Teoría de la Utilidad: Función de Utilidad

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def calcular_utilidad_esperada(opciones):
    utilidad_total = 0
    for opcion in opciones:
        resultado = opcion['resultado']
        probabilidad = opcion['probabilidad']
        utilidad_total += resultado * probabilidad
    return utilidad_total

# Definir las opciones y sus probabilidades asociadas
opcion_1 = {'resultado': 100, 'probabilidad': 0.6}
opcion_2 = {'resultado': 200, 'probabilidad': 0.4}

opciones = [opcion_1, opcion_2]

# Calcular la utilidad esperada de cada opción
utilidad_opcion_1 = calcular_utilidad_esperada(opciones)

# Imprimir los resultados
print("Utilidad esperada de la opción 1:", utilidad_opcion_1)

