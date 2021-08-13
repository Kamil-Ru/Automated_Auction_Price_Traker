import requests
from bs4 import BeautifulSoup

URL = "https://www.ebay.pl/sch/i.html?_fsrp=1&rt=nc&_from=R40&LH_PrefLoc=3&LH_ItemCondition=1000&_nkw=GeForce+RTX+3070+Ti&_sacat=0&LH_BIN=1&_sop=2&LH_RPA=1"
headers = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(URL, headers)

web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

all_items = soup.find_all(name="li",
                            class_="s-item")
all_items = all_items[:9]
lowest_price = 10000

for item in all_items:

    item_price = item.find(name="div", class_="s-item__detail s-item__detail--primary").get_text()
    item_price = str(item_price).split(",")[0]
    item_price = ("".join(_ for _ in item_price if _.isdigit()))
    item_price = int(item_price)

    items_checking_text = item.find(name="h3", class_="s-item__title").get_text()

    URL = item.find(name="a", class_="s-item__link").get("href")

    if items_checking_text.find("3070") > 0 and item_price < lowest_price:
        lowest_price = item_price
        item_name = items_checking_text
        items_URL = URL

print(f"Price: {lowest_price}\nText: {item_name}\nURL: {items_URL}")
