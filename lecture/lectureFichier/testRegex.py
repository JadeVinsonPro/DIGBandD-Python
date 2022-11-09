import re

chaine = "aicc"
#----------
chaineVerif = r'\b[atcg]'

if (re.match(chaineVerif, chaine)):
    print("chaine ok")
else:
    print("chaine invalide")

