n1 = int(input("Insira o angulo 1: "))
n2 = int(input("Insira o angulo 2: "))

n3 = n1 + n2

if n3 > 180:
    print("foi inserido algulos maiores do que era suposto")
else:
    n4 = 180 - n3
    print("O valor do 3 angulo é: ", n4)