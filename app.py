from time import time
from flask import Flask, render_template, jsonify, Response, request, url_for
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/') #could add methods post and get
def index_view():
    username = request.args.get('username')
    #this loads the webpage from template file
    return render_template('index.html', username = username)

@app.route('/timeline')
def timeline_view():
    return render_template('timeline.html')

@app.route('/users')
def users_view():
    with open('./users.json', 'r') as f:
        users = f.read()
    return Response(users, mimetype="application/json")

@app.route('/posts')
def posts_view():
    with open('./posts.json', 'r') as f:
        posts = f.read()
    return Response(posts, mimetype="application/json")

@app.route('/test/', methods=['POST', 'GET'])
def test_view():
    username = request.args.get('username')
    #print(username)
    if username==None:
        username = 'Franc'
    
    #load users.json
    with open('./users.json', 'r') as f:
        users = f.read()
    users_data = json.loads(users)
        
    user_following = users_data[username]
    
    with open('./posts.json', 'r') as f:
        posts = f.read()
    posts_data = json.loads(posts)
    user_posts = posts_data[username]
    
    #timeline = 
    
    for user in user_following:
        with open('./posts.json', 'r') as f:
            posts = f.read()
            
    user_following.append(username)
    
    
    
    #filter
    for post in user_posts:
        for key in post:
            print(post[key])
            
    #dict1 = user_posts[0]
    #print(dict1['status'])
    return '''
            The posts for {} are: {}
            they are following: {} '''.format(username, user_posts, user_following)
    #return Response(data, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')