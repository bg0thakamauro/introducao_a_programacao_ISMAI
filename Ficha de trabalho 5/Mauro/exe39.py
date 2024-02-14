import random

frase = input("Insira uma frase")
palavras_embaralhadas = ' '.join(random.sample(frase.split(), len(frase.split())))
print("Frase com palavras embaralhadas:", palavras_embaralhadas)
palavras_invertidas = ' '.join(frase.split()[::-1])