from password import *
import requests
from datetime import date

class DataManager:
    def __init__(self):
        self.headersAuth = {
        'Authorization': f'Bearer {BEARER_AUTHENTICATION}',
    }

    def post(self, price, shop, url):
        url_sheety = URL_SHEETY
        body = {
            "Arkusz1": {
                "Date": date.today().__str__(),
                "Price": price,
                "Shop": shop,
                'Link': "url"
            }
        }
        print()
        print(body)
        print(self.headersAuth)
        response = requests.post(data=body, headers=self.headersAuth, url=url_sheety)
        # response = requests.request("POST", url=url_sheety, json=body, headers=self.headersAuth)


        response.raise_for_status()
        return print(response.text)
