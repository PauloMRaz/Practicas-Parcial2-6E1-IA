#Paulo Enrique Muñoz Razón    21310181_E1      2 de Mayo del 2024
#Inteligencia artificial
#Probabilidad (Incertidumbre)

#Probabilidad-Hamming, Hopfield, Hebb, Boltzmann, ...
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

#Algoritmo de Hopfield
import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        for pattern in patterns:
            pattern_row = np.reshape(pattern, (1, self.num_neurons))
            self.weights += np.dot(pattern_row.T, pattern_row)
        np.fill_diagonal(self.weights, 0)

    def predict(self, input_pattern, max_iter=100):
        output_pattern = input_pattern.copy()
        for _ in range(max_iter):
            new_output_pattern = np.sign(np.dot(output_pattern, self.weights))
            if np.array_equal(new_output_pattern, output_pattern):
                break
            output_pattern = new_output_pattern
        return output_pattern

# Ejemplo de uso
patterns = np.array([
    [-1, 1, -1, 1],
    [1, -1, 1, -1],
    [-1, -1, -1, -1]
])
num_neurons = len(patterns[0])
hopfield_net = HopfieldNetwork(num_neurons)
hopfield_net.train(patterns)

input_pattern = np.array([1, 1, 1, -1])
predicted_pattern = hopfield_net.predict(input_pattern)
print("Patrón de entrada:", input_pattern)
print("Patrón predicho:", predicted_pattern)
