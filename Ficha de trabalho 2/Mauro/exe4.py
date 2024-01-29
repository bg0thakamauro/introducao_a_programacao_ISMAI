ano = int(input("Insira o ano"))

if(ano % 4 == 0):
    if(ano % 100 == 0):
        if(ano % 400 == 0):
            print("é bisexto")
        else:
            print("nao é bisexto")
    else:
            print("é bisexto")

else:
    print("nao é bisexto")

    