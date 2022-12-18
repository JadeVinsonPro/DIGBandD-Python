IBAN = "20041010050500013M02606FR00"



list1 = list(IBAN)
print(IBAN)
list2 = ""
print(type(list1))
for i in range(0, len(list1), 1):
    if not list1[i].isdigit():
        list1[i] = ord(list1[i]) - 55

for i in range(0, len(list1), 1):
    list2 += str(list1[i])
print(list2)
x = int(list2)
print(x)

#et apres tu mets FR + la clé IBAN + le code que t'as recupéré
verif = 98 - (x % 97)
print(verif)