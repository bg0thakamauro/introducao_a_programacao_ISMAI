# 8-bit Unicode Transformation Format - https://pt.wikipedia.org/wiki/UTF-8
#coding: utf-8

# variavel constante 
PI = 3.1415

# Ler o valor do raio
raio = float(input("Introduza o valor do raio -> "))

# Calcular o perimetro e área
perimetro = 2 * PI * raio
area = PI * raio**2

# Apresentar resultados
print("Área ->", area)
print("Perimetro -> %.2f"  % perimetro)

