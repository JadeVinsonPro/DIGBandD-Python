import re

import regexp as regexp

numero = "+33 6 10 20 30 10"

numero = "+33610203010"

regex = "(0|\\+33|0033)[1-9][0-9]{8}"

if re.match(regex, numero) is not None:

    print("Numero valide")

else:

    print("Numero invalide")