n1 = int(input("Insira o valor do Red"))
n2 = int(input("Insira o valor do Blue"))
n3 = int(input("Insira o valor do Green"))

n4 = max(n1, n2, n3)

if(n1 == n2 or n1 == n3 or n3 == n2):
    print("algum dos valores é igual a outro, atenção a resposta final que pode confundir")

if(n4 == n1):
    print("Red")
if(n4 == n2):
    print("Blue")
if(n4 == n3):
    print("Green")