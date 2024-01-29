vetor = []
for i in range(10):
    valor = int(input("Insira um valor"))
    vetor.append(valor)

n1 = int(input("Insira o valor que deseja procurar"))
n2 = 0

for i in range(10):
    if(vetor[i] == n1):
        n2 = i

if n2 > 0:
    print(i)
else:
    print("Nao existe")