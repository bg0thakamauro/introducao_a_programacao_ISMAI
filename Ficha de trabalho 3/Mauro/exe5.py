n1 = input("escreva o seu nome")
n2 = int(input("Escreva quantas vezes quer que escreva o nome 0-20"))

while n2 > 0 and n2 < 21:
    print(n1)
    n2 = n2 - 1

if(n2 > 20):
    print("erro, numero maior que 20")