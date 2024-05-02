#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Planificación-Planificación de Orden Parcial

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from pddlpy import DomainProblem

# Definir el dominio y el problema
domain = """
(define (domain planificacion)
  (:requirements :strips :typing)
  (:types accion)

  (:predicates
    (ejecutada ?x - accion)
  )

  (:action accion-1
    :parameters ()
    :precondition ()
    :effect (and (ejecutada accion-1))
  )

  (:action accion-2
    :parameters ()
    :precondition ()
    :effect (and (ejecutada accion-2))
  )
)
"""

problem = """
(define (problem planificacion-1)
  (:domain planificacion)
  (:objects)
  (:init)
  (:goal (and (ejecutada accion-1) (ejecutada accion-2)))
)
"""

# Crear el problema de planificación
planificacion = DomainProblem(domain, problem)

# Resolver el problema
solution = planificacion.solve()

# Imprimir la solución
print("Planificación de Orden Parcial:")
for action in solution:
    print(action)
