def limpar_espacos(string):
    return string.strip()

# Exemplo de uso:
texto = "   maça  e pera              "
texto_limpo = limpar_espacos(texto)
print("Texto original:", texto)
print("Texto limpo:", texto_limpo)
