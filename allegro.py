import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser

DEFAULT_OAUTH_URL = 'https://allegro.pl/auth/oauth'


import requests
from bs4 import BeautifulSoup
import pprint

URL = "https://allegro.pl/kategoria/podzespoly-komputerowe-karty-graficzne-260019?string=GeForce%20RTX%203070%20Ti&order=p&stan=nowe"
headers = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(URL)

amazon_web_page = response.text

pprint.pprint(amazon_web_page)

soup = BeautifulSoup(amazon_web_page, "html.parser")

pprint.pprint(soup)

all_items = soup.find_all(name="article",
                          class_="mx7m_1 mnyp_co mlkp_ag")

print(all_items)