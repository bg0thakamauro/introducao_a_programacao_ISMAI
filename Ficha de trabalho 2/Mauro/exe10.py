n1 = int(input("Insira o numero de dias: "))

n2 = 0

while n1 > 7:
    n1 = n1 - 7
    n2 = n2 + 1

print("sao ", n2, " semanas e ", n1 ," dias ")