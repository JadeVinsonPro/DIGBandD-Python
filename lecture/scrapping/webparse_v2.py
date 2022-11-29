import requests
from bs4 import BeautifulSoup

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
        link_text = link.get('href')
        if link_text is not None:
            print('Variable is not None')
            print(link_text.split(','))
        else:
            print('Variable is None')
