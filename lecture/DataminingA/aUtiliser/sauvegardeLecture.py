# importing csv module
import csv

# csv file name
filename = "databaseTDB.csv"

# initializing the titles and rows list
fields = []
rows = []
listeTotale = []
dico = {}

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    #reader = csv.reader(csvfile)


    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    dico = {rows[0]: rows[1] for rows in csvreader}
    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nBienvenue sur l\'algorithme Apriori:\n')

#pourcentage = int(input("Veuillez entrer votre support minimum en pourcentage"))

compteurTotal = 0

#parcourt du tableau pour connaitre le nombre d'elements
for row in rows:
    # parsing each column of a row
    for col in row:
        compteurTotal = compteurTotal + 1
        print("col:",col)
        listeTotale.append(col)


    print(compteurTotal)

#calcul supMin
#supMin  = round((pourcentage/100) * compteurTotal)

#on met la liste dans un dictionnaire
for c in listeTotale:
    dico[c] = dico.get(c, 0) + 1

for i in sorted(dico):
    print(i,dico.get(i))

print(listeTotale)
print("dico")
print(dico)


delete = []
#on supprime les elements qui on un support inferieur à celui mis
for k,v in dico.items():
    if v < 2:
        delete.append(k)
for i in delete:
    del dico[i]

print(dico)

for k,v in dico.items():
    if v < 2:
        delete.append(k)
for i in delete:
    del dico[i]


