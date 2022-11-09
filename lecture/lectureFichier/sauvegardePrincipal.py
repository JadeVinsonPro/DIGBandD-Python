#importation de la bibliotheque RE pour supprimer tous les espaces d'une chaîne de caractères
import re
#notice d'usage
print("Veuillez à entrer la bonne valeur car "
      "ce programme se chargera de mettre toute la chaîne de caractères en MAJUSCULES "
      "et supprimera tous les espaces. ")

#saisie de la chaîne et de la séquence uniquement en STRING
chaine = str(input("Entrez la chaîne : "))
sequence = str(input("Entrez la séquence : "))

#suppression de tous les espaces AVANT & APRES & DEDANS
chaine = re.sub("\s+","",chaine)

#mise de tous les caractères en minuscules
chaine = chaine.lower()

#comptage de la longueur de la chaîne de caractères rentrée soit le nombre de caractères de la chaîne
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

def saisie(chaine4):
    if valide(chaine4) == 1:
        proportion(chaine, sequence)
    else:
        return print("Chaîne invalide")

def proportion(chaine2, sequence2):
    compteur = 0

    compteur1 = 0
    compteur2 = 0
    compteur12 = 0
    compteur21 = 0
    premiereSequence = str(sequence2[0])
    deuxiemeSequence = str(sequence2[1])

    for i in chaine2:

        if i == premiereSequence:
            compteur1 = 1
            # si le compteur de G est à 1 et que la lettre précédent le C est un C alors
            if compteur2 == 1 and str(chaine2[compteur - 1]) == deuxiemeSequence:
                compteur21 = compteur21 + 1
                compteur1 = 0
                compteur2 = 0

        if i == deuxiemeSequence:
            compteur2 = 1
            # si le compteur de G est à 1 et que la lettre précédent le C est un C alors
            if compteur1 == 1 and str(chaine2[compteur - 1]) == premiereSequence:
                compteur12 = compteur12 + 1
                compteur1 = 0
                compteur2 = 0

        compteur = compteur + 1

    pourcentageSequence = round((compteur12 * 100) / longueur)

    return pourcentageSequence


pourcentageSequence = proportion(chaine, sequence)


print("La chaîne entrée : ", chaine, "\n")
print("La séquence entrée : ", sequence, "\n")
print("Il y a ", pourcentageSequence, "% de \"", sequence, "\" dans votre chaîne.")

