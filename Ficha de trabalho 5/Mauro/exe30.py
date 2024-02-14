frase = input("Insira a frase")

frase = frase.lower()

palavras = frase.split()

numerototal = 0
i = 0
for palavra in palavras:
    if 'a' in palavra:
        numerototal += 1

print(numerototal)
