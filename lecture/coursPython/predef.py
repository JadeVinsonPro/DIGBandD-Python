texte=["pomme","pain","pomme","orange","pomme","pain"]
lettres ={}
for c in texte:
    if c in lettres:
        lettres[c] = lettres[c] + 1#ou lettres[c]+=1
    else:
        lettres[c] = 1
for i in sorted(lettres):
    print(i,lettres.get(i))