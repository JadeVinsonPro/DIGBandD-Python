
listAvecPonctuation = []
listAvecPonctuation = ["Ceci est un phrase."]
listFinal = []

i = 0
while i < len(listAvecPonctuation):
    moTemp = ""
    while i < len(listAvecPonctuation) and listAvecPonctuation[i] != " " and listAvecPonctuation[i] != "." and \
            listAvecPonctuation[i] != "!" and listAvecPonctuation[i] != "?" and listAvecPonctuation[i] != ";" and \
            listAvecPonctuation[i] != ",":
        moTemp = moTemp + listAvecPonctuation[i]
        i = i + 1
    listFinal.append(moTemp)
    i = i + 1


print(moTemp)