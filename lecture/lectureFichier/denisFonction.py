#saisie = input("Saisir la chaîne : ")
import re
import string

saisie = "AT GC TC TA"
#saisie = ''.join([i for i in string if not i.isdigit()])
# suppression de tous les espaces AVANT & APRES & DEDANS
saisie = re.sub("\s+", "", saisie)
# mise de tous les caractères en MAJUSCULES
saisie = saisie.upper()

longueur = len(saisie)

#condition si autre caractere que C, G, A, et T
def valide(saisie):
    print("Veuillez à entrer la bonne valeur car "
          "ce programme se chargera de mettre toute la chaîne de caractères en MAJUSCULES "
          "et supprimera tous les espaces. ")

    compteur = 0

    compteurC = 0
    compteurG = 0
    compteurCG = 0
    compteurGC = 0

    compteurA= 0
    compteurT = 0
    compteurAT = 0
    compteurTA = 0

    for i in saisie:

        if i == "C":
            compteurC = 1
            #si le compteur de G est à 1 et que la lettre précédent le C est un C alors
            if compteurG == 1 and str(saisie[compteur - 1]) == "G":
                compteurCG = compteurCG + 1
                compteurC = 0
                compteurG = 0

        if i == "G":
            compteurG = 1
            #si le compteur de C est à 1 et que la lettre précédent le G est un C alors
            if compteurC == 1 and str(saisie[compteur - 1]) == "C":
                compteurGC = compteurGC + 1
                compteurC = 0
                compteurG = 0

        if i == "A":
            compteurA = 1
            # si le compteur de G est à 1 et que la lettre précédent le C est un C alors
            if compteurT == 1 and str(saisie[compteur - 1]) == "T":
                compteurAG = compteurAT + 1
                compteurA = 0
                compteurT = 0

        if i == "T":
            compteurT = 1
            # si le compteur de C est à 1 et que la lettre précédent le G est un C alors
            if compteurA == 1 and str(saisie[compteur - 1]) == "A":
                compteurTA = compteurGC + 1
                compteurA = 0
                compteurT = 0

        compteur = compteur + 1

    print("Nombre de couples CG : ", compteurCG)
    print("Nombre de couples GC : ", compteurGC)
    print("Nombre de couples AT : ", compteurAT)
    print("Nombre de couples TA : ", compteurTA)


    if compteurCG >=1 or compteurGC >=1 or compteurAT >=1 or compteurTA >=1:
        return "vraie"
    else:
        return "faux"

def saisieF(saisie):
    valide(saisie)
print(valide(saisie))
print('La chaîne etudiée par la fonction est', saisie,".")
print("Elle contient", longueur, "caractères.")
#print("Nombre de couples CG : ", compteurCG)
#print("Nombre de couples GC : ", compteurGC)
#print(compteurGC)