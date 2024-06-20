from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Info():
    def __init__(self):
        chrome_driver_path = r'C:\Users\chromedriver-win64\chromedriver.exe'
        service = Service(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.ID, 'searchInput')
        search.send_keys(self.query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()
        time.sleep(10)  # Wait for 10 seconds
        self.driver.quit()  # Quit the webdriver instance after 10 seconds

