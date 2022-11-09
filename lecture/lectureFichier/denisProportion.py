#chaine = str(input("Entrez la chaîne : "))
sequence = str(input("Entrez la séquence : "))
import re

chaine = "cacgt"
#suppression de tous les espaces AVANT & APRES & DEDANS
chaine = re.sub("\s+","",chaine)
#mise de tous les caractères en minuscules
chaine = chaine.lower()

compteur = 0

compteur1 = 0
compteur2 = 0

premiereSequence = str(sequence[0])
deuxiemeSequence = str(sequence[1])

compteur12 = 0
compteur21 = 0

longueur = len(chaine)


for i in chaine:

    if i == premiereSequence:
        compteur1 = 1
        #si le compteur de G est à 1 et que la lettre précédent le C est un C alors
        if compteur2 == 1 and str(chaine[compteur - 1]) == deuxiemeSequence:
            compteur21 = compteur21 + 1
            compteur1 = 0
            compteur2 = 0

    if i == deuxiemeSequence:
        compteur2 = 1
        #si le compteur de G est à 1 et que la lettre précédent le C est un C alors
        if compteur1 == 1 and str(chaine[compteur - 1]) == premiereSequence:
            compteur12 = compteur12 + 1
            compteur1 = 0
            compteur2 = 0

    compteur = compteur + 1


#def proportion(sequence):
    #if sequence == "ca":

pourcentageSequence = round((compteur12 * 100) / longueur)
print("La chaîne entrée : ", chaine, "\n")
print("La séquence entrée : ", sequence, "\n")
print("Il y a ", compteur12,"occurences.")
print("Il y a ", pourcentageSequence, "% de \"", sequence,"\" dans votre chaîne.")