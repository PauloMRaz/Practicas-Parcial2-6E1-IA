#Paulo Enrique Muñoz Razón    21310181_E1      24/Abril/2024
#Inteligencia artificial
#Probabilidad (Incertidumbre)

#Probabilidad-- Aprendizaje Probabilístico:Aprendizaje Profundo (Deep Learning)
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.keras import layers, models

# Cargar y preprocesar datos
(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = tf.keras.datasets.mnist.load_data()
x_entrenamiento, x_prueba = x_entrenamiento / 255.0, x_prueba / 255.0

# Definir el modelo de red neuronal profunda
modelo = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Capa de entrada: aplanar la imagen 28x28 en un vector de 784 elementos
    layers.Dense(128, activation='relu'),  # Capa oculta: 128 neuronas con función de activación ReLU
    layers.Dropout(0.2),                   # Dropout para regularización
    layers.Dense(10, activation='softmax') # Capa de salida: 10 neuronas con función de activación softmax
])

# Compilar el modelo
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(x_entrenamiento, y_entrenamiento, epochs=5)

# Evaluar el modelo
puntuacion = modelo.evaluate(x_prueba, y_prueba)
print("Precisión en el conjunto de prueba:", puntuacion[1])
