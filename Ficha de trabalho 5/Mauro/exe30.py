frase = input("Insira a frase")

frase = frase.lower()

palavras = frase.split()

numerototal = 0
i = 0
for frase in palavras:
    if 'a' in frase:
        numerototal += 1

print(numerototal)
