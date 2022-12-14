import requests
from bs4 import BeautifulSoup
import pandas as pd



# liste de tÃ©lÃ©phone
tel_list = {""};

# exemple d'URL
urls = ['https://www.bcge.ch/', 'https://www.creageneve.com/', 'https://www.hsbc.ch/', 'https://wow-consulting.fr/',
            'https://www.unige.ch/', 'https://www.epfl.ch/fr/', 'https://ethz.ch/en.html/',
            'https://ecole.grandeecole.inseec.com/']


#html_text = requests.get(crea_url).text
#soup = BeautifulSoup(html_text, 'html.parser')


#title = soup.find('title').text
#print(title)


for line in open("../../../../Downloads/listeurlfile.txt").readlines():
    html_text = requests.get(line).text
    soup = BeautifulSoup(html_text, 'html.parser')
    title = soup.find('title')
    print(title)

    for link in soup.find_all('a'):
        print("lin",link)
        link_text = link.get('href')
        if link_text is not None:
            print('Variable is not None')
            print(link_text.split(','))
        else:
            print('Variable is None')

    for numero in soup.find_all('numero'):
        link_text = numero.get('')

numero = "+33 6 10 20 30 10"

regex = "(0|\\+33|0033)[1-9][0-9]{8}"

if re.match(regexp, numero) is not None:

    print("Numero valide")

else:

    print("Numero invalide")