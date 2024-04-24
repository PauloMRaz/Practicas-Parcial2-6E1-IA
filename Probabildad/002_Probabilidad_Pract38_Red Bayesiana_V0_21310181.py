#Paulo Enrique Muñoz Razón    21310181_E1      24/Abril/2024
#Inteligencia artificial
#Probabilidad (Incertidumbre)

#Probabilidad-Razonamiento Probabilístico: Red Bayesiana
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Definir la estructura del modelo
modelo = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# Entrenar el modelo con datos
datos = pd.DataFrame(data={'D': ['F', 'F', 'T', 'F', 'T'],
                           'I': ['F', 'T', 'F', 'T', 'F'],
                           'G': ['F', 'F', 'T', 'T', 'F'],
                           'L': ['F', 'F', 'T', 'T', 'F'],
                           'S': ['F', 'F', 'F', 'T', 'T']})
modelo.fit(datos, estimator=MaximumLikelihoodEstimator)

# Realizar inferencia en el modelo
inferencia = VariableElimination(modelo)
probabilidad = inferencia.query(variables=['L'], evidence={'D': 'T', 'I': 'T'})
print(probabilidad)
