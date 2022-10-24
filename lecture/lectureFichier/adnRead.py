#Compte le nombre de caractères
count = 0
compteurC = 0
compteurG = 0

#On parcourt le fichier texte
for i in (open("adn.txt").read()):
    #Compteur de la somme de caractères
    count = count + 1

    #Compteur du nombre de C
    if i == "C":
        compteurC = compteurC + 1

    #Compteur du nombre de G
    elif i == "G":
        compteurG =compteurG + 1

#Calcul du pourcentage parmi toute la ligne
pourcentageC = round((compteurC * 100) / count)
pourcentageG = round((compteurG * 100) / count)

print("Le fichier contient", count, "caractères.")

print("Nombres de C : ", compteurC, "\nSoit un pourcentage de :", pourcentageC)
print("Nombres de G : ", compteurG, "\nSoit un pourcentage de :", pourcentageG)

