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
dico = {}

for mot in fichierSepare:
    print(mot)
    for i in mot:
        print(i)
        if i =="Numero de compte bancaire":
            ban = {i in mot}
            print(ban)

        #dico.append(i[0],i[1])
    #dico[mot] = dico.get(mot, 0) + 1

print(dico)