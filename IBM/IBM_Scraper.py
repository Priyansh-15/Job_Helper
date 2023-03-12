import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

IBM_URL = "https://www.ibm.com/in-en"

def get_internship_jobs():
    pass

def get_entry_level_jobs():
    pass

def get_experienced_jobs():
    pass

def navigate_browser():
    wait = WebDriverWait(driver, 10)
    cookie_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Required only')]")))
    cookie_element.click()
    wait = WebDriverWait(driver, 10)
    careers_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Explore IBM careers')]")))
    careers_element.click()
    wait = WebDriverWait(driver, 10)
    jobs_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Jobs')]")))
    jobs_element.click()
    get_internship_jobs()
    get_entry_level_jobs()
    get_experienced_jobs()
    pass

def start_browser():
    driver.get(IBM_URL)
    navigate_browser()
    time.sleep(5)
    driver.quit()

start_browser()

