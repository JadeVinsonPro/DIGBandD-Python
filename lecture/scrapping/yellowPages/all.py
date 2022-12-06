import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, villes):
    # retrieving all the quote <div> HTML element on the page
    ville_elements = soup.find_all('a', class_='href')

    # iterating over the list of quote elements
    # to extract the data of interest and store it
    # in quotes
    for ville_element in ville_elements:
        # extracting the text of the quote
        nom = ville_element.find('a', class_='href').text

        villes.append(
            {
                'nom': nom,

            }
        )

# the url of the home page of the target website
base_url = 'https://www.yellowpages.com/sitemap'

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
villes = []

# scraping the home page
scrape_page(soup, villes)

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
    scrape_page(soup, villes)

    # looking for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')

# reading  the "quotes.csv" file and creating it
# if not present
csv_file = open('quote.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['Nom'])

# writing each row of the CSV
for ville in villes:
    writer.writerow(ville.values())

# terminating the operation and releasing the resources
csv_file.close()