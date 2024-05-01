#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica de 1er Orden-Sintaxis y Semántica: Cuantificadores

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from sympy import symbols, Q, ask, Any

# Definir la variable x
x = symbols('x')

# Expresar la afirmación "para todo x, x es positivo o x es negativo"
afirmacion_universal = Q.positive(x) | Q.negative(x)

# Expresar la afirmación "existe un x tal que x es positivo"
afirmacion_existencial = Any(x, Q.positive(x))

# Verificar si la afirmación universal es verdadera
if ask(afirmacion_universal):
    print("La afirmación universal es verdadera.")
else:
    print("La afirmación universal es falsa.")

# Verificar si la afirmación existencial es verdadera
if ask(afirmacion_existencial):
    print("La afirmación existencial es verdadera.")
else:
    print("La afirmación existencial es falsa.")
