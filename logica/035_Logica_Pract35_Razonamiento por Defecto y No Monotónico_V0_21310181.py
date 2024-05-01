#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Razonamiento por Defecto y No Monotónico

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

class DefaultReasoner:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def infer(self, new_fact):
        # Verificar si el nuevo hecho contradice los hechos existentes
        if "not " + new_fact in self.facts:
            print("Conflicto encontrado. El nuevo hecho contradice un hecho existente.")
            return

        # Agregar el nuevo hecho
        self.facts.add(new_fact)
        print("Nuevo hecho inferido:", new_fact)

    def retract(self, fact):
        if fact in self.facts:
            self.facts.remove(fact)
            print("Hecho retraído:", fact)
        else:
            print("El hecho no está presente en la base de conocimientos.")

# Crear un razonador por defecto
reasoner = DefaultReasoner()

# Agregar algunos hechos iniciales
reasoner.add_fact("pájaros tienen alas")
reasoner.add_fact("pájaros pueden volar")

# Intentar inferir un nuevo hecho
reasoner.infer("pájaros pueden volar")

# Retraer un hecho existente
reasoner.retract("pájaros tienen alas")

# Intentar inferir un hecho contradictorio
reasoner.infer("no pájaros pueden volar")
