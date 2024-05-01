#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica de 1er Orden-Encadenamiento: Hacia Delante y Atrás

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

# Definición de hechos y reglas
hechos = {
    "humano": ["juan", "maría", "pedro"],
    "mortal": ["juan", "maría", "pedro"]
}

reglas = [
    {"antecedente": ["humano", "?x"], "consecuente": ["mortal", "?x"]}
]

def encadenamiento_hacia_adelante(hechos, reglas):
    nuevo_hecho = True
    while nuevo_hecho:
        nuevo_hecho = False
        for regla in reglas:
            antecedente_verdadero = True
            for elemento in regla["antecedente"]:
                if elemento[0] != "?":  # Si no es una variable
                    if elemento not in hechos:
                        antecedente_verdadero = False
                        break
                else:  # Si es una variable
                    variable = elemento[1:]
                    if variable not in hechos:
                        antecedente_verdadero = False
                        break
            if antecedente_verdadero:
                for elemento in regla["consecuente"]:
                    if elemento[0] == "?":  # Si es una variable
                        variable = elemento[1:]
                        hechos[variable] = [hecho for hecho in hechos[regla["antecedente"][1]]]
                    else:  # Si no es una variable
                        hechos[elemento] = [hecho for hecho in hechos[regla["antecedente"][1]]]
                nuevo_hecho = True

def encadenamiento_hacia_atras(hechos, reglas, objetivo):
    if objetivo in hechos:
        return True
    for regla in reglas:
        if regla["consecuente"][1] == objetivo:
            antecedente_verdadero = True
            for elemento in regla["antecedente"]:
                if elemento[0] != "?":  # Si no es una variable
                    if elemento not in hechos:
                        antecedente_verdadero = False
                        break
                else:  # Si es una variable
                    variable = elemento[1:]
                    if not encadenamiento_hacia_atras(hechos, reglas, variable):
                        antecedente_verdadero = False
                        break
            if antecedente_verdadero:
                return True
    return False

# Ejemplo de uso
encadenamiento_hacia_adelante(hechos, reglas)
print("Hechos después de encadenamiento hacia adelante:", hechos)

objetivo = "mortal"
resultado = encadenamiento_hacia_atras(hechos, reglas, objetivo)
print(f"¿Es {objetivo} un hecho? {resultado}")
