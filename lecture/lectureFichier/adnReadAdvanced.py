#Compte le nombre de caractères
count = 0
compteurC = 0
compteurG = 0

j = 0
g = 0
i = 0
fichier = open("adn.txt").read()
print(fichier)
#On parcourt le fichier texte
fichier = open("adn.txt").read()
longueur = len(fichier)

for i in (fichier):
    #Compteur de la somme de caractères

    g = 0
    j = 0
    print("compteur", count)
    #Compteur du nombre de C
    if i == "C":
        j = count + 1
        #pas a la fin de la chaine de caracteres
        if j < longueur:
            if str(fichier[j]) == "G":
                compteurC = compteurC + 1
                print("ok")
                print(compteurC)
                i = i + 1

                #if j+1 < longueur:
                    #if str(fichier[j+1]) != "C":
                        #print("non")


    #Compteur du nombre de G
    if i == "G":
        g = count + 1
        #pas a la fin de la chaine de caracteres
        if g < longueur:
            if str(fichier[g]) == "C":
                compteurG = compteurG + 1
                print("compteur GC", compteurG)

    count = count + 1

    if count == longueur:
        break


#Calcul du pourcentage parmi toute la ligne
#pourcentageC = round((compteurC * 100) / count)
#pourcentageG = round((compteurG * 100) / count)
#pourcentageC = round((compteurCG * 100) / count)
#pourcentageG = round((compteurGC * 100) / count)

print("Le fichier contient", longueur, "caractères.")

#print("Nombres de C : ", compteurC)
#print("Nombres de G : ", compteurG)
print("Nombres de CG : ", compteurC, "\nSoit un pourcentage de :", )
print("Nombres de GC : ", compteurG, "\nSoit un pourcentage de :", )


