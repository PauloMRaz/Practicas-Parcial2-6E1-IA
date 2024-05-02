#Paulo Enrique Muñoz Razón    21310181_E1      2 de Mayo del 2024
#Inteligencia artificial
#Probabilidad (Incertidumbre)

#Probabilidad-Hamming, Hopfield, Hebb, Boltzmann, ...
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

#Algoritmo de Hamming
def hamming_distance(vector1, vector2):
    """Calcula la distancia de Hamming entre dos vectores de bits."""
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud.")
    distance = sum(bit1 != bit2 for bit1, bit2 in zip(vector1, vector2))
    return distance

# Ejemplo de uso
vector1 = [0, 1, 0, 1, 1]
vector2 = [1, 1, 0, 0, 1]
distance = hamming_distance(vector1, vector2)
print("Distancia de Hamming:", distance)
