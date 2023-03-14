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

MICROSOFT_INTERNSHIP_URL = "https://careers.microsoft.com/students/us/en/search-results"
MICROSOFT_NEWGRAD_URL ="https://careers.microsoft.com/students/us/en/search-results"
MICROSOFT_EXPERIENCED_URL ="https://careers.microsoft.com/us/en/search-results"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS
microsoft_employment_type_button='/html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[8]/div[1]/span/button'
microsoft_intern_button='/html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[8]/div[2]/div/div[2]/ul/li[1]/label/span[2]'
microsoft_back_button='//*[@id="content"]/div/div[1]/div/nav/ul/li/a'
microsoft_job_location='//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/ul/li[1]/div[2]'
microsoft_job_title='//*[@id="content"]/div/div[2]/div/div[1]/h2'
microsoft_job_description='//*[@id="content"]/div/div[2]/div/div[2]/div[3]/div/div[1]'

def text_decode(txt):
    str=""
    for s in txt:
        if(s=='>'):
            t=1
        elif(s=='<'):
            t=0
        if(t==1 and s!='>' and s!='\n'):
            str+=s
    return str

def auto():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MICROSOFT_INTERNSHIP_URL)
    driver.execute_script("window.scrollTo(0, 300)")  
    time.sleep(20)  

def Microsoft_job_internship_scrape(index):
    microsoft_internship=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    driver.get(MICROSOFT_INTERNSHIP_URL)
    driver.execute_script("window.scrollTo(0, 300)")
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-close-btn-container"]/button'))).click()

    while True:
        try:
            microsoft_job_expand='//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]/a'
            wait.until(EC.element_to_be_clickable((By.XPATH,microsoft_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,microsoft_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(microsoft_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(microsoft_job_location)
            description_data=dom.xpath(microsoft_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description+=etree.tostring(d, pretty_print=True).decode()

            job_data={
                'Company_Name':'Microsoft',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            microsoft_internship.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,microsoft_back_button))).click() 
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]/a')))
            driver.execute_script("window.scrollTo(0, 800)")
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,microsoft_internship,'Microsoft_internship_openings.csv')


def Microsoft_job_newgrad_scrape(index):
    microsoft_newgrad=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    driver.get(MICROSOFT_NEWGRAD_URL)
    driver.execute_script("window.scrollTo(0, 300)")
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-close-btn-container"]/button'))).click()
    
    while True:
        try:
            microsoft_job_expand='//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]/a'
            wait.until(EC.element_to_be_clickable((By.XPATH,microsoft_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,microsoft_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(microsoft_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(microsoft_job_location)
            description_data=dom.xpath(microsoft_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description+=etree.tostring(d, pretty_print=True).decode()

            job_data={
                'Company_Name':'Microsoft',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            microsoft_newgrad.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,microsoft_back_button))).click() 
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]')))
            driver.execute_script("window.scrollTo(0, 800)")
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,microsoft_newgrad,'Microsoft_newgrad_openings.csv')

def Microsoft_job_experienced_scrape(index):
    microsoft_experienced=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    driver.get(MICROSOFT_EXPERIENCED_URL)
    driver.execute_script("window.scrollTo(0, 300)")
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-close-btn-container"]/button'))).click()
    
    while True:
        try:
            microsoft_job_expand='//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]/a'
            wait.until(EC.element_to_be_clickable((By.XPATH,microsoft_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,microsoft_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(microsoft_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(microsoft_job_location)
            description_data=dom.xpath(microsoft_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description+=etree.tostring(d, pretty_print=True).decode()

            job_data={
                'Company_Name':'Microsoft',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            microsoft_experienced.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,microsoft_back_button))).click() 
            #time.sleep(1.5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]')))
            driver.execute_script("window.scrollTo(0, 800)")
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,microsoft_experienced,'Microsoft_experienced_openings.csv')

def add_to_csv(fieldnames,microsoft,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(microsoft)

#auto()
#Microsoft_job_internship_scrape(1)
#Microsoft_job_newgrad_scrape(1)
#Microsoft_job_experienced_scrape(1)
