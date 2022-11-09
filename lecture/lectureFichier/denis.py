#saisie = input("Saisir la chaîne : ")
import re

print("Veuillez à entrer la bonne valeur car "
      "ce programme se chargera de mettre toute la chaîne de caractères en MAJUSCULES "
      "et supprimera tous les espaces. ")
saisie = "cg cg"
#suppression de tous les espaces AVANT & APRES & DEDANS
saisie = re.sub("\s+","",saisie)
#mise de tous les caractères en MAJUSCULES
saisie = saisie.upper()

compteur = 0

compteurC = 0
compteurG = 0
compteurCG = 0
compteurGC = 0

longueur = len(saisie)

for i in saisie:

    if i == "C":
        compteurC = 1
        #si le compteur de G est à 1 et que la lettre précédent le C est un C alors
        if compteurG == 1 and str(saisie[compteur - 1]) == "G":
            compteurGC = compteurGC + 1
            compteurC = 0
            compteurG = 0

    if i == "G":
        compteurG = 1
        #si le compteur de C est à 1 et que la lettre précédent le G est un C alors
        if compteurC == 1 and str(saisie[compteur - 1]) == "C":
            compteurCG = compteurCG + 1
            compteurC = 0
            compteurG = 0

    compteur = compteur + 1


print('La chaîne etudiée par la fonction est', saisie,".")
print("Elle contient", longueur, "caractères.")
print("Nombre de couples CG : ", compteurCG)
print("Nombre de couples GC : ", compteurGC)