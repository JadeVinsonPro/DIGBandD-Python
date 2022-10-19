# Write a Python program that computes the factorial of an integer #

#Consigne
print("Calcul des facteurs d'un nombre")
#Déclaration de la variable
a = int(input("Entrez un numéro dont vous souhaitez connaître tous les facteurs : "))
b = 0


#Tant que a supérieur à b
while a > b:
    b = b + 1
    #Si le modulo est égal à 0, on affiche le diviseur
    if a%b == 0:
        print(b)

