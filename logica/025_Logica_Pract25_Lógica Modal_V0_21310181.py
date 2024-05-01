#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Otras Lógicas-Lógica Modal

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

class ModalLogicParser:
    def __init__(self):
        self.propositions = set()
        self.modal_operators = {'□', '◇'}

    def parse(self, expression):
        tokens = expression.split()
        modal_operator = None
        propositions = []

        for token in tokens:
            if token in self.modal_operators:
                modal_operator = token
            else:
                propositions.append(token)

        return modal_operator, propositions

class ModalLogicSystem:
    def __init__(self):
        self.parser = ModalLogicParser()

    def evaluate(self, expression):
        modal_operator, propositions = self.parser.parse(expression)

        if modal_operator == '□':
            # Evaluación de la modalidad "necesidad"
            result = all(propositions)
        elif modal_operator == '◇':
            # Evaluación de la modalidad "posibilidad"
            result = any(propositions)
        else:
            # Sin operador modal, asumimos una proposición simple
            result = True if propositions else False

        return result

# Ejemplo de uso
logic_system = ModalLogicSystem()
expression = '□ P ∧ Q'
result = logic_system.evaluate(expression)
print(f"Resultado de la expresión '{expression}': {result}")


