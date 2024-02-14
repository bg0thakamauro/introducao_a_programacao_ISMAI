numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("O maior número primo inferior a", numero, "é: 0")
else:
    for i in range(numero - 1, 1, -1):
        eh_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            print("O maior número primo inferior a", numero, "é:", i)
            break
    else:
        print("O maior número primo inferior a", numero, "é: 0")
