#Compte le nombre de caractères
count = 0
#Compte le nombre de caractères C
compteurC = 0
#Compte le nombre de caractères G
compteurG = 0
#Numéro d'enplacement du caractère sur la chaîne
g = 0
i = 0
fichier = open("adn.txt").read()
print(fichier)
longueur = len(fichier)
print(longueur)
#On parcourt le fichier texte
for i in (fichier):
    print(i)

    #Compteur de la somme de caractères
    print(str(fichier[count]))
    #Compteur du nombre de C
    if i == "C":
        g = count + 1
        if str(fichier[g]) == "G":
            print("ok")
            compteurC = +1
            print(compteurC)
            #if str(fichier[g+1]) == "C" + str(fichier[g+1]) == "C":
                #i = i + 1

    #Compteur du nombre de G
    if i == "G":
        g = count + 1
        print(str(fichier[g]))
        if str(fichier[g]) == "C":
            print("ok")
            compteurG = compteurG +1
            print(compteurG)

    count = count + 1
#Calcul du pourcentage parmi toute la ligne
#pourcentageC = round((compteurCG * 100) / count)
#pourcentageG = round((compteurGC * 100) / count)

print("Le fichier contient", count, "caractères.")

print("Nombres de CG : ", compteurC, "\nSoit un pourcentage de :", )
print("Nombres de GC : ", compteurG, "\nSoit un pourcentage de :", )

