import pprint

# TODO 3: add this program do server

from amazon import amazon
from ebay import ebay
from komputronik import komputronik
from morele import morele
from msg import send_email, send_SMS
# TODO 1: Delete data manager ?
# TODO 2: Change file name "data_manager_2" to "data_manager_2"
from data_menager_2 import DataManager
from allegro import Allegro

amazon_response = amazon()
ebay_response = ebay()
komputronik_response = komputronik()
morele_response = morele()
allegro = Allegro()
allegro_response = allegro.get_data()

response = []
response.append(amazon_response)
response.append(ebay_response)
response.append(komputronik_response)
response.append(morele_response)
response.append(allegro_response)

lowest_price = 10000
for item in response:
    if item['price'] < lowest_price:
        lowest_price = item['price']
        lowest_item = item

send_data = DataManager()
send_data.send_data(response)


pprint.pprint(response)
print(f"Text: {lowest_item['text']}\nPrice: {lowest_item['price']}\nURL: {lowest_item['url']}")

send_email(price=lowest_item['price'], text=lowest_item['text'], url=lowest_item['url'])

if lowest_item['price'] < 3000:
    send_SMS(price=lowest_item['price'])
