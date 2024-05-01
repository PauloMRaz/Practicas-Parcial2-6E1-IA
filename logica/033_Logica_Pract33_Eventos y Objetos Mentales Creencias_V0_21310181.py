#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Eventos y Objetos Mentales: Creencias

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

# Definir un diccionario para representar un evento
evento = {
    "nombre": "reunión con el cliente",
    "fecha": "2024-05-10",
    "lugar": "oficina del cliente",
    "hora": "15:00",
    "duración": "2 horas",
    "objetivo": "presentar propuesta de proyecto"
}

# Imprimir información del evento
print("Evento:", evento["nombre"])
print("Fecha:", evento["fecha"])
print("Lugar:", evento["lugar"])
print("Hora:", evento["hora"])
print("Duración:", evento["duración"])
print("Objetivo:", evento["objetivo"])

# Definir un diccionario para representar una creencia
creencia = {
    "sujeto": "yo",
    "contenido": "El cliente está interesado en nuestra propuesta.",
    "fecha": "2024-05-10"
}

# Imprimir información de la creencia
print("\nCreencia:", creencia["contenido"])
print("Sujeto:", creencia["sujeto"])
print("Fecha:", creencia["fecha"])
