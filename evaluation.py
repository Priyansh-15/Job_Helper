import pandas as pd
import random
import math

skill_index_map={'C++': 1, 'Python': 2,'Java': 3,'JavaScript': 4,'Dsa': 5 , 'Problem Solving': 6,'MySql': 7,'Web services':8, 'Html/Css': 9, 'Communication':10,'Team work' : 11, 'Leadership': 12, 'Adaptability': 13}


def get_skill_value(desc,skill,skill_l,skill_u):
    a=desc.count(skill)
    b=desc.count(skill_l)
    c=desc.count(skill_u)
    ind=max(a,max(b,c))
    if(ind==0):
        val=random.randint(1,4)
    elif(ind<=2):
        val=random.randint(5,8)
    else:
        val=random.randint(9,10)
    return val



def ecludian_distance(a,b):
    if((a*a)<(b*b)):
        return -math.sqrt((b*b)-(a*a))
    return math.sqrt((a*a)-(b*b))

def predictions(description,user_skills,skill_index_map):
    job_skills=[]
    for x in skill_index_map:
        job_skills.insert(skill_index_map[x]-1,get_skill_value(description,x,x.lower(),x.upper()))
    chances=[]
    for x in range(0,len(job_skills)):
        chances.append(ecludian_distance(user_skills[x],job_skills[x]))
    lose_skill=[]
    per=0
    temp = list(skill_index_map.items())

    for x in range (0,len(chances)):
        if(chances[x]<0):
            lose_skill.append(temp[x][0])
        else:
            per+=1
    per=per/len(chances)
    per*=100
   
    if(len(lose_skill)==0):
        lose_skill.append("no missing skills")
    return lose_skill,per


def search(file,user_skills): 
    print(file,user_skills)
    u=0
    while(u<len(user_skills)):
        user_skills[u]=int(user_skills[u])
        u=u+1

    csv = pd.read_csv('{}.csv'.format(file),encoding='utf-8')
    res_per = []
    lose_column=[]

    for i in range(csv.shape[0]):
        skills_to_work,percentage=predictions(csv.iloc[i, 4],user_skills,skill_index_map)
        str1=""
        for e in skills_to_work:
           str1+=e+','
        str1=str1[0:len(str1)-1]
        res_per.append(percentage)  
        lose_column.append(str1)

    csv['{}'.format('Missing_Skills')] =lose_column
    csv['{}'.format('Percentage')] = res_per

    csv.to_csv('{}.csv'.format(file), index=False)

# user_skill=[9,8,6,5,5,7,4,7,1,10,10,7,5]

# print(predictions('Proven experience as a Software Developer, Software Engineer or similar role Familiarity with Agile development methodologies Experience with software design and development in a test-driven environment Knowledge of coding languages (e.g. C++, Java, JavaScript) and frameworks/systems (e.g. AngularJS, Git) Experience with databases and Object-Relational Mapping (ORM) frameworks (e.g. Hibernate) Ability to learn new languages and technologies Excellent communication skills Resourcefulness and troubleshooting aptitude Attention to detail BSc/BA in Computer Science, Engineering or a related field',user_skill,skill_index_map))