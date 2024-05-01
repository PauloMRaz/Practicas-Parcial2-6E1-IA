#Paulo Enrique Muñoz Razón      21310181      
#Practica 6               1 de Mayo de 2024
#Vision Artificial 
#Representar el Conocimiento-Ingeniería del Conocimiento: Ontologías

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from rdflib import Graph, Namespace, RDF, RDFS, Literal

# Cargar el grafo RDF desde el archivo
g = Graph()
g.parse("ontologia.rdf")

# Consulta SPARQL para obtener los nombres de las instancias
query = """
    PREFIX ex: <http://example.org/>
    SELECT ?nombre
    WHERE {
        ?instancia ex:name ?nombre .
    }
"""

# Ejecutar la consulta y obtener resultados
resultados = g.query(query)

# Imprimir los nombres de las instancias
print("Nombres de las instancias:")
for resultado in resultados:
    print(resultado["nombre"])


