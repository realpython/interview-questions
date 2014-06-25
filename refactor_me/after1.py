import requests
from bs4 import BeautifulSoup
from urlparse import urljoin


def get_data(url, base):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    for listing in soup.find_all('p', 'row'):
        if listing.find('span', 'price'):
            price = int(listing.text[2:6])
            if  100 < price <= 250:
                print listing.text
                print urljoin(base, listing.a['href'])
                print '\n'



url = 'http://philadelphia.craigslist.org/search/sss?sort=date&query=firefly%20tickets'
base = 'http://philadelphia.craigslist.org/cpg/'

get_data(url, base)
