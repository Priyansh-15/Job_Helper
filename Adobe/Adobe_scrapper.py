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

ADOBE_EXPERIENCED_URL = "https://careers.adobe.com/us/en/search-results"
GOOGLE_NEWGRAD_URL="https://careers.google.com/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&employment_type=FULL_TIME&employment_type=PART_TIME&employment_type=TEMPORARY&jex=ENTRY_LEVEL"
GOOGLE_EXPERIENCED_URL= "https://careers.google.com/jobs/results/?distance=50&employment_type=FULL_TIME"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS
adobe_type='/html/body/div[2]/div[3]/div/div/div/div[1]/section[1]/div/div/div/div[3]/div[5]/div[1]/div/span/button/i'
adobe_experienced_type='/html/body/div[2]/div[3]/div/div/div/div[1]/section[1]/div/div/div/div[3]/div[5]/div[2]/div/div[2]/fieldset/ul/li[2]/label/span[1]'

google_back_button='/html/body/div[1]/header/div[1]/div[2]/div/div/button'
adobe_job_location='/html/body/div[2]/div[3]/div/div[1]/div[2]/section/div/div/div/div[1]/section/div/div[1]/span[1]/span/text()'
adobe_job_title='/html/body/div[2]/div[3]/div/div[1]/div[2]/section/div/div/div/div[1]/h1'
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
   
    driver.get()
    wait=WebDriverWait(driver,10)
    while True:
        try:
            google_job_expand='//*[@id="search-results"]/li['+str(index)+']/div/a/div'
            wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
            time.sleep(10)
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



def Adobe_job_experienced_scrape():
    index=1
    adobe_experienced=[]
    location=""
    description=""
    driver = webdriver.Chrome()
   
    driver.get(ADOBE_EXPERIENCED_URL)
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/div/div/div/div[2]/button[2]/ppc-content'))).click()
    
    wait.until(EC.element_to_be_clickable((By.XPATH,adobe_type))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,adobe_experienced_type))).click()
   
    while True:
        try:
            adobe_description='/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/p[3]'
            page0 = driver.execute_script('return document.body.innerHTML')
            soup0=BeautifulSoup(''.join(page0), 'lxml')
            dom0 = etree.HTML(str(soup0))
            description=dom0.xpath(adobe_description)[0].text
        
            adobe_job_expand='/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/span/a/div'
            print(driver.find_element(By.XPATH,adobe_job_expand))
            print(adobe_job_expand)
            time.sleep(10)
            wait.until(EC.element_to_be_clickable((By.XPATH,adobe_job_expand))).click()

            wait.until(EC.presence_of_element_located((By.XPATH,adobe_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 
            #scraped information
            job_title=dom.xpath(adobe_job_title)[0].text
            job_url=driver.current_url
            try:
                location=dom.xpath(adobe_job_location)
            except:
                location="Multiple Location"
            
            job_data={
                'Company_Name':'Adobe',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':description
            } 
            adobe_experienced.append(job_data)
            
            #wait.until(EC.element_to_be_clickable((By.XPATH,amazon_back_button))).click() 
            driver.back()
            #time.sleep(1.5)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/span/a/div/span')))
            print(index-1)
        

        except TimeoutException:
            driver.quit()
            break
    add_to_csv(fieldnames,adobe_experienced,'Adobe_experienced_openings.csv')




def add_to_csv(fieldnames,adobe,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(adobe)



Adobe_job_experienced_scrape()
