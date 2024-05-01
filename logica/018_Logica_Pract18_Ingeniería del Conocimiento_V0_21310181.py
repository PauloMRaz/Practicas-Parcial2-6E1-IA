#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica de 1er Orden-Ingeniería del Conocimiento

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

class SistemaDiagnostico:
    def __init__(self):
        self.reglas_diagnosticos = {
            "faringitis": ["fiebre", "dolor de garganta"],
            "sarampion": ["fiebre", "erupcion cutanea"]
        }

    def diagnosticar_sintomas(self, sintomas):
        for enfermedad, condiciones in self.reglas_diagnosticos.items():
            if all(condicion in sintomas for condicion in condiciones):
                return enfermedad
        return "No se pudo diagnosticar la enfermedad"


# Crear una instancia del sistema de diagnóstico
sistema = SistemaDiagnostico()

# Síntomas del paciente
sintomas_paciente = ["fiebre", "dolor de garganta"]

# Diagnosticar enfermedad
enfermedad_diagnosticada = sistema.diagnosticar_sintomas(sintomas_paciente)
print("Enfermedad diagnosticada:", enfermedad_diagnosticada)
