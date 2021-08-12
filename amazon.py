import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.pl/s?k=geforce+rtx+3070+ti&i=computers&rh=n%3A20788599031%2Cp_36%3A100000-600000&s=price-asc-rank&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1628523140&rnid=20900476031&ref=sr_st_price-asc-rank"
headers = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(URL, headers)

amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, "lxml")

all_items = soup.find_all(name="div",
                          class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20")

lowest_price = 10000

for item in all_items:

    items_checking_text = item.find(name="span", class_="a-size-base-plus a-color-base a-text-normal").get_text()
    items_price = item.find(name="span", class_="a-price-whole")

    if items_price == None:
        items_price = 10000
    else:
        items_price = items_price.get_text()
        items_price = int((items_price.replace("\xa0", "")).replace(",", ""))

    if items_checking_text.find("3070") > 0 and items_price < lowest_price:
        lowest_price = items_price
        item_name = items_checking_text

        URL = (item.find(name="a", class_="a-link-normal a-text-normal")).get('href')
        items_URL = "https://www.amazon.pl/" + URL

print(f"Price:{lowest_price}\nText: {item_name}\nURL: {items_URL}")