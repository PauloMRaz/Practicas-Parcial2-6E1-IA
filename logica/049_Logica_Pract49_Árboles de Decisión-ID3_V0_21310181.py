#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Aprendizaje Inductivo-Árboles de Decisión: ID3

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Cargar el conjunto de datos de Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Etiquetas

# Inicializar y entrenar el clasificador de árbol de decisión
classifier = DecisionTreeClassifier(criterion='entropy')  # Utilizando el criterio de entropía para el algoritmo ID3
classifier.fit(X, y)

# Imprimir el árbol de decisión
tree_rules = export_text(classifier, feature_names=iris.feature_names)
print(tree_rules)
