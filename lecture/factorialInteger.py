# Write a Python program that computes the factorial of an integer #

#SI NEGATIVE faire un blindage de caractere
print("Calcul du factorielle d'un nombre")
#Déclaration de la variable
a = int(input("Entrez un numéro dont vous souhaitez connaître la factorielle : "))

#Initialisation de la somme à 1
somme = 1

#Calcul de factoriel si le nombre entré est positif
if a > 0:
    for x in range(a, 0, -1):
        somme = somme * x
    print(a,"! =",somme)

#Calcul de factoriel si le nombre entré est égal à 1
elif a == 1:
    print("1! = 1")

#Calcul de factoriel si le nombre entré est égal à 0
elif a == 0:
    print("0! = 1")

#Calcul de factoriel si le nombre entré est négatif
elif a < 0:
    print("Calcul impossible. Veuillez entrer un nombre entier.")

#ERREUR
else:
    print("ERROR")



