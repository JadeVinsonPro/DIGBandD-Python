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


codePays = input("Quel est le code pays ? ")
cleControle = int(input("Quel est la clée de contrôle ? "))
bbanComplet.append(codePays)
bbanComplet.append(cleControle)
print(bbanComplet)

for x,y in fichierSepare:
    if x == "Code banque":
        print("code",y)
        bbanComplet.append(y)

    if x == "Code agence":
        print("code",y)
        bbanComplet.append(y)

    if x == "Numero de compte bancaire":
        print("code",y)
        bbanComplet.append(y)

    if x == "Chiffre d'indicatif national":
        print("code",y)
        bbanComplet.append(y)

longueur = len(bbanComplet)
compteur = 0
while compteur > longueur:
    for i in bbanComplet:
        bbanComplet[compteur] = bbanComplet[compteur].replace('\n', "")
        compteur = compteur + 1
print("fin",bbanComplet)

bbanComplet[2] = bbanComplet[2].replace('\n', "")
bbanComplet[3] = bbanComplet[3].replace('\n', "")
bbanComplet[4] = bbanComplet[4].replace('\n', "")
print(bbanComplet)

bbanComplet = ''.join([str(elem) for elem in bbanComplet ])
# Afficher la listeurlfile.txt
print(bbanComplet)


print("\n"
      "L'IBAN complet est \n", bbanComplet)

