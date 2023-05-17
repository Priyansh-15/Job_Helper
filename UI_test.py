# lambdatest_test.py

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        #object of ChromeOptions
        options = webdriver.ChromeOptions()
        #setting headless parameter
        options.headless = True
        self.driver = webdriver.Chrome(options=options)


# tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("http://localhost:3001/")

        # Click on name txt box
        name_box = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/form/div/div[1]/fieldset/div/div[1]/input')
        name_box.send_keys("Koustubh Sinha")

        # Click on  slider
        slider = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/form/div/div[2]/fieldset/div/div[1]/span[2]/span[3]')
        slider.click()

        # Enter next
        next= driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/form/div/center/a/div')
        next.click()
        

if __name__ == "__main__":
    unittest.main()