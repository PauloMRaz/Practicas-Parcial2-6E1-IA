#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Reglas, Redes Semánticas y Lógica Descriptiva

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Reglas
# Ejemplo de regla en Python
def aplicar_descuento(edad):
    if edad < 18:
        return "Tiene derecho a un descuento del 20%."
    else:
        return "No tiene derecho a descuento."

# Aplicar la regla
print(aplicar_descuento(15))  # Salida: Tiene derecho a un descuento del 20%.
print(aplicar_descuento(20))  # Salida: No tiene derecho a descuento.
