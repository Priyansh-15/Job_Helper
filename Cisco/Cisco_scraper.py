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

CISCO_INTERNSHIP_URL = "https://jobs.cisco.com/jobs/SearchJobs/?21180=%5B165%5D&21180_format=6022&21181=%5B186%2C194%2C187%2C55816092%5D&21181_format=6023&listFilterMode=1"
CISCO_NEWGRAD_URL ="https://jobs.cisco.com/jobs/SearchJobs/?21180=%5B164%5D&21180_format=6022&21181=%5B186%2C194%2C187%2C55816092%5D&21181_format=6023&listFilterMode=1"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS
cisco_back_button='//*[@id="content"]/div/div[1]/div/nav/ul/li/a'
cisco_job_location='//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/ul/li[1]/div[2]'
cisco_job_title='//*[@id="content"]/div/div[2]/div/div[1]/h2'
cisco_job_description='//*[@id="content"]/div/div[2]/div/div[2]/div[3]/div/div[1]'

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
    driver.get(CISCO_INTERNSHIP_URL)
    driver.execute_script("window.scrollTo(0, 300)")  
    time.sleep(20)  

def Cisco_job_internship_scrape(index):
    cisco_internship=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    driver.get(CISCO_INTERNSHIP_URL)
    driver.execute_script("window.scrollTo(0, 300)")
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-close-btn-container"]/button'))).click()
    
    while True:
        try:
             
            cisco_job_expand='//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]/a'
            wait.until(EC.element_to_be_clickable((By.XPATH,cisco_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,cisco_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(cisco_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(cisco_job_location)
            description_data=dom.xpath(cisco_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description+=etree.tostring(d, pretty_print=True).decode()

            job_data={
                'Company_Name':'Cisco',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            cisco_internship.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,cisco_back_button))).click() 
            time.sleep(1.5)
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]')))
            driver.execute_script("window.scrollTo(0, 800)")
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,cisco_internship,'Cisco_internship_openings.csv')


def Cisco_job_newgrad_scrape(index):
    cisco_newgrad=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    driver.get(CISCO_NEWGRAD_URL)
    driver.execute_script("window.scrollTo(0, 300)")
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-close-btn-container"]/button'))).click()
    
    while True:
        try:
             
            cisco_job_expand='//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]/a'
            wait.until(EC.element_to_be_clickable((By.XPATH,cisco_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,cisco_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information
            job_title=dom.xpath(cisco_job_title)[0].text
            job_url=driver.current_url
            location_data=dom.xpath(cisco_job_location)
            description_data=dom.xpath(cisco_job_description)

            for l in location_data:
                location=etree.tostring(l, pretty_print=True).decode()
                location=text_decode(location)

            for d in description_data:
                description+=etree.tostring(d, pretty_print=True).decode()

            job_data={
                'Company_Name':'Cisco',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':text_decode(description)
            } 
            cisco_newgrad.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,cisco_back_button))).click() 
            time.sleep(1.5)
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr['+str(index)+']/td[1]')))
            driver.execute_script("window.scrollTo(0, 800)")
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,cisco_newgrad,'Cisco_newgrad_openings.csv')


def add_to_csv(fieldnames,google,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(google)

#auto()
Cisco_job_internship_scrape(1)
Cisco_job_newgrad_scrape(1)


