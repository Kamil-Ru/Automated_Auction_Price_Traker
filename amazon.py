import requests
from bs4 import BeautifulSoup
from password import HEADERS

URL = "https://www.amazon.pl/s?k=geforce+rtx+3070+ti&i=computers&rh=n%3A20788599031%2Cp_36%3A100000-600000&s=price-asc-rank&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1628523140&rnid=20900476031&ref=sr_st_price-asc-rank"
headers = HEADERS

response = requests.get(URL, headers)

web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

all_items = soup.find_all(name="div",
                          class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20")

lowest_price = 10000
item_name = None
items_URL = None


for item in all_items:

    item_checking_text = item.find(name="span", class_="a-size-base-plus a-color-base a-text-normal").get_text()
    item_price = item.find(name="span", class_="a-price-whole")

    if item_price == None:
        item_price = 10000
    else:
        item_price = item_price.get_text()
        item_price = int((item_price.replace("\xa0", "")).replace(",", ""))

    if item_checking_text.find("3070") > 0 and item_price < lowest_price:
        lowest_price = item_price
        item_name = item_checking_text

        URL = (item.find(name="a", class_="a-link-normal a-text-normal")).get('href')
        items_URL = "https://www.amazon.pl/" + URL

print(f"Price:{lowest_price}\nText: {item_name}\nURL: {items_URL}")