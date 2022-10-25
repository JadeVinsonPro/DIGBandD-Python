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
for i in (fichier):
    #Compteur de la somme de caractères

    j = 0
    print(str(fichier[count]))
    #Compteur du nombre de C
    if i == "C":
        j = count + 1
        if str(fichier[g]) == "G":
            compteurC = +1
            print(compteurC)


    #Compteur du nombre de G
    if i == "G":
        g = count + 1
        print(str((fichier[g])))
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

