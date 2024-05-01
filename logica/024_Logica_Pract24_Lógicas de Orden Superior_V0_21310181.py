#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Otras Lógicas-Lógicas de Orden Superior

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from z3 import *

# Crear un solucionador
solver = Solver()

# Definir variables
P = Function('P', IntSort(), BoolSort())
Q = Function('Q', IntSort(), BoolSort())
x = Int('x')

# Agregar restricciones
solver.add(ForAll(x, Implies(P(x), Q(x))))

# Verificar la satisfactibilidad
print(solver.check())

# Obtener el modelo si es satisfacible
if solver.check() == sat:
    print(solver.model())
