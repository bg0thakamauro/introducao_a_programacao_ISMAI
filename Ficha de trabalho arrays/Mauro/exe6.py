
vetor = []
for i in range (10):
    valor = int(input("insira um valor"))
    if valor in vetor:
        print("Valor ja inserido, porfavor, coloque outro")
    else:
        vetor.append(valor)
print(vetor)
