import pandas as pd
import json
import numpy as np
import random

google_logo='https://static.vecteezy.com/system/resources/previews/009/469/630/original/google-logo-isolated-editorial-icon-free-vector.jpg'
amazon_logo='https://www.citypng.com/public/uploads/preview/-11596400565qsuxfwyv9j.png'
cisco_logo='https://cdn-icons-png.flaticon.com/512/882/882730.png'
adobe_logo='https://static.cdnlogo.com/logos/a/89/adobe-thumb.png'


def conv(file): 
    job_data = []
    csv = pd.read_csv('{}.csv'.format(file),encoding='utf-8')
    for i in range(csv.shape[0]):
        pic=""
        if(csv.iloc[i,0]=='Google'):
            pic=google_logo
        elif(csv.iloc[i,0]=='Amazon'):
            pic=amazon_logo
        elif(csv.iloc[i,0]=='Adobe'):
            pic=adobe_logo
        elif(csv.iloc[i,0]=='Cisco'):
            pic=cisco_logo
        loca=""
        if(len(csv.iloc[i,3])>0):
            loca=csv.iloc[i,3]
        else:
            loca="NAN"
        job_inst={
                    'Company_Name':csv.iloc[i,0],
                    'Job_title':csv.iloc[i,1],
                    'Url':csv.iloc[i,2],
                    'Job_Location':loca,
                    'Description':csv.iloc[i,4][0:200],
                    'Percentage':csv.iloc[i,6],
                    'Missing_Skills':csv.iloc[i,5],
                    'image_url':pic
                } 
        job_data.append(job_inst)
    return job_data
    


def main_conv(category):
    job_col=[]
    try:
        google_d=conv('Google_internship_openings')
        for g in google_d:
            job_col.append(g)
    except:
        print("error google")
    try:
        amazon_d=conv('Amazon_internship_openings')
        for a in amazon_d:
            job_col.append(a)
    except:
        print("error amazon")
    try:
        adobe_d=conv('Adobe_internship_openings')
        for ad in adobe_d:
            job_col.append(ad)
    except:
        print("error adobe")
    try:
        cisco_d=conv('Cisco_internship_openings')
        for c in cisco_d:
            job_col.append(c)
    except:
        print("error cisco")

    random.shuffle(job_col)
    json_object = json.dumps(job_col)
    
    # Writing to sample.json
    with open(category, "w") as outfile:
        outfile.write(json_object)

    return json_object

def main_conv1(category):
    job_col=[]
    try:
        google_d=conv('Google_newgrad_openings')
        for g in google_d:
            job_col.append(g)
    except:
        print("error google")
    try:
        amazon_d=conv('Amazon_newgrad_openings')
        for a in amazon_d:
            job_col.append(a)
    except:
        print("error amazon")
    try:
        adobe_d=conv('Adobe_newgrad_openings')
        for ad in adobe_d:
            job_col.append(ad)
    except:
        print("error adobe")
    try:
        cisco_d=conv('Cisco_newgrad_openings')
        for c in cisco_d:
            job_col.append(c)
    except:
        print("error cisco")

    random.shuffle(job_col)
    json_object = json.dumps(job_col)
    
    # Writing to sample.json
    with open(category, "w") as outfile:
        outfile.write(json_object)
        
    return json_object

def main_conv2(category):
    job_col=[]
    try:
        google_d=conv('Google_experienced_openings')
        for g in google_d:
            job_col.append(g)
    except:
        print("error google")
    try:
        amazon_d=conv('Amazon_experienced_openings')
        for a in amazon_d:
            job_col.append(a)
    except:
        print("error amazon")
    try:
        adobe_d=conv('Adobe_experienced_openings')
        for ad in adobe_d:
            job_col.append(ad)
    except:
        print("error adobe")
    try:
        cisco_d=conv('Cisco_experienced_openings')
        for c in cisco_d:
            job_col.append(c)
    except:
        print("error cisco")

    random.shuffle(job_col)
    json_object = json.dumps(job_col)
    
    # Writing to sample.json
    with open(category, "w") as outfile:
        outfile.write(json_object)
        
    return json_object


