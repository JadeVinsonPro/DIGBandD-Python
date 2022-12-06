import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
page = requests.get('https://quotes.toscrape.com', headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

quotes = []
quote_elements = soup.find_all('div', class_='quote')

print(quote_elements)

for quote_element in quote_elements:
    # extracting the text of the quote
    text = quote_element.find('span', class_='text').text
    # extracting the author of the quote
    author = quote_element.find('small', class_='author').text

    # extracting the tag <a> HTML elements related to the quote
    tag_elements = quote_element.find('div', class_='tags').find_all('a', class_='tag')

    # storing the list of tag strings in a list
    tags = []
    for tag_element in tag_elements:
        tags.append(tag_element.text)

print(tag_element)

quotes.append(
    {
        'text': text,
        'author': author,
        'tags': ', '.join(tags) # merging the tags into a "A, B, ..., Z" string
    }
)

# the url of the home page of the target website
base_url = 'https://quotes.toscrape.com'

# retrieving the page and initializing soup...

# getting the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

# if there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # getting the new page
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parsing the new page
    soup = BeautifulSoup(page.text, 'html.parser')

    # scraping logic...

    # looking for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')