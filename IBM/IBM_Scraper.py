import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

IBM_URL = "https://www.ibm.com/in-en"
JOBS_BUTTON = "//*[@id=\"__next\"]/div/div[1]/div[2]/div/div/div[2]/div[1]/nav/ul/li[5]/a"
CLEAR_FILTERS = "//*[@id=\"filterPanel\"]//dds-filter-panel//section/div/button"
APPLY_FILTERS = "//*[@id=\"__next\"]/div/div[2]/div/main/div/div[2]/div/div[1]/div/div/div/button"
INTERNSHIP_JOBS = "//*[@id=\"filterPanel\"]//dds-filter-panel/dds-filter-group/dds-filter-group-item[3]/dds-filter-panel-checkbox[2]//label"
ENTRY_LEVEL_JOBS = "//*[@id=\"filterPanel\"]//dds-filter-panel/dds-filter-group/dds-filter-group-item[3]/dds-filter-panel-checkbox[3]//label"
EXPERIENCED_JOBS = "//*[@id=\"filterPanel\"]//dds-filter-panel/dds-filter-group/dds-filter-group-item[3]/dds-filter-panel-checkbox[1]//label"
JOBS_ANCHOR_CLASS = "cds--link bx--card__footer undefined"

internship_job_links = []
entry_level_job_links = []
experienced_job_links = []

def wait_for_page_load(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

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
    wait_for_page_load(driver)
    click_element(driver, "xpath", job_xpath)
    click_element(driver, "xpath", APPLY_FILTERS)

def get_job_links(driver, identifier):
    try:
        if identifier == 1:
            internship_job_links = driver.find_element(By.CSS_SELECTOR, 'a.{}'.format(JOBS_ANCHOR_CLASS))
            print(internship_job_links)
        elif identifier == 2:
            entry_level_job_links = driver.find_element(By.CSS_SELECTOR, 'a.{}'.format(JOBS_ANCHOR_CLASS))
            print(entry_level_job_links)
        elif identifier == 3:
            experienced_job_links = driver.find_element(By.CSS_SELECTOR, 'a.{}'.format(JOBS_ANCHOR_CLASS))
            print(experienced_job_links)
        else:
            raise ValueError("Invalid identifier: {}".format(identifier))
    except ValueError as e:
        print("Error: {}".format(str(e)))

def get_internship_jobs(driver):
    wait_for_page_load(driver)
    filter_jobs(driver, INTERNSHIP_JOBS)
    wait_for_page_load(driver)
    get_job_links(driver, 1)

def get_entry_level_jobs(driver):
    wait_for_page_load(driver)
    filter_jobs(driver, ENTRY_LEVEL_JOBS)
    wait_for_page_load(driver)
    get_job_links(driver, 2)

def get_experienced_jobs(driver):
    wait_for_page_load(driver)
    filter_jobs(driver, EXPERIENCED_JOBS)
    wait_for_page_load(driver)
    get_job_links(driver, 3)

def navigate_browser(driver):
    wait_for_page_load(driver)
    click_element(driver, "xpath", "//button[contains(text(), 'Required only')]")
    wait_for_page_load(driver)
    click_element(driver, "link", "Explore IBM careers")
    wait_for_page_load(driver)
    click_element(driver, "xpath", JOBS_BUTTON)
    get_internship_jobs(driver)
    get_entry_level_jobs(driver)
    get_experienced_jobs(driver)

def start_browser():
    driver = webdriver.Chrome()
    driver.get(IBM_URL)
    driver.maximize_window()
    navigate_browser(driver)
    time.sleep(5)
    driver.quit()

start_browser()

