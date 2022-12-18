# On ouvre le fichier en mode 'read' :
import re

fichier = open("bankaccount.txt", 'r')
# On lis le fichier :
contenu_du_fichier = fichier.readlines()

print("Le contenu du fichier est", contenu_du_fichier)
fichierSepare = []
#Création d'une listeurlfile.txt pouyr chaque ligne clé/valeur
for mot in contenu_du_fichier:
    motSepare = mot.split("\t")
    fichierSepare.append(motSepare)


bbanComplet = []

codePays = input("Quel est le code pays ? (Ex : FR) ")


for x,y in fichierSepare:
    if x == "Code banque":
        bbanComplet.append(y)

    if x == "Code agence":
        bbanComplet.append(y)

    if x == "Numero de compte bancaire":
        bbanComplet.append(y)

    if x == "Chiffre d'indicatif national":
        bbanComplet.append(y)

#on ajoute le code pays au bban
bbanComplet.append(codePays)
longueur = len(bbanComplet)
compteur = 0

#on parcourt la liste de bban et on supprime les retours à la ligne
while compteur > longueur:
    for i in bbanComplet:
        bbanComplet[compteur] = bbanComplet[compteur].replace('\n', "")
        compteur = compteur + 1

bbanComplet[0] = bbanComplet[0].replace('\n', "")
bbanComplet[1] = bbanComplet[1].replace('\n', "")
bbanComplet[2] = bbanComplet[2].replace('\n', "")


bbanComplet = ''.join([str(elem) for elem in bbanComplet ])
# Afficher la listeurlfile.txt



print("\n"
      "L'IBAN complet sans la clé de contrôle est \n", bbanComplet)

compteurB = 0
bbanComplet = list(bbanComplet)
for i in bbanComplet:
#toutes les
    if not i.isdigit():
        bbanComplet[compteurB] = ord(bbanComplet[compteurB]) - 55
        bbanComplet[compteurB] = int(bbanComplet[compteurB])
    bbanComplet[compteurB] = int(bbanComplet[compteurB])
    compteurB = compteurB + 1
#on transforme en chaine de caracteres


bban = []
compteur = 0
for i in bbanComplet:
    bban.append(str(bbanComplet[compteur]))
    compteur = compteur + 1

verif = 98 - (bbanComplet % 97)


print("La clé est :",verif, "et la suite", bbanComplet)