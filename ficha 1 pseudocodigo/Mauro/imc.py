def calculo_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Insira o peso: "))
altura = float(input("Insira a altura: "))

imc = calculo_imc(peso, altura)

print("O IMC é:", imc)
