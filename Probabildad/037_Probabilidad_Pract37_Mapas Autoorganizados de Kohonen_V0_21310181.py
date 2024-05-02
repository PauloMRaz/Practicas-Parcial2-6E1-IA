#Paulo Enrique Muñoz Razón    21310181_E1      2 de Mayo del 2024
#Inteligencia artificial
#Probabilidad (Incertidumbre)

#Probabilidad-Mapas Autoorganizados de Kohonen
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from minisom import MiniSom
import numpy as np

# Generar datos de ejemplo
data = np.random.rand(100, 10)

# Configurar y entrenar el SOM
som = MiniSom(10, 10, 10, sigma=0.5, learning_rate=0.5)
som.train_random(data, 100)

# Visualizar el mapa de neuronas
from pylab import pcolor, colorbar, plot
pcolor(som.distance_map().T)
colorbar()

# Obtener las etiquetas de agrupamiento para cada muestra
labels = som.labels_map(data)
print("Etiquetas de agrupamiento:", labels)
