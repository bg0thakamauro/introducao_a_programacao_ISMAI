# 8-bit Unicode Transformation Format - https://pt.wikipedia.org/wiki/UTF-8
#coding: utf-8

# taxa fixa de conversao
TAXA = 1.17

# Ler valor em euros
valorEuro = float(input("Introduza valor em euros -> "))

# calcular o valor em dolar
valorDolar = valorEuro * TAXA

# mostrar resultado
print("Valor em dolar =", valorDolar)

