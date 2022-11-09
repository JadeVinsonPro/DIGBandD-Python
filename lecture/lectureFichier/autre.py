import re

#chaine = input("chaine :")
#longueur = len(chaine)
sequence = "jade"
longueurSequence = len(sequence)

compteurHorsADNSequence = 0

for i in sequence:
    # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
    # on ajoute 1 au compteur
    if i not in ("a", "t", "g", "c"):
        compteurHorsADNSequence = compteurHorsADNSequence + 1



while compteurHorsADNSequence != 0:
    sequence = input("\nSéquence invalide.\n"
                     "La séquence doit contenir strictement 2 caractères et être composée que des caractères \"a\", \"t\", \"g\" et/ou \"c\".\n"
                     "Veuillez entrer une séquence valide : ")
    compteurHorsADNSequence = 0
    for i in sequence:
        # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
        # on ajoute 1 au compteur
        if i not in ("a", "t", "g", "c"):
            compteurHorsADNSequence = compteurHorsADNSequence + 1

    longueurSequence = len(sequence)
    compteurHorsADNSequence = compteurHorsADNSequence
    while longueurSequence != 2:
        if longueurSequence <= 1:
            sequence = input("\nSéquence trop courte.\n"
                             "La séquence doit contenir strictement 2 caractères.\n"
                             "Veuillez entrer une séquence avec uniquement 2 caractères : ")
            compteurHorsADNSequence = 0
            for i in sequence:
            # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
            # on ajoute 1 au compteur
                if i not in ("a", "t", "g", "c"):
                    compteurHorsADNSequence = compteurHorsADNSequence + 1
            longueurSequence = len(sequence)

        elif longueurSequence > 2:
            sequence = input("\nSéquence trop longue.\n"
                             "La séquence doit contenir strictement 2 caractères.\n"
                             "Veuillez entrer une séquence plus courte : ")
            compteurHorsADNSequence = 0
            for i in sequence:
                # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
                # on ajoute 1 au compteur
                if i not in ("a", "t", "g", "c"):
                    compteurHorsADNSequence = compteurHorsADNSequence + 1
            longueurSequence = len(sequence)

        compteurHorsADNSequence = compteurHorsADNSequence
        sequence = re.sub("\s+", "", sequence)
        sequence = sequence.lower()
        longueurSequence = len(sequence)

