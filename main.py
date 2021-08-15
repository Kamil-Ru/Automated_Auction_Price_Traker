from amazon import amazon
from ebay import ebay
from komputronik import komputronik
from morele import morele
from msg import send_email

#   amazon_response = amazon()
#   ebay_response = ebay()
#   komputronik_response = komputronik()
#   morele_response = morele()

amazon_response = {'price': 4969, 'text': 'Gigabyte GeForce RTX 3070 Ti GV-N307TGAMING OC-8GD, Karta Graficzna do Gier, 8 GB', 'url': 'https://www.amazon.pl//Gigabyte-GeForce-GV-N307TGAMING-OC-8GD-Graficzna/dp/B095X6RLJW?dchild=1'}
ebay_response = {'price': 4331, 'text': 'Zotac Gaming GeForce RTX 3070 Ti Trinity OC 8GB GDDR6X ✅ OVP ✅ Händler Rechnung ', 'url': 'https://www.ebay.pl/itm/265246057611?hash=item3dc1e5a48b%3Ag%3AicYAAOSwafdhAnMw&LH_RPA=1&LH_BIN=1&LH_ItemCondition=1000'}
komputronik_response = {'price': 10000, 'text': None, 'url': None}
morele_response = {'price': 5399, 'text': 'Karta graficzna Inno3D GeForce RTX 3070 Ti X3 OC Dual Slot 8GB GDDR6X (N307T3-086XX-1820VA45)', 'url': 'https://www.morele.net/karta-graficzna-inno3d-geforce-rtx-3070-ti-x3-oc-dual-slot-8gb-gddr6x-n307t3-086xx-1820va45-5947969/'}
response=[]

response.append(amazon_response)
response.append(ebay_response)
response.append(komputronik_response)
response.append(morele_response)

print(amazon_response)
print(ebay_response)
print(komputronik_response)
print(morele_response)

print(response)
lowest_price = 10000

for item in response:
    if item['price'] < lowest_price:
        lowest_price = item['price']
        lowest_item = item

send_email(price=lowest_item['price'], text=lowest_item['text'], url=lowest_item['url'])

print(f"Text: {lowest_item['text']}\nPrice: {lowest_item['price']}\nURL: {lowest_item['url']}")

