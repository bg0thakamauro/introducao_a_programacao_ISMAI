n1 = float(input("Insira o dia da data 1"))
n2 = float(input("Insira o mes da data 1"))
n3 = float(input("Insira o ano da data 1"))

n4 = float(input("Insira o dia da data 2"))
n5 = float(input("Insira o mes da data 2"))
n6 = float(input("Insira o ano da data 2"))

if n6 == n3:
    if n2 == n5:
        if n1 == n4:
            print("as datas sao iguais")
        else:
            if n4 > n1:
                print("a 2 data é maior que a data 1")
            else:
                print("a 1 data é maior que a data 2")
    else:
        if n5 > n2:
            print("a 2 data é maior que a data 1")
        else:
            print("a 1 data é maior que a data 2")
else:
    if n6 > n3:
        print("a 2 data é maior que a data 1")
    else:
        print("a 1 data é maior que a data 2")