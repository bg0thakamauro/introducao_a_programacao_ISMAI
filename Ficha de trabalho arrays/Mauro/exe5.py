vetor = []
for i in range(3):
    valor = int(input("Insira um valor: "))
    vetor.append(valor)

maximo = max(vetor)
segundo_maximo = float('-inf')

for valor in vetor:
    if valor != maximo and valor > segundo_maximo:
        segundo_maximo = valor

print("O segundo maior valor é:", segundo_maximo)
