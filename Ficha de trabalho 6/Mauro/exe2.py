def maior_absoluto(n1, n2, n3):
    abs_n1 = abs(n1)
    abs_n2 = abs(n2)
    abs_n3 = abs(n3)
    maior = max(abs_n1, abs_n2, abs_n3)

    return maior

n1 = float(input("Insira o valor: "))
n2 = float(input("Insira o valor: "))
n3 = float(input("Insira o valor: "))

maior_abs = maior_absoluto(n1, n2, n3)
print("O maior valor absoluto é:", maior_abs)
