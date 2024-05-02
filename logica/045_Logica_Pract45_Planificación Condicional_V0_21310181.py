#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Planificación-Planificación Condicional

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

# Definición de las reglas de planificación condicional
reglas_planificacion = [
    ({'ingredientes': 'huevos', 'utensilios': 'sartén'}, 'cocinar_huevos'),
    ({'ingredientes': 'pan', 'utensilios': 'tostadora'}, 'tostar_pan'),
    ({'ingredientes': 'café', 'utensilios': 'cafetera'}, 'preparar_café')
]

# Función para planificar las acciones
def planificar(estado_actual, reglas):
    acciones = []
    for condicion, accion in reglas:
        if all(item in estado_actual.items() for item in condicion.items()):
            acciones.append(accion)
    return acciones

# Estado actual de los ingredientes y utensilios disponibles
estado_actual = {'ingredientes': ['huevos', 'pan', 'café'], 'utensilios': ['sartén', 'tostadora', 'cafetera']}

# Planificar las acciones basadas en el estado actual
acciones_planificadas = planificar(estado_actual, reglas_planificacion)

# Mostrar las acciones planificadas
print("Acciones planificadas:")
for accion in acciones_planificadas:
    print("- " + accion)
