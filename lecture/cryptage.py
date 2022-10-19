#Write a program that performs a rotation cypher

mot = str(input("Entrez un mot que vous souhaitez crypter : "))
long = len(mot)
i = 0
resultat = 0
liste = list(str.strip(mot))
print(liste)

while i < long:
    a = liste[i]
    chiffre = ord(a)
    code = chiffre + 1
    traduction = chr(code)
    resultat.append(traduction)
    i = i + 1
    print(resultat)

print(chiffre)