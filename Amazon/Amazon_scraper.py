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

AMAZON_INTERNSHIP_URL = "https://www.amazon.jobs/en/business_categories/student-programs?offset=0&result_limit=10&sort=relevant&category%5B%5D=software-development&category%5B%5D=hardware-development&category%5B%5D=data-science&category%5B%5D=operations-it-support-engineering&category%5B%5D=systems-quality-security-engineering&job_type%5B%5D=Internship&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"
AMAZON_NEWGRAD_URL="https://www.amazon.jobs/en/business_categories/student-programs?offset=0&result_limit=10&sort=relevant&category%5B%5D=software-development&category%5B%5D=hardware-development&category%5B%5D=operations-it-support-engineering&category%5B%5D=data-science&category%5B%5D=systems-quality-security-engineering&job_type%5B%5D=Full-Time&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"
AMAZON_EXPERIENCED_URL= "https://www.amazon.jobs/en/job_categories/software-development?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS
amazon_job_location='//*[@id="job-detail-body"]/div/div[2]/div/div[1]/div[2]/div[1]/div/div'
amazon_job_title='//*[@id="job-detail"]/div[1]/div/div/div/div[1]/div/h1'
amazon_job_description='//*[@id="job-detail-body"]/div/div[1]/div/div[2]'


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
           
           

def Amazon_job_internship_scrape():
    index=1
    amazon_internship=[]
    amazon_internship.append({
                    'Company_Name':'Company_Name',
                    'Job_title':'Job_title',
                    'Url':'Url',
                    'Location':'Location',
                    'Description':'Description'
                } )
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    
    driver.get(AMAZON_INTERNSHIP_URL)
    wait=WebDriverWait(driver,10)
    try:
        while True:
            try:
                amazon_job_expand='//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div['+str(index)+']/a/div'
                wait.until(EC.element_to_be_clickable((By.XPATH,amazon_job_expand))).click()
                wait.until(EC.presence_of_element_located((By.XPATH,amazon_job_title))) #dummy to wait till page is loaded

                page = driver.execute_script('return document.body.innerHTML')
                soup=BeautifulSoup(''.join(page), 'lxml')
                dom = etree.HTML(str(soup))

                index+=1 

                #scraped information
                job_title=dom.xpath(amazon_job_title)[0].text
                job_url=driver.current_url
                location_data=dom.xpath(amazon_job_location)
                description_data=dom.xpath(amazon_job_description)

                for l in location_data:
                    location=etree.tostring(l, pretty_print=True).decode()
                    location=text_decode(location)

                for d in description_data:
                    description=etree.tostring(d, pretty_print=True).decode()
                
                if(len(location)<=0):
                    location='No specific location'

                job_data={
                    'Company_Name':'Amazon',
                    'Job_title':job_title,
                    'Url':job_url,
                    'Location':location,
                    'Description':text_decode(description)
                } 
                amazon_internship.append(job_data)
                
                #wait.until(EC.element_to_be_clickable((By.XPATH,amazon_back_button))).click() 
                driver.back()
                #time.sleep(1.5)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div['+str(index)+']/a/div')))
                print(index-1)

            except TimeoutException:
                driver.quit()
                break

        add_to_csv(fieldnames,amazon_internship,'Amazon_internship_openings.csv')
        return "amazon jobs added to csv"    
    except:
        return "scraper actions couldn't be completed"


