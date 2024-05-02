#Paulo Enrique Muñoz Razón    21310181_E1      2 de Mayo del 2024
#Inteligencia artificial
#Probabilidad (Incertidumbre)

#Probabilidad-Monte Carlo para Cadenas de Markov

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import random

# Función para simular el lanzamiento de una moneda
def lanzamiento_moneda():
    # Genera un número aleatorio entre 0 y 1
    valor = random.random()
    # Devuelve 'cara' si el valor es menor que 0.5, 'cruz' de lo contrario
    return 'cara' if valor < 0.5 else 'cruz'

# Función para simular el proceso de Monte Carlo para Cadenas de Markov (MCMC)
def monte_carlo_cadenas_markov(iteraciones):
    # Inicializa el estado actual con un lanzamiento aleatorio de la moneda
    estado_actual = lanzamiento_moneda()
    # Inicializa el contador de 'cara' y 'cruz'
    contador_cara = 0
    contador_cruz = 0

    # Itera sobre el número especificado de iteraciones
    for _ in range(iteraciones):
        # Incrementa el contador correspondiente al estado actual
        if estado_actual == 'cara':
            contador_cara += 1
        else:
            contador_cruz += 1

        # Realiza un nuevo lanzamiento de la moneda para actualizar el estado actual
        estado_actual = lanzamiento_moneda()

    # Calcula las probabilidades de obtener 'cara' y 'cruz' utilizando el método de Monte Carlo
    probabilidad_cara = contador_cara / iteraciones
    probabilidad_cruz = contador_cruz / iteraciones

    # Imprime los resultados
    print("Después de", iteraciones, "iteraciones:")
    print("Probabilidad de cara:", probabilidad_cara)
    print("Probabilidad de cruz:", probabilidad_cruz)

# Número de iteraciones para el método de Monte Carlo
iteraciones = 10000

# Ejecuta el método de Monte Carlo para Cadenas de Markov
monte_carlo_cadenas_markov(iteraciones)
