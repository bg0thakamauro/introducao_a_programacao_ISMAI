

import random
def alterarvogais(string):
    vogais = 'aeiou'
    for x1 in string:
        if x1.lower() == "a":
            novastring = random.choice(vogais.replace("a"," "))




n1 = input("insira a palavra")
n2 = alterarvogais(n1)
print(n2)