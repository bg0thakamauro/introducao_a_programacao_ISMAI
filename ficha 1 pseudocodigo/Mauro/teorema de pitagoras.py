def calcular_hipotenusa(cateto1, cateto2):
    return (cateto1 * 2 + cateto2 * 2) * 0.5

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print("A hipotenusa é:", hipotenusa)
