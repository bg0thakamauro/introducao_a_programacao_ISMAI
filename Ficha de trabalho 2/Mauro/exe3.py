n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
n3 = int(input("Insira o terceiro numero: "))

maior = max(n1, n2, n3)

if(n1 == n2 and n2 == n3):
    print("os numeros sao iguais")
else:
    print(maior)