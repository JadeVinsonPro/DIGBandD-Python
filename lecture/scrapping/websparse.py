import requests
from bs4 import BeautifulSoup

#listeurlfile.txt de tÃ©lÃ©phone
tel_list = {""}

#exemple d'URL
crea_url = 'https://www.creageneve.com/'

#recupÃ©ration du contenu html d'un site Ã  partir de l'url
html_text = requests.get(crea_url).text
#affichage du contenu html
#print(html_text)
soup = BeautifulSoup(html_text, 'html.parser')

#rÃ©cupÃ©ration de titre
title = soup.find('title').text
#affichage du titre
print(title)

#rÃ©cupÃ©ration de body
#body = soup.find('body').text
#affichage du body
#print(body)

#parcours des urls
for link in soup.find_all('a'):
    link_text = link.get('href')
    print(link_text)
    link_list = link_text.split(":")
    if(link_list[0] == "tel"):
        tel_list.add(link_list[1])

#affichage des numÃ©ros de tÃ©lÃ©phones extraitss
for s in tel_list:
    print(s)