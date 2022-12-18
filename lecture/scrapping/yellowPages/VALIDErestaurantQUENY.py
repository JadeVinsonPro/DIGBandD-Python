import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    # retrieving all the quote <div> HTML element on the page
    quote_elements = soup.find_all('div', class_='info')
    informations_elements = soup.find_all('div', class_='info-section info-secondary')

    # iterating over the list of quote elements
    # to extract the data of interest and store it
    # in quotes
    for quote_element in quote_elements:

        #numero = quote_element.find('h2', class_='n').text
        nom = quote_element.find('span').text
        tag_elements = quote_element.find('div', class_='categories').find_all('a')
        adresse = quote_element.find('div', class_='street-address')
        if adresse is not None:
            a = adresse.text

        ville = quote_element.find('div', class_='locality')
        if ville is not None:
            v = ville.text

        lien = quote_element.find('a', 'href')
        #recuperer tous les liens de la page
        #for a_href in quote_element.find_all("a", href=True):
            #print(a_href["href"])

        tel = quote_element.find('div', class_="phones phone primary")
        if tel is not None:
            x = tel.text


        # storing the list of tag strings in a list
        tags = []
        for tag_element in tag_elements:
            tags.append(tag_element.text)

        # appending a dictionary containing the quote data
        # in a new format in the quote list
        quotes.append(
            {
                #'numero': numero,

                'nom': nom,
                'tags': ', '.join(tags),# merging the tags into a "A, B, ..., Z" string
                'adresse': a,
                'ville': v,
                'lien': lien,
                'phones phone primary': x

            }
        )

# the url of the home page of the target website
base_url = 'https://www.yellowpages.com/new-york-ny/restaurants'

# defining the User-Agent header to use in the GET request below
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

# parsing the target web page with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

# initializing the variable that will contain
# the list of all quote data
quotes = []

# scraping the home page
scrape_page(soup, quotes)

# getting the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

# if there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # getting the new page
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parsing the new page
    soup = BeautifulSoup(page.text, 'html.parser')

    # scraping the new page
    scrape_page(soup, quotes)

    # looking for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')

# reading  the "quotes.csv" file and creating it
# if not present
csv_file = open('NYRestaurant.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['Nom du restaurant', 'Tags', 'Adresse', 'Ville', 'Site', 'Numéro de tél'])

# writing each row of the CSV
for quote in quotes:
    writer.writerow(quote.values())

# terminating the operation and releasing the resources
csv_file.close()