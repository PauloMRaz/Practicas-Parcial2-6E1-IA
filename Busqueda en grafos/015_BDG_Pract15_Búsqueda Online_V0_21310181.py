#Paulo Enrique Muñoz Razón    21310181_E1      16/Abril/2024
#Inteligencia artificial
#Busqueda en grafos

#Busqueda no informada-Búsqueda Online

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import time
import random

def busqueda_en_linea():
    objetivo = 42  # Valor que queremos encontrar
    while True:
        nueva_informacion = random.randint(1, 100)  # Simulación de nueva información recibida
        print("Nueva información recibida:", nueva_informacion)
        
        if nueva_informacion == objetivo:
            print("¡Objetivo encontrado!")
            break
        
        time.sleep(1)  # Simulación de procesamiento en tiempo real
        
        # Verificar si se ha ingresado una señal para detener el bucle
        if input("Presiona 'q' y Enter para detener la búsqueda en línea: ") == 'q':
            print("Búsqueda en línea detenida.")
            break

# Ejecutar la búsqueda en línea
busqueda_en_linea()

