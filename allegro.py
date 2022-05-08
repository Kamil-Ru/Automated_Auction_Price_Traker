import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class Allegro:
    def __init__(self):
        self.URL = "https://allegro.pl/kategoria/podzespoly-komputerowe-karty-graficzne-260019?string=GeForce%203070%20Ti&stan=nowe&order=p&offerTypeBuyNow=1"
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver")

    def get_data(self):
        self.driver.get(self.URL)
        time.sleep(5)

        button_cookies = self.driver.find_element_by_xpath("//button[@data-role='accept-consent']")
        button_cookies.click()
        time.sleep(1)

        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(20)

        searching_cards = self.driver.find_elements_by_xpath("//div[contains(@class, 'mpof_ki myre_zn _9c44d_1Hxbq')]")

        lowest_price = 10000
        for card in searching_cards:
            try:
                items_checking_text = card.find_element_by_xpath(".//a[@class='_w7z6o _uj8z7 meqh_en mpof_z0 mqu1_16 _9c44d_2vTdY  ']").text

                url = card.find_element_by_xpath(".//a[@class='_w7z6o _uj8z7 meqh_en mpof_z0 mqu1_16 _9c44d_2vTdY  ']").get_attribute('href')

                item_checking_price = card.find_element_by_xpath(".//div[@class='msa3_z4 _9c44d_2K6FN']").text
                item_checking_price = item_checking_price.split(",")
                item_checking_price = item_checking_price[0]

                item_checking_price = int("".join(_ for _ in item_checking_price if _.isdigit()))

                if items_checking_text.find("3070") > 0 and item_checking_price < lowest_price:
                    lowest_price = item_checking_price
                    item_name = items_checking_text
                    items_URL = url

            except:
                print("EMPTY")

        self.driver.quit()

        return {"price": lowest_price, "text": item_name, "url": items_URL, "shop": "Allegro"}




