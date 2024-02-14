nomenormal = input("Insira o seu nome")

contaespaços = nomenormal.count(" ")

textofinal = ""

if(contaespaços > 0):
    i=0
    while i < len(textofinal):
        if i == 0 or nomenormal[i - 1] == " ":
            textofinal += nomenormal[i].upper()
        else:
            textofinal += nomenormal[i].lower()
        i += 1
else:
    textofinal = nomenormal.capitalize()

print(textofinal)

