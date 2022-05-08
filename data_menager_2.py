import time
from selenium import webdriver
from password import URL_GOOGLE

class DataManager:
    def __init__(self):
        self.url = URL_GOOGLE
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver")

    def send_data(self, data):
        self.driver.get(self.url)
        time.sleep(2)

        input_boxes = self.driver.find_elements_by_xpath("//input[@class='quantumWizTextinputPaperinputInput exportInput']")

        list = []
        for element in data:
            list.append(element['price'])
            list.append(element['url'])

        a = 0
        for element in input_boxes:
            element.send_keys(list[a])
            a += 1

        send_button = self.driver.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonContent exportButtonContent']")
        send_button.click()
        time.sleep(1)
        self.driver.quit()


