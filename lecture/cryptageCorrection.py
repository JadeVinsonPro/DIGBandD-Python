# Crypter un mot
d = input("Saisir le texte : ")
rar = ""
d = str.lower(d)
for c in d:
    if c == "z":
        nov = 'a'
    else:
        x = ord(c)+1
        nov = chr(x)
    rar = rar+nov
    print(rar)

print(rar)