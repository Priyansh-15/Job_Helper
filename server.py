# import main Flask class and request object
from flask import Flask, request
import main
import time
from flask_cors import CORS
# create the Flask app
app = Flask(__name__)
CORS(app)

@app.route('/experienced_api',methods=['GET'])
def query_example():
    user_skills=[]
    user_skills.append(request.args.get('c', None))
    user_skills.append(request.args.get('py', None))
    user_skills.append(request.args.get('j', None))
    user_skills.append(request.args.get('js', None))
    user_skills.append(request.args.get('dsa', None))
    user_skills.append(request.args.get('ps', None))
    user_skills.append(request.args.get('sql', None))
    user_skills.append(request.args.get('wb', None))
    user_skills.append(request.args.get('hs', None))
    user_skills.append(request.args.get('co', None))
    user_skills.append(request.args.get('t', None))
    user_skills.append(request.args.get('l', None))
    user_skills.append(request.args.get('a', None))
    data=main.experienced_data(user_skills)
    return data

@app.route('/internship_api', methods=['GET'])
def form_example():
    user_skills=[]
    user_skills.append(request.args.get('c', None))
    user_skills.append(request.args.get('py', None))
    user_skills.append(request.args.get('j', None))
    user_skills.append(request.args.get('js', None))
    user_skills.append(request.args.get('dsa', None))
    user_skills.append(request.args.get('ps', None))
    user_skills.append(request.args.get('sql', None))
    user_skills.append(request.args.get('wb', None))
    user_skills.append(request.args.get('hs', None))
    user_skills.append(request.args.get('co', None))
    user_skills.append(request.args.get('t', None))
    user_skills.append(request.args.get('l', None))
    user_skills.append(request.args.get('a', None))
    print(user_skills)
    data=main.internship_data(user_skills)
    return data

@app.route('/newgrad_api',methods=['GET'])
def json_example():
    user_skills=[]
    user_skills.append(request.args.get('c', None))
    user_skills.append(request.args.get('py', None))
    user_skills.append(request.args.get('j', None))
    user_skills.append(request.args.get('js', None))
    user_skills.append(request.args.get('dsa', None))
    user_skills.append(request.args.get('ps', None))
    user_skills.append(request.args.get('sql', None))
    user_skills.append(request.args.get('wb', None))
    user_skills.append(request.args.get('hs', None))
    user_skills.append(request.args.get('co', None))
    user_skills.append(request.args.get('t', None))
    user_skills.append(request.args.get('l', None))
    user_skills.append(request.args.get('a', None))
    data=main.newgrad_data(user_skills)
    return data

@app.route('/api',methods=['GET'])

def json_example1():
    time.sleep(5)
    response="api working"
    
    return response

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)