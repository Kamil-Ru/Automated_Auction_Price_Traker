from selenium import webdriver

class Allegro:
    def __init__(self):
        self.URL = "https://allegro.pl/kategoria/podzespoly-komputerowe-karty-graficzne-260019?string=GeForce%203070%20Ti&stan=nowe&order=p"
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver")

    def get_data(self):
        self.driver.get(self.URL)
        test_1 = self.driver.find_elements_by_xpath("//article[@class='mx7m_1 mnyp_co mlkp_ag']")

        for element in test_1:
            item_price = self.driver.find_element_by_xpath("//span[@class='_1svub _lf05o']").text
            print(item_price)
            item_price = item_price.split(",")[0]
            item_price = int("".join(_ for _ in item_price if _.isdigit()))








        return print(f"Len: {len(test_1)}\n Print: {test_1}\n Prize: {item_price}")




