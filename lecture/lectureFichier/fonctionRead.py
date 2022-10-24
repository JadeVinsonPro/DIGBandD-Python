#Compte le nombre de caractères
count = 0
for line in (open("adn.txt").read()):
    count = count + 1
print("The file contains", count, "caracters.")

#Compte le nombre de lignes
count = 0
for line in (open("adn.txt").readlines()):
    count = count + 1
print("The file contains", count, "lines.")
