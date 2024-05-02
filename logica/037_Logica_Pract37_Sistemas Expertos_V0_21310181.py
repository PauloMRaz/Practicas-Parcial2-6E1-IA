#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Sistemas Expertos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

class SistemaExperto:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def consultar(self, pregunta):
        for regla in self.base_conocimiento:
            antecedente, consecuente = regla
            if all(hecho in pregunta for hecho in antecedente):
                return consecuente
        return "No se puede determinar la respuesta."

# Base de conocimiento de un sistema experto sobre diagnóstico médico
base_conocimiento_medico = [
    (["fiebre", "tos"], "resfriado"),
    (["fiebre", "dolor de garganta"], "amigdalitis"),
    (["dolor de cabeza", "mareos"], "migraña"),
    (["dolor de cabeza", "vómitos"], "migraña"),
    (["fiebre", "dolor de cabeza"], "gripe"),
]

# Crear un sistema experto médico
sistema_medico = SistemaExperto(base_conocimiento_medico)

# Consultar al sistema experto
sintomas = ["fiebre", "tos"]
diagnostico = sistema_medico.consultar(sintomas)
print("Los síntomas", sintomas, "pueden indicar:", diagnostico)
