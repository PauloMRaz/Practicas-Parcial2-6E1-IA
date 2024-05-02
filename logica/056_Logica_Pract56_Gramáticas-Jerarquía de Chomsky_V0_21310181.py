#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Tratamiento Lógico del Lenguaje-Gramáticas: Jerarquía de Chomsky

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import nltk

# Definir la gramática
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V | V NP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'rug'
    V -> 'chased' | 'sat'
    P -> 'on' | 'in'
""")

# Crear un parser para la gramática
parser = nltk.ChartParser(grammar)

# Definir una oración para analizar
sentence = "the cat chased the dog".split()

# Realizar el análisis sintáctico de la oración
for tree in parser.parse(sentence):
    print(tree)
    tree.draw()  # Mostrar el árbol de análisis sintáctico
