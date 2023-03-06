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

MICROSOFT_INTERNSHIP_URL = "https://jobs.cisco.com/jobs/SearchJobs/?21180=%5B165%5D&21180_format=6022&21181=%5B186%2C194%2C187%2C55816092%5D&21181_format=6023&listFilterMode=1"
MICROSOFT_NEWGRAD_URL ="https://jobs.cisco.com/jobs/SearchJobs/?21180=%5B164%5D&21180_format=6022&21181=%5B186%2C194%2C187%2C55816092%5D&21181_format=6023&listFilterMode=1"
MICROSOFT_EXPERIENCED_URL ="https://jobs.cisco.com/jobs/SearchJobs/?21180=%5B163%5D&21180_format=6022&21181=%5B186%2C194%2C187%2C55816092%5D&21181_format=6023&listFilterMode=1"
fieldnames = ['Company_Name','Job_title','Url','Location','Description']

