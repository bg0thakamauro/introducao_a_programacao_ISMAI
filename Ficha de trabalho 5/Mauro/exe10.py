nome_completo = input("Introduza o seu nome completo: ")
conta_espacos = nome_completo.count(" ")

primeiro_nome = ""
ultimo_nome = ""

if conta_espacos > 0:
    espaco = 0
    for carater in nome_completo:
        if carater == " ":
            espaco += 1
        if espaco == 0:
            primeiro_nome += carater
        if espaco == conta_espacos:
            ultimo_nome += carater
else:
    primeiro_nome = nome_completo

print(primeiro_nome.strip(), ultimo_nome.strip())