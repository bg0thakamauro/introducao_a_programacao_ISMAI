string = input("Digite uma string: ")
substring = input("Digite a substring que deseja contar: ")
contador = 0
index = string.find(substring)
while index != -1:
    contador += 1
    index = string.find(substring, index + 1)
print(f"A substring '{substring}' ocorre {contador} vezes na string.")
