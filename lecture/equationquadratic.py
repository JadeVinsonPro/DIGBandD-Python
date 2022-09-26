from math import *
import math

print("Résolution d'une équation du second degré")

a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))

discriminant = b^2 - (4*a*c)
print("Le discriminant est de ", discriminant,".")

if discriminant > 0:
    resultat1 = (-b+sqrt(b^2-4*a*c)/2*a)
    resultat2 = (-b-sqrt(b^2-4*a*c)/2*a)
    print("Il existe 2 solutions. Les résultats sont ", resultat1, " et ", resultat2,".")

elif discriminant < 0:
    print("Le discriminant est négatif. Il n'existe aucune solution.")

elif discriminant == 0:
    resultat = -(b/2*a)
    print("Il n'exite qu'une seule solution. Le résultat est ", resultat,".")

else:
    print("ERREUR.")


