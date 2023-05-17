import threading
from Google import Google_scraper
from Adobe import Adobe_scraper
from Amazon import Amazon_scraper
from Cisco import Cisco_scraper
import evaluation
import json_convertor



def internship_data(user_skill):

    t1 = threading.Thread(target=Google_scraper.Google_job_internship_scrape)
    t2 = threading.Thread(target=Amazon_scraper.Amazon_job_internship_scrape)
    t3 = threading.Thread(target=Cisco_scraper.Cisco_job_internship_scrape)
    t4 = threading.Thread(target=Adobe_scraper.Adobe_job_internship_scrape)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Done! internship scrape")
    print(user_skill[0])
    try:
        evaluation.search('Amazon_internship_openings',user_skill)
    except:
        print("error amazon")
    
    try:
        evaluation.search('Google_internship_openings',user_skill)
    except:
        print("error google")

    try:
        evaluation.search('Adobe_internship_openings',user_skill)
    except:
        print("error adobe")

    try:
        evaluation.search('Cisco_internship_openings',user_skill)
    except:
        print("error cisco")
    
    fetched=json_convertor.main_conv('internship_jobs.json')
    return fetched

def newgrad_data(user_skill):
    t1 = threading.Thread(target=Google_scraper.Google_job_newgrad_scrape)
    t2 = threading.Thread(target=Amazon_scraper.Amazon_job_newgrad_scrape)
    t3 = threading.Thread(target=Cisco_scraper.Cisco_job_newgrad_scrape)
    t4 = threading.Thread(target=Adobe_scraper.Adobe_job_newgrad_scrape)


    t1.start()
    t2.start()
    t3.start()
    t4.start()


    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Done! newgrad")

    try:
        evaluation.search('Amazon_newgrad_openings',user_skill)
    except:
        print("error amazon")
    
    try:
        evaluation.search('Google_newgrad_openings',user_skill)
    except:
        print("error google")

    try:
        evaluation.search('Adobe_newgrad_openings',user_skill)
    except:
        print("error adobe")

    try:
        evaluation.search('Cisco_newgrad_openings',user_skill)
    except:
        print("error cisco")
    
    fetched=json_convertor.main_conv1('newgrad_jobs.json')
    return fetched

def experienced_data(user_skill):
    t1 = threading.Thread(target=Google_scraper.Google_job_experienced_scrape)
    t2 = threading.Thread(target=Amazon_scraper.Amazon_job_experienced_scrape)
    t3 = threading.Thread(target=Cisco_scraper.Cisco_job_experienced_scrape)
    t4 = threading.Thread(target=Adobe_scraper.Adobe_job_experienced_scrape)

    t1.start()
    t2.start()
    t3.start()
    t4.start()


    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Done! experienced")

    try:
        evaluation.search('Amazon_experienced_openings',user_skill)
    except:
        print("error amazon")
    
    try:
        evaluation.search('Google_experienced_openings',user_skill)
    except:
        print("error google")

    try:
        evaluation.search('Adobe_experienced_openings',user_skill)
    except:
        print("error adobe")

    try:
        evaluation.search('Cisco_experienced_openings',user_skill)
    except:
        print("error cisco")
    
    fetched=json_convertor.main_conv2('experienced_jobs.json')
    return fetched



# experienced_data()