#mettre dans des tableaux chaque listeurlfile.txt

Tid10 = 0
Tid20 = 0
dico = {}
dico["Tid10"] = ["A", "C", "D"]
dico["Tid20"] = ["B", "C", "E"]
dico["Tid40"] = ["B", "E"]
dico["Tid30"] = ["A", "B", "J", "E", "J"]


print(dico)
print(str(dico.keys())," sont des clés")
print(str(dico.values())," sont des valeurs")


for i in dico:
    for f in dico.values():
        print("jade")

for f in dico.values():
    print(f)

t = []
print(sorted(dico.values()))
for i in sorted(dico.values()):
    print(i)
    t.append(i)

print(t)
print(len(t))
print(len(dico.values()))