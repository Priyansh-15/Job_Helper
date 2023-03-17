import time
import csv
from bs4 import BeautifulSoup
from IPython.display import HTML
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions

#object of ChromeOptions
options = webdriver.ChromeOptions()
#setting headless parameter
options.headless = True

GOOGLE_INTERNSHIP_URL = "https://careers.google.com/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&employment_type=INTERN&jex=ENTRY_LEVEL"
GOOGLE_NEWGRAD_URL="https://careers.google.com/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&employment_type=FULL_TIME&employment_type=PART_TIME&employment_type=TEMPORARY&jex=ENTRY_LEVEL"
GOOGLE_EXPERIENCED_URL= "https://careers.google.com/jobs/results/?distance=50&employment_type=FULL_TIME"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS
google_back_button='/html/body/div[1]/header/div[1]/div[2]/div/div/button'
google_job_location='//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[1]/ul[2]/li[2]'
google_job_title='//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[1]/h1'
google_job_description='//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[2]/div[2]'


def text_decode(txt):
    str=""
    for s in txt:
        if(s=='>'):
            t=1
        elif(s=='<'):
            t=0
        if(t==1 and s!='>'):
           str+=s
    return str
           
           

def Google_job_internship_scrape(index):
    google_internship=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
   
    driver.get(GOOGLE_INTERNSHIP_URL)
    wait=WebDriverWait(driver,10)
    while True:
        try:
            google_job_expand='//*[@id="search-results"]/li['+str(index)+']/div/a/div'
            wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,google_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(google_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(google_job_location)
            description_data=dom.xpath(google_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description=etree.tostring(d, pretty_print=True).decode()
            
            job_data={
                'Company_Name':'Google',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            google_internship.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,google_back_button))).click() 
            time.sleep(1.5)
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results"]/li['+str(index-1)+']/div/a/div')))
            driver.execute_script("window.scrollTo(0, 1000)") 
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,google_internship,'Google_internship_openings.csv')



def Google_job_newgrad_scrape(index):
    google_newgrad=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
   
    driver.get(GOOGLE_NEWGRAD_URL)
    wait=WebDriverWait(driver,10)
    while True:
        try:
            google_job_expand='//*[@id="search-results"]/li['+str(index)+']/div/a/div'
            wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,google_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(google_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(google_job_location)
            description_data=dom.xpath(google_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description=etree.tostring(d, pretty_print=True).decode()
            
            job_data={
                'Company_Name':'Google',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            google_newgrad.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,google_back_button))).click() 
            time.sleep(1.5)
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results"]/li['+str(index-1)+']/div/a/div')))
            driver.execute_script("window.scrollTo(0, 1080)") 
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,google_newgrad,'Google_newgrad_openings.csv')



def Google_job_experienced_scrape(index):
    google_experienced=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
   
    driver.get(GOOGLE_EXPERIENCED_URL)
    wait=WebDriverWait(driver,10)
    while True:
        try:
            google_job_expand='//*[@id="search-results"]/li['+str(index)+']/div/a/div'
            wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,google_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(google_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(google_job_location)
            description_data=dom.xpath(google_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description=etree.tostring(d, pretty_print=True).decode()
            
            job_data={
                'Company_Name':'Google',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            google_experienced.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,google_back_button))).click() 
            time.sleep(1.5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results"]/li['+str(index-1)+']/div/a/div')))
            driver.execute_script("window.scrollTo(0, 1080)") 
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,google_experienced,'Google_experienced_openings.csv')



def add_to_csv(fieldnames,google,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(google)


Google_job_internship_scrape(1)
Google_job_newgrad_scrape(1)
Google_job_experienced_scrape(1)
