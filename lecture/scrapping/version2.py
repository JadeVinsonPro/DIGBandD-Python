import requests
from bs4 import BeautifulSoup

#listeurlfile.txt de tÃ©lÃ©phone

def parse_url_getphones(line_url):
    tel_list = {""};
    html_text = requests.get(line_url).text
    # affichage du contenu html
    #print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    # rÃ©cupÃ©ration de titre
    title = soup.find('title')
    # affichage du titre
    print(title)
    # parcours des urls
    for link in soup.find_all('a'):
        link_text = link.get('href')
        #print(link_text)
        link_list = link_text.split(":")
        if (link_list[0] == "tel"):
            tel_list.add(link_list[1])
    # affichage des numÃ©ros de tÃ©lÃ©phones extraitss
    for s in tel_list:
        print(s)
    return tel_list

tel_list_final = {""}
for line_url in open("listeurlfile.txt").readlines():
    # recupÃ©ration du contenu html d'un site Ã  partir de l'url
    tel_list = parse_url_getphones(line_url)
    if len(tel_list) >=1:
        for s in tel_list :
            tel_list_final.add(s)
print(tel_list_final)