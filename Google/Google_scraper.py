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

GOOGLE_INTERNSHIP_URL = "https://careers.google.com/jobs/results/?distance=50&employment_type=INTERN"
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
    driver = webdriver.Chrome()
    driver.headless = True
    driver.get(GOOGLE_INTERNSHIP_URL)
    wait=WebDriverWait(driver,10)
    while True:
        try:
            google_job_expand='//*[@id="search-results"]/li['+str(index)+']/div/a/div'
            wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,google_job_title))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'html.parser')
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

def add_to_csv(fieldnames,google,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(google)


Google_job_internship_scrape(1)

