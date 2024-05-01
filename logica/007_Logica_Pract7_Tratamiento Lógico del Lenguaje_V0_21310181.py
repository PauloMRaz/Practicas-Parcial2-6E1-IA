#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Lógica-Tratamiento Lógico del Lenguaje

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Descargar recursos de NLTK (solo necesitas hacerlo una vez)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Oración de ejemplo
oracion = "El gato está en la alfombra y el perro está en el jardín."

# Tokenización de la oración en palabras
palabras = word_tokenize(oracion.lower())  # Convertir a minúsculas para normalización

# Eliminar palabras vacías (stop words)
palabras = [palabra for palabra in palabras if palabra not in stopwords.words('spanish')]

# Lematización de palabras
lemmatizador = WordNetLemmatizer()
palabras_lematizadas = [lemmatizador.lemmatize(palabra) for palabra in palabras]

# Mostrar resultado
print("Oración original:", oracion)
print("Palabras después del tratamiento lógico:", palabras_lematizadas)
