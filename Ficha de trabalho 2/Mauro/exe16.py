n1 = int(input("Insira a hora atual em formado 24h"))
n2 = int(input("Insira os minutos"))

if n1 == 24 and n2 > 00:
    print("hora invalida")
else:
    n3 = 23 - n1
    n4 = 60 - n2
    print("Falta: ", n3, "horas e ", n4," minutos")
