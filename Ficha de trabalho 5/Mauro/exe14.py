n1 = input("Insira a palavra")
contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
n1 = n1.lower()
for char in n1:
    if char in contagem_vogais:
        contagem_vogais[char] += 1

print(contagem_vogais)
