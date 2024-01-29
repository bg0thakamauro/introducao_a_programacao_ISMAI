vetor = []
for i in range(10):
    valor = int(input("Insira um valor"))
    vetor.append(valor)

max = vetor[0]
maxp = 0

for i in range(1, 10):
    if vetor[i] > max:
        max = vetor[i]
        maxp = i
print(max)
print(maxp)