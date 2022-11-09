#Parcourir un tableau
Tid10 = ["A", "C", "D"]
for element in Tid10:
    print(element)

#lecture d'un tableau et on ne reprend que les éléments au-dessus de 10
l = [1,10,5,7,12]
monTab = [p for p in l if p > 10]
#print(monTab)
#[12]

#lecture d'un tableau et on ne reprend que les éléments au-dessus de 10
# et met ceux séléctionnés au carré
l = [1,10,5,7,12,15]
monTab = [p*3 for p in l if p > 10]
#print(monTab)
#[36, 45]

#tableau de tableau

#position précise
m = [[1,2,3],
    [5,6,7],
     [8,9,10],
     [18,20]]

f = m[1][2], m[2]
#print(f)
#7
#(7, [8, 9, 10])

#meme tableau dans tableau
m = [1,2,3]
mm = [m, m , m]

#print(m[0])1
#print(mm)[[1, 2, 3], [1, 2, 3], [1, 2, 3]]


n = [[1,2,3],
    [5,6,7],
     [8,9,10],
     [18,20,30]]
nb_ligne = 0
nb_colonne = 0
#calcul nombre de ligne
for element in n:
    nb_ligne = nb_ligne + 1
    for colonne in n:
        nb_colonne = nb_colonne + 1


print("ligne",nb_ligne)
print("colonne",nb_colonne)


for i in range(0, nb_ligne):
    for j in range(0, nb_colonne):
        a = n[i][j]
        print(a)