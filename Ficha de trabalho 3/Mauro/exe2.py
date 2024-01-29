n1 = int(input("Insira um valor: "))
n2 = int(input("Insira outro valor: "))

max = max(n1, n2)
min = min(n1, n2) + 1

while min < max:
    print(min)
    min += 1

print("o numero maior é o ", max)