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
INFOSYS_NEWGRAD_URL="https://digitalcareers.infosys.com/infosys/global-careers?location=Asia%20Pacific&job_type=graduate"
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



def Infosys_job_newgrad_scrape(index):
    infosys_newgrad=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
   
    driver.get(INFOSYS_NEWGRAD_URL)
    wait=WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]'))).click()
    driver.execute_script("window.scrollTo(0, 680)") 
    s_i=680
    time.sleep(1)
    while True:
        try:
            
            infosys_job_expand='//*[@id="section_59988"]/a['+str(index)+']/div[1]/div[1]'
            page0 = driver.execute_script('return document.body.innerHTML')
            soup0=BeautifulSoup(''.join(page0), 'lxml')
            dom0 = etree.HTML(str(soup0))
            try:
                job_title=dom0.xpath(infosys_job_expand)[0].text
            except:
                break
            location=dom0.xpath('//*[@id="section_59988"]/a[1]/div[1]/div[2]')[0].text
            print(location)
            wait.until(EC.element_to_be_clickable((By.XPATH,infosys_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="sortableHeader"]/li/div/div/div/div[1]'))) #dummy to wait till page is loaded

            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup))

            index+=1 

            #scraped information //*[@id="section_59988"]/a[1]/div[1]/div[1]
            
            job_url=driver.current_url
            try:
                description_data=dom.xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]')
                print(description_data)
                for l in description_data:
                    description=etree.tostring(l, pretty_print=True).decode()
                    description=text_decode(description)
            except:
                description='not found'
            print(description)
            
            job_data={
                'Company_Name':'Infosys',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':description
            } 
            infosys_newgrad.append(job_data)
            
            driver.back()
            s_i=s_i+200
            
           
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results"]/li['+str(index-1)+']/div/a/div')))
            
            driver.execute_script('window.scrollTo(0,'+str(s_i)+')')
            time.sleep(1) 
            print(index-1)

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,infosys_newgrad,'Infosys_newgrad_openings.csv')





def add_to_csv(fieldnames,infosys,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(infosys)



Infosys_job_newgrad_scrape(1)

