import requests
from bs4 import BeautifulSoup
import csv


def scrape_quotes(url):
    # get the HTML
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # locate element containing all quotes
        quotes = soup.find_all('div', class_='quote')

        # prepare to store data in a csv file
        data = []

        # loop through each quote and get the quote, author and tags
        for quote in quotes:
            quote_text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags_list = quote.find('div', class_='tags').find_all('a', class_='tag')
            tags = [tag.text for tag in tags_list]
            data.append([quote_text, author, ', '.join(tags)])

        return data
    else:
        print(f"Error could not get the page{url}")


def main():
    url = 'http://quotes.toscrape.com/'
    data = scrape_quotes(url)

    # scrape all pages
    for page in range(2, 11):
        data += scrape_quotes(f'{url}page/{page}/')

    # save data in a csv file
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Quote', 'Author', 'Tags'])
        writer.writerows(data)


if __name__ == '__main__':
    main()
