
Tid10 = ["A", "C", "D"]
Tid20 = ["B", "C", "E"]
Tid30 = ["A", "B", "C", "E"]
Tid40 = ["B", "E"]

dico = {}

compteurTotal = 0
total = Tid10 + Tid20 + Tid30 + Tid40

for element in total:
    compteurTotal = compteurTotal + 1

#total.sort()
#print(total)
pourcentage = 20
#calcul supMin
supMin  = round((pourcentage/100) * compteurTotal)
supMin = int(supMin)
intermediare = []
compteur = 0
print(total)

dico = {}
#on met la liste dans un dictionnaire
for c in total:
    dico[c] = dico.get(c, 0) + 1


