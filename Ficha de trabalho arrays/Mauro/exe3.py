valor_procurado = int(input("Digite o valor que deseja procurar (entre 1 e 20): "))
if 1 <= valor_procurado <= 20:
    try:
        posicao = list(range(1, 21)).index(valor_procurado) + 1
        print(f"O valor {valor_procurado} existe na posição {posicao}.")
    except ValueError:
        print(f"O valor {valor_procurado} não existe no vetor.")
else:
    print("Valor inválido. O valor deve estar entre 1 e 20.")
