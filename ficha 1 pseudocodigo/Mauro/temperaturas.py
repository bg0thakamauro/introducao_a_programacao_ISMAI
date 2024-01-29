def convertertemperatura(tempc):
    return ((tempc * 9) / 5) + 31 

tempc = float(input("Digite o comprimento do primeiro cateto: "))

tempf = convertertemperatura(tempc)
print("A hipotenusa é:", tempf)