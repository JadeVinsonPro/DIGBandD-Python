#mettre dans des tableaux chaque liste

Tid10 = 0
dico = {}
Tid10 = ["A", "C", "D"]
Tid20 = ["B", "C", "E"]
Tid30 = ["A", "B", "C", "E"]
Tid40 = ["B", "E"]

print(dico)
compteurTotal = 0
total = Tid10 + Tid20 + Tid30 + Tid40

for element in total:
    compteurTotal = compteurTotal + 1

total.sort()
print(total)
pourcentage = 20
#calcul supMin
supMin  = round((pourcentage/100) * compteurTotal)

compteurA = 0
compteurB = 0
compteurC = 0
compteurD = 0
compteurE = 0

for i in total:
    if i == "A":
        compteurA = compteurA + 1

l = [1,10,5,7,12]
monTab = [p for p in l if p > 10]

print("Il y a en tout : ",compteurTotal)
print("Support minimum de :",supMin)