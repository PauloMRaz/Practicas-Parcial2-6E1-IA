#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Reglas, Redes Semánticas y Lógica Descriptiva

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Lógica Descriptiva:
from owlready2 import *

# Cargar ontología desde un archivo OWL
onto = get_ontology("mi_ontologia.owl").load()

# Consultar la ontología
for clase in onto.classes():
    print(clase)
