import requests
from bs4 import BeautifulSoup
from urlparse import urljoin


def get_data(url, base):
    response = requests.get(url)

    soup = BeautifulSoup(response.content)

    for listing in soup.find_all('p', 'row'):
        if listing.find('span', 'price') is not None:
            price = listing.text[2:6]
            price = int(price)
            if price <= 250 and price > 100:
                print listing.text
                linkend = listing.a['href']
                url = urljoin(base, linkend)
                print url
                print "\n"


url = 'http://philadelphia.craigslist.org/search/sss?sort=date&query=firefly%20tickets'
base = 'http://philadelphia.craigslist.org/cpg/'

get_data(url, base)
