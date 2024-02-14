import random

def baralharvogais(texto):
    texto= texto.lower()

    vogais = 'aeiou'
    for i in range (len(texto)-1):
        if texto[i] == vogais:
            texto1[i] = random.vogais[random]
    return texto1

texto1 = ""
texto = input("Insira a palavra")
final = baralharvogais(texto1)
print(final)