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
print("fin",bbanComplet)

bbanComplet[0] = bbanComplet[0].replace('\n', "")
bbanComplet[1] = bbanComplet[1].replace('\n', "")
bbanComplet[2] = bbanComplet[2].replace('\n', "")

print(bbanComplet)

bbanComplet = ''.join([str(elem) for elem in bbanComplet ])
# Afficher la listeurlfile.txt
print(bbanComplet)


print("\n"
      "L'IBAN complet sans la clé de contrôle est \n", bbanComplet)

print(bbanComplet)
compteurB = 0
for i in bbanComplet:
    if not bbanComplet[compteurB].isdigit():
        bbanComplet[compteurB] = ord(bbanComplet[compteurB]) - 55
    compteurB = compteurB + 1
#on transforme en chaine de caracteres
print(bbanComplet)
#resutat = bbanComplet/97
#print(resutat)
compteur = 0
#sélection des 9 premiers
neuf =[]

for i in bbanComplet:
    neuf.append(i)


print(neuf)
print(len(neuf))


sansM = neuf
del sansM[17]
print(sansM)

if sansM-97 == 0:
    print("ok")

