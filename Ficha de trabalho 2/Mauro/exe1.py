n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))

maior = max(n1, n2)
menor = min(n1, n2)

if maior % menor == 0:
    print("numero maior é divisivel pelo menor")
else:
    print("nao é divisivel um pelo outro")