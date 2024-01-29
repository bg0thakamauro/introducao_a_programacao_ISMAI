c1 = 0
n2 = 2222222222222222222222222
n3 = 0
n1 = 0

while c1 < 11:
    if(n1 == 10):
        if(n1 == n2):
            n3 += 1
        n2 = n1
        c1 += 1
    else:
        n1 = int(input("Insira um numero"))
        if(n1 == n2):
            n3 += 1
        n2 = n1
        c1 += 1

print(n3)

##por corrigir
    