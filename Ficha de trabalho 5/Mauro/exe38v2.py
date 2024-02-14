def contarletrasrepetidas(texto):
    texto = texto.lower()
    i = 0
    contar = 0
    for i in range (len(texto)-1):
        if texto[i] == texto[i+1]:
            contar += 1
    return contar


texto=input("Insira o texto")
final = contarletrasrepetidas(texto)
print(final)