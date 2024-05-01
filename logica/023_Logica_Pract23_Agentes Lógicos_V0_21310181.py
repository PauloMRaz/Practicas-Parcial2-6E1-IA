#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica de 1er Orden-Agentes Lógicos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from pyDatalog import pyDatalog

# Definir las reglas lógicas
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

# Reglas lógicas: definición de relaciones entre los términos
+padre('juan', 'pepe')
+padre('pepe', 'juanito')
+padre('pepe', 'maría')
+padre('paco', 'pepe')

abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)

# Consultas lógicas
print(abuelo(X, 'juanito'))
print(abuelo('paco', Y))
