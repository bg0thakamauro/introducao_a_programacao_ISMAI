# 8-bit Unicode Transformation Format - https://pt.wikipedia.org/wiki/UTF-8
#coding: utf-8

from math import sqrt, pow

# ler coordenadas do ponto 1
print("Indique as coordenadas do ponto 1 (x/y): ")
x1 = int(input())
y1 = int(input())

# ler coordenadas do ponto 2
print("Indique as coordenadas do ponto 1 (x/y): ")
x2 = int(input())
y2 = int(input())

# calcular a distancia
distancia = sqrt((x2 - x1)**2 + pow(y2 - y1,2))

# mostrar resultado
print("Distância = %.3f" % distancia)

