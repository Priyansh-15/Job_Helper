import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

IBM_URL = "https://www.ibm.com/in-en"
CLEAR_FILTERS = "//*[@id=\"filterPanel\"]//dds-filter-panel//section/div/button"
APPLY_FILTERS = "//*[@id=\"__next\"]/div/div[2]/div/main/div/div[2]/div/div[1]/div/div/div/button"
INTERNSHIP_JOBS = "//*[@id=\"filterPanel\"]//dds-filter-panel/dds-filter-group/dds-filter-group-item[3]/dds-filter-panel-checkbox[2]//label"
ENTRY_LEVEL_JOBS = "//*[@id=\"filterPanel\"]//dds-filter-panel/dds-filter-group/dds-filter-group-item[3]/dds-filter-panel-checkbox[3]//label"
EXPERIENCED_JOBS = "//*[@id=\"filterPanel\"]//dds-filter-panel/dds-filter-group/dds-filter-group-item[3]/dds-filter-panel-checkbox[1]//label"
JOBS_ANCHOR_CLASS = "cds--link bx--card__footer undefined"

internship_job_links = []
entry_level_job_links = []
experienced_job_links = []

def click_element(driver, identifier, value):
    try:
        if identifier == "xpath":
            element = driver.find_element(By.XPATH, value)
            element.click()
        elif identifier == "link":
            element = driver.find_element(By.LINK_TEXT, value)
            element.click()
        else:
            raise ValueError("Invalid identifier: {}".format(identifier))
    except ValueError as e:
        print("Error: {}".format(str(e)))

def filter_jobs(driver, job_xpath):
    click_element(driver, "xpath", CLEAR_FILTERS)
    click_element(driver, "xpath", job_xpath)
    click_element(driver, "xpath", APPLY_FILTERS)

def get_job_links(driver, identifier):
    try:
        if identifier == 1:
            internship_job_links = driver.find_elements_by_css_selector('a.{}'.format(JOBS_ANCHOR_CLASS))
        elif identifier == 2:
            entry_level_job_links  = driver.find_elements_by_css_selector('a.{}'.format(JOBS_ANCHOR_CLASS))
        elif identifier == 3:
            experienced_job_links  = driver.find_elements_by_css_selector('a.{}'.format(JOBS_ANCHOR_CLASS))
        else:
            raise ValueError("Invalid identifier: {}".format(identifier))
    except ValueError as e:
        print("Error: {}".format(str(e)))
        

def get_internship_jobs(driver):
    filter_jobs(driver, INTERNSHIP_JOBS)
    get_job_links(driver, 1)

def get_entry_level_jobs(driver):
    filter_jobs(driver, ENTRY_LEVEL_JOBS)

def get_experienced_jobs(driver):
    filter_jobs(driver, EXPERIENCED_JOBS)



def navigate_browser(driver):
    wait = WebDriverWait(driver, 10)
    cookie_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Required only')]")))
    cookie_element.click()
    click_element(driver, "link", "Explore IBM careers")
    click_element(driver, "link", "Jobs")
    get_internship_jobs(driver)
    get_entry_level_jobs(driver)
    get_experienced_jobs(driver)

def start_browser():
    driver = webdriver.Chrome()
    driver.get(IBM_URL)
    navigate_browser(driver)
    time.sleep(5)
    driver.quit()

start_browser()

