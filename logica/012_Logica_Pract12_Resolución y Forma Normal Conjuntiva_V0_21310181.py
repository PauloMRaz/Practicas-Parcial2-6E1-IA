#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica Proposicional-Resolución y Forma Normal Conjuntiva

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from sympy import symbols, Or, And, Not, to_cnf, satisfiable

# Definir las variables proposicionales
p, q, r = symbols('p q r')

# Ejemplo de fórmula proposicional
formula = And(Or(p, q), Or(Not(r), q))

# Convertir a Forma Normal Conjuntiva (FNC)
fnc = to_cnf(formula)

# Verificar satisfacibilidad de la FNC
if satisfiable(fnc):
    print("La FNC es satisfacible.")
else:
    print("La FNC no es satisfacible.")
