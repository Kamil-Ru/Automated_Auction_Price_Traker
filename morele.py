import requests
from bs4 import BeautifulSoup

URL = "https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,p,0,,,,/1/?q=RTX+3070+Ti"
headers = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(URL, headers)

web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

all_items = soup.find_all(name="div",
                          class_="cat-product card")

lowest_price = 10000

for item in all_items:

    item_price = item.find(name="div", class_="price-new")

    item_price = item_price.get_text().split(",")[0]
    item_price = int("".join(_ for _ in item_price if _.isdigit()))
    item_checking_text = item.find(name="a", class_="productLink")

    item_checking_text, URL = item_checking_text.get("title"), item_checking_text.get("href")

    if item_checking_text.find("3070") > 0 and item_price < lowest_price:
        lowest_price = item_price
        item_name = item_checking_text
        items_URL = "https://www.morele.net" + URL

print(f"Price: {lowest_price}\nText: {item_name}\nURL: {items_URL}")