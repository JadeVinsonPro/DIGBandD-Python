#chaine = str(input("Entrez la chaîne : "))
#sequence = str(input("Entrez la séquence : "))
import re

chaine = "catderf"
sequence = "ca"

#suppression de tous les espaces AVANT & APRES & DEDANS
chaine = re.sub("\s+","",chaine)
#mise de tous les caractères en minuscules
chaine = chaine.lower()

longueur = len(chaine)

def valide(chaine3):

    for i in chaine3:

        compteur = 0

        compteurC = 0
        compteurG = 0
        compteurCG = 0
        compteurGC = 0

        compteurA = 0
        compteurT = 0
        compteurAT = 0
        compteurTA = 0

        for i in chaine3:

            if i == "c":
                compteurC = 1
                # si le compteur de G est à 1 et que la lettre précédent le C est un C alors
                if compteurG == 1 and str(chaine3[compteur - 1]) == "g":
                    compteurCG = compteurCG + 1
                    compteurC = 0
                    compteurG = 0

            if i == "g":
                compteurG = 1
                # si le compteur de C est à 1 et que la lettre précédent le G est un C alors
                if compteurC == 1 and str(chaine3[compteur - 1]) == "c":
                    compteurGC = compteurGC + 1
                    compteurC = 0
                    compteurG = 0

            if i == "a":
                compteurA = 1
                # si le compteur de G est à 1 et que la lettre précédent le C est un C alors
                if compteurT == 1 and str(chaine3[compteur - 1]) == "t":
                    compteurAT = compteurAT + 1
                    compteurA = 0
                    compteurT = 0

            if i == "t":
                compteurT = 1
                # si le compteur de C est à 1 et que la lettre précédent le G est un C alors
                if compteurA == 1 and str(chaine3[compteur - 1]) == "a":
                    compteurTA = compteurGC + 1
                    compteurA = 0
                    compteurT = 0

            compteur = compteur + 1

    if compteurCG >= 1 or compteurGC >= 1 or compteurAT >= 1 or compteurTA >= 1:
        return 1
    else:
        return 0


if valide(chaine) == 1:
    print("La saisie est valide.")
else:
    print("La saisie est fausse.")