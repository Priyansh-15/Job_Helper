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
fieldnames = ['Company_Name','Job_title','Url','Location','Description']


#LIST OF REQUIRED XPATHS
adobe_type='/html/body/div[2]/div[3]/div/div/div/div[1]/section[1]/div/div/div/div[3]/div[5]/div[1]/div/span/button/i'
adobe_experienced_type='/html/body/div[2]/div[3]/div/div/div/div[1]/section[1]/div/div/div/div[3]/div[5]/div[2]/div/div[2]/fieldset/ul/li[2]/label/span[1]'

google_back_button='/html/body/div[1]/header/div[1]/div[2]/div/div/button'
adobe_job_location='/html/body/div[2]/div[3]/div/div[1]/div[2]/section/div/div/div/div[1]/section/div/div[1]/span[1]/span/text()'
adobe_job_title='/html/body/div[2]/div[3]/div/div[1]/div[2]/section/div/div/div/div[1]/h1'
google_job_description='//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[2]/div[2]'






def Adobe_job_experienced_scrape():
    index=1
    adobe_experienced=[]
    location=""
    description=""
    driver = webdriver.Chrome(options=options)
   
    driver.get(ADOBE_EXPERIENCED_URL)
    wait=WebDriverWait(driver,10)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/div/div/div/div[2]/button[2]/ppc-content'))).click()
    except:
        print("not there")
    wait.until(EC.element_to_be_clickable((By.XPATH,adobe_type))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,adobe_experienced_type))).click()

    while True:
        try:
            adobe_description='/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/p[3]'
            
            page0 = driver.execute_script('return document.body.innerHTML')
            soup0=BeautifulSoup(''.join(page0), 'lxml')
            dom0 = etree.HTML(str(soup0))
            try:
                description=dom0.xpath(adobe_description)[0].text
            except:
                driver.quit()
                break
            try:
                job_title=dom0.xpath('/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/span/a/div/span')[0].text
            except:
                driver.quit()
                break
            try:
                job_id=dom0.xpath('/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/p[1]/span[3]/span/span[2]')[0].text
            except:
                driver.quit()
                break
            job_t=job_title.replace('-','')
            job_t=job_t.replace(',','')
            job_t=job_t.replace('.','')
            job_t=job_t.replace('&','')
            job_t=job_t.replace(' ','-')
            try:
                location_t=dom0.xpath('/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[2]/ul/li['+str(index)+']/div[1]/div[1]/p[1]/span[1]/span/text()')
                
                l=0
                while(l<len(location_t)):
                    if(location_t[l]!='\n'):
                        location=location_t[l]
                        break
                    l=l+1
            except:
                location="Multiple Location"
            
            job_url='https://careers.adobe.com/us/en/job/'+job_id+'/'+job_t
        
        
            index+=1 
            #scraped information https://careers.adobe.com/us/en/job/R130911/Solutions-Architect
        
            
            job_data={
                'Company_Name':'Adobe',
                'Job_title':job_title,
                'Url':job_url,
                'Location':location,
                'Description':description
            } 
            adobe_experienced.append(job_data)
            
            #wait.until(EC.element_to_be_clickable((By.XPATH,amazon_back_button))).click() 
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
