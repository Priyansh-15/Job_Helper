import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#list of xpaths
google_job_button="/html/body/div[1]/header/div[1]/div[1]/nav/ul/li[4]/a"
google_job_type_button='//*[@id="accordion-employment-type"]'
google_job_filter_experienced='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[1]/label/span'
google_job_expand='//*[@id="search-results"]/li[1]/div/a/div/div[2]/div[2]/a'
google_job_filter_internship='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[4]/label/span'
google_job_filter1_newgrad='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[2]/label/span'
google_job_filter2_newgrad='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[3]/label/span'


def GoogleExperienced():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    wait=WebDriverWait(driver,10)
     
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_type_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_filter_experienced))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
    
    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    time.sleep(10)
    driver.close()

def GoogleNew_Grad():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    wait=WebDriverWait(driver,10)
     
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_type_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_filter_experienced))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_filter1_newgrad))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_filter2_newgrad))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    time.sleep(10)
    driver.close()


def GoogleInternship():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    wait=WebDriverWait(driver,10)
     
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_type_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_filter_internship))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    time.sleep(10)
    driver.close()