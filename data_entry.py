from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfm-VQAcRnBnMMEjQF9FJEwK_d15at8K0jsnimTI7jN60q1cA/viewform?usp=sf_link"

chrome_driver_path = "E:\Development\chromedriver.exe"


class DataEntry:
    def __init__(self, adresses, rents, links):
        self.adresses = adresses
        self.rents = rents
        self.links = links
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def fill_form(self):
        self.driver.get(FORM_LINK)
        time.sleep(3)

        for x in range(len(self.adresses)):

            input_adress = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_adress.send_keys(self.adresses[x])

            input_price = self.driver.find_element_by_xpath(
               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_price.send_keys(self.rents[x])

            input_link = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_link.send_keys(self.links[x])

            send_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            send_button.click()

            time.sleep(2)
            another_send_button = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_send_button.click()
            time.sleep(1)


