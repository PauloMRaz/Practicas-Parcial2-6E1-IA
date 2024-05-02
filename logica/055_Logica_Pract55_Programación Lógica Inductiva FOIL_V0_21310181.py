#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Aprendizaje Inductivo-Programación Lógica Inductiva: FOIL

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from pyswip import Prolog

def foil(examples):
    prolog = Prolog()
    prolog.assertz(":- use_module(library(foil)).")
    
    for example in examples:
        prolog.assertz(example)
    
    prolog.assertz(":- foil.")
    for result in prolog.query("induce_rules"):
        print(result)

# Ejemplo de datos de entrenamiento
examples = [
    "pos(ex1).",
    "neg(ex2).",
    "pos(ex3).",
    "neg(ex4)."
]

# Ejecutar FOIL en los ejemplos
foil(examples)
