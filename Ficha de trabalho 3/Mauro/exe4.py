n1 = int(input("Insira um numero de de incrementos que quer 1-10"))
n2 = 0

if(n1 > 9 or n1 < 1):
    print("nao foi inserido o numero correto ao qual foi pedido")
else:
    while n2 < 101 :
        print(n2)
        n2 += n1



