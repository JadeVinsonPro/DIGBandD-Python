# On ouvre le fichier en mode 'read' :
fichier = open("bankaccount.txt", 'r')
# On lis le fichier :
contenu_du_fichier = fichier.readlines()

print(contenu_du_fichier)
fichierSepare = []
for mot in contenu_du_fichier:
    motSepare = mot.split("\t")
    print(motSepare)
    fichierSepare.append(motSepare)


print(motSepare)
print(fichierSepare)
