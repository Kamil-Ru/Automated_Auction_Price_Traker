import requests
from bs4 import BeautifulSoup

URL = "https://www.komputronik.pl/search/category/1099?sort=1&by=f_price_10&showBuyActiveOnly=1&query=GeForce%20RTX%203070%20Ti"
headers = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(URL, headers)

web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

all_items = soup.find_all(name="li",
                          class_="product-entry2")

lowest_price = 10000

for item in all_items:
    try:
        item_price = item.find(name="span", class_="price")
        item_price = item_price.text
        item_price = ("".join(_ for _ in item_price if _.isdigit()))
        item_price = int(item_price)

        items_checking_text = item.find(name="div", class_="pe2-head").get_text()

        URL = item.find(name="div", class_="pe2-head")
        URL = URL.find(name="a").get("href")

        if items_checking_text.find("3070") > 0 and item_price < lowest_price:
            lowest_price = item_price
            item_name = items_checking_text
            items_URL = URL

    except:
        continue

print(f"Price: {lowest_price}\nText: {item_name}\nURL: {items_URL}")
