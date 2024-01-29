n1 = int(input("Insira a idade"))

if(n1 < 0):
    print("Invalido")
elif(n1 <12 and n1 >= 0):
    print("infancia")
elif(n1 > 13 and n1 <17):
    print("adolescencia")
elif(n1 > 18 and n1 <59):
    print("Adulto")
elif(n1 > 60):
    print("idoso")