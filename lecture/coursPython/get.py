texte=["pomme","pain","pomme","orange","pomme"
,"pain"]
lettres ={}
for c in texte:
    lettres[c] = lettres.get(c, 0) + 1
for i in sorted(lettres):
    print(i,lettres.get(i))