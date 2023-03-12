import time
from selenium import webdriver

IBM_URL = "https://www.ibm.com/in-en"

def startBrowser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(IBM_URL)
    time.sleep(5)
    driver.quit()
