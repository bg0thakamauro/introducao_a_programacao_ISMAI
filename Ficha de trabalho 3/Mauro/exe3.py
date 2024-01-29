n1 = int(input("Insira um numero de 1-9"))
n2 = 1

if(n1 > 9 or n1 < 1):
    print("nao foi inserido o numero correto ao qual foi pedido")
else:
    while n2 < 11:
        print(n1*n2)
        n2 += 1


