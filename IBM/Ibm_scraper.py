#
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

IBM_INTERNSHIP_URL = "https://careers.google.com/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&employment_type=INTERN&jex=ENTRY_LEVEL"
IBM_NEWGRAD_URL="https://careers.google.com/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&employment_type=FULL_TIME&employment_type=PART_TIME&employment_type=TEMPORARY&jex=ENTRY_LEVEL"
IBM_EXPERIENCED_URL= "https://www.ibm.com/careers/in-en/search/?filters=level:Professional"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS

ibm_job_location='//*[@id="post-116"]/div/div[1]/div/div[1]/div/div[2]/ul/li[1]/div/div'
ibm_job_title='//*[@id="post-116"]/div/div[1]/div/div[1]/div/div[1]/h1/p'
ibm_job_description='//*[@id="post-116"]/div/div[4]/div/div[1]/div/div[1]/div'

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
           
           



def Ibm_job_experienced_scrape(index):
    ibm_experienced=[]
    location=""
    description=""
    driver = webdriver.Chrome()
   
    driver.get(IBM_EXPERIENCED_URL)
    wait=WebDriverWait(driver,10)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="truste-consent-close"]'))).click()
    except:
        print('not there')

    while True:
        try:
            ibm_job_expand='//*[@id="__next"]/div/div[2]/div/main/div/div[2]/div/div[2]/div[2]/div/div['+str(index)+']/div/div/div/a'
            wait.until(EC.element_to_be_clickable((By.XPATH,ibm_job_expand))).click()
          
            p = driver.current_window_handle
            chwd = driver.window_handles
            
            for w in chwd:
                if(w!=p):
                    driver.switch_to.window(w)
            wait.until(EC.presence_of_element_located((By.XPATH,ibm_job_title))) 
            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'lxml')
            dom = etree.HTML(str(soup)) 
            index+=1 
            
            #scraped information
            job_title=dom.xpath('/html/body/div[2]/div[2]/main/div/section/div/div/div[4]/div/div[2]/div/div[2]/div[1]/div[1]/text()')
            job_url=driver.current_url
            location=dom.xpath(ibm_job_location)[0].text
            
            try:   
                description_data=dom.xpath(ibm_job_description)
                for d in description_data:
                    description=etree.tostring(d, pretty_print=True).decode()
                description=text_decode(description)
            except:
                description="couldn't get"
        
            job_data={
                'Company_Name':'IBM',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':description
            } 
            ibm_experienced.append(job_data)
            
            driver.close()
            driver.switch_to.window(p)
            print(index-1)
            

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,ibm_experienced,'IBM_experienced_openings.csv')



def add_to_csv(fieldnames,ibm,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(ibm)


Ibm_job_experienced_scrape(1)
