# On ouvre le fichier en mode 'read' :
import re

fichier = open("bankaccount.txt", 'r')
# On lis le fichier :
contenu_du_fichier = fichier.readlines()

print(contenu_du_fichier)
fichierSepare = []
#Création d'une listeurlfile.txt pouyr chaque ligne clé/valeur
for mot in contenu_du_fichier:
    motSepare = mot.split("\t")
    fichierSepare.append(motSepare)


bbanComplet = []


codePays = input("Quel est le code pays ? (Ex : FR) ")
cleControle = int(input("Quel est la clée de contrôle ? (Ex : 14) "))
#on place les varibles dans leurs listes respectives
bbanComplet.append(codePays)
bbanComplet.append(cleControle)


#on met toutes les differentes parties du IBAN du fichier dans une seule liste
for x,y in fichierSepare:
    if x == "Code banque":
        bbanComplet.append(y)

    if x == "Code agence":
        bbanComplet.append(y)

    if x == "Numero de compte bancaire":
        bbanComplet.append(y)

    if x == "Chiffre d'indicatif national":
        bbanComplet.append(y)

#on met la longeur du bban dans une variable longueur
longueur = len(bbanComplet)
compteur = 0
#on parcourt la liste de bban et on supprime les retours à la ligne
while compteur > longueur:
    for i in bbanComplet:
        bbanComplet[compteur] = bbanComplet[compteur].replace('\n', "")
        compteur = compteur + 1


bbanComplet[2] = bbanComplet[2].replace('\n', "")
bbanComplet[3] = bbanComplet[3].replace('\n', "")
bbanComplet[4] = bbanComplet[4].replace('\n', "")


#suppression de tous les espaces
bbanComplet = ''.join([str(elem) for elem in bbanComplet ])


print("\n"
      "L'IBAN complet est \n", bbanComplet)