def Amazon_job_newgrad_scrape():
    index=1
    amazon_newgrad=[]
    amazon_newgrad.append({
                    'Company_Name':'Company_Name',
                    'Job_title':'Job_title',
                    'Url':'Url',
                    'Location':'Location',
                    'Description':'Description'
                } )
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    
    driver.get(AMAZON_NEWGRAD_URL)
    wait=WebDriverWait(driver,10)
    try:
        while True:
            try:
                amazon_job_expand='//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div['+str(index)+']/a/div'
                wait.until(EC.element_to_be_clickable((By.XPATH,amazon_job_expand))).click()
                wait.until(EC.presence_of_element_located((By.XPATH,amazon_job_title))) #dummy to wait till page is loaded

                page = driver.execute_script('return document.body.innerHTML')
                soup=BeautifulSoup(''.join(page), 'lxml')
                dom = etree.HTML(str(soup))

                index+=1 

                #scraped information
                job_title=dom.xpath(amazon_job_title)[0].text
                job_url=driver.current_url
                location_data=dom.xpath(amazon_job_location)
                description_data=dom.xpath(amazon_job_description)

                for l in location_data:
                    location=etree.tostring(l, pretty_print=True).decode()
                    location=text_decode(location)

                for d in description_data:
                    description=etree.tostring(d, pretty_print=True).decode()
                
                if(len(location)<=0):
                    location='No specific location'

                job_data={
                    'Company_Name':'Amazon',
                    'Job_title':job_title,
                    'Url':job_url,
                    'Location':location,
                    'Description':text_decode(description)
                } 
                amazon_newgrad.append(job_data)
                
                #wait.until(EC.element_to_be_clickable((By.XPATH,amazon_back_button))).click() 
                driver.back()
                #time.sleep(1.5)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div['+str(index)+']/a/div')))
                print(index-1)

            except TimeoutException:
                driver.quit()
                break

        add_to_csv(fieldnames,amazon_newgrad,'Amazon_newgrad_openings.csv')
        return "amazon jobs added to csv"    
    except:
        return "scraper actions couldn't be completed"



def Amazon_job_experienced_scrape():
    index=1
    amazon_experienced=[]
    amazon_experienced.append({
                    'Company_Name':'Company_Name',
                    'Job_title':'Job_title',
                    'Url':'Url',
                    'Location':'Location',
                    'Description':'Description'
                } )
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
    
    driver.get(AMAZON_EXPERIENCED_URL)
    wait=WebDriverWait(driver,10)
    try:
        while True:
            try:
                amazon_job_expand='//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div['+str(index)+']/a/div'
                wait.until(EC.element_to_be_clickable((By.XPATH,amazon_job_expand))).click()
                wait.until(EC.presence_of_element_located((By.XPATH,amazon_job_title))) #dummy to wait till page is loaded

                page = driver.execute_script('return document.body.innerHTML')
                soup=BeautifulSoup(''.join(page), 'lxml')
                dom = etree.HTML(str(soup))

                index+=1 

                #scraped information
                job_title=dom.xpath(amazon_job_title)[0].text
                job_url=driver.current_url
                location_data=dom.xpath(amazon_job_location)
                description_data=dom.xpath(amazon_job_description)

                for l in location_data:
                    location=etree.tostring(l, pretty_print=True).decode()
                    location=text_decode(location)

                for d in description_data:
                    description=etree.tostring(d, pretty_print=True).decode()
                
                if(len(location)<=0):
                    location='No specific location'
                    
                job_data={
                    'Company_Name':'Amazon',
                    'Job_title':job_title,
                    'Url':job_url,
                    'Location':location,
                    'Description':text_decode(description)
                } 
                amazon_experienced.append(job_data)
                
                #wait.until(EC.element_to_be_clickable((By.XPATH,amazon_back_button))).click() 
                driver.back()
                #time.sleep(1.5)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div['+str(index)+']/a/div')))
                print(index-1)

            except TimeoutException:
                driver.quit()
                break

        add_to_csv(fieldnames,amazon_experienced,'Amazon_experienced_openings.csv')
        return "amazon jobs added to csv"    
    except:
        return "scraper actions couldn't be completed"




def add_to_csv(fieldnames,amazon,title):
    with open(title, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(amazon)

#Amazon_job_internship_scrape()
#Amazon_job_newgrad_scrape()
# Amazon_job_experienced_scrape()


  