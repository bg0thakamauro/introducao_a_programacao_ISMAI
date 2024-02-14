def verificarletras(texto):
    texto = texto.lower()
    contador = 0
    for i in range (len(texto)-1):
        if texto[i] == texto[i + 1] and texto[i].isalpha():
            contador += 1
    return contador

texto=input("Insira um texto")
final = verificarletras(texto)
print(final)