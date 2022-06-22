from flask import Flask, render_template, jsonify, Response, request, url_for
from datetime import datetime
import json, operator

app = Flask(__name__)

@app.route('/') #could add methods post and get
def index_view():
    username = request.args.get('username')
    #this loads the webpage from template file
    return render_template('index.html', username = username)

@app.route('/timeline', methods = ['POST', 'GET'])
def timeline_view():
    if request.method == 'POST':
        result = request.form.to_dict()
        print(result)
        username = result['username']
        timeline = get_timeline(username)
        return render_template('timeline.html', user = username, result = timeline)
   
def get_timeline(username):
    #username = request.args.get('username')
    #print(username)
    #if username==None:
    #    username = 'Franc'
    
    #load users.json
    with open('./users.json', 'r') as f:
        users = f.read()
    users_data = json.loads(users)
    #users followed by user 
        
    try: 
        user_following = users_data[username]
        user_following.append(username)
        print(user_following)
        
        with open('./posts.json', 'r') as f:
            posts = f.read()
        posts_data = json.loads(posts)
        #users posts
        theposts = []
        all_posts = {}
        #all posts
        for user in user_following:    
            if posts_data[user] != []:
                #print (posts_data[user])
                #all_posts[user] = user
                #theposts.append(posts_data[user])
                all_posts[user] = posts_data[user]
            else:
                #all_posts[user] = user
                #print (posts_data[user])
                #theposts.append(posts_data[user])
                all_posts[user] = []
        #print(theposts[1][1]['time'])
        #filter
        
        #order posts
        for user in user_following:
            print(user)
            print(all_posts[user])
            if all_posts[user]!=[]:
                all_posts[user] = sorted(all_posts[user], key=operator.itemgetter('time'),reverse=True)
                print(all_posts[user])    
                
        """ 
        for post in user_posts:
            for key in post:
                print(post[key]) """
                
        #dict1 = user_posts[0]
        #print(dict1['status'])
        return all_posts
    except:
        
        return render_template('index.html')

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
    #users followed by user    
    user_following = users_data[username]
    user_following.append(username)
    print(user_following)
    
    with open('./posts.json', 'r') as f:
        posts = f.read()
    posts_data = json.loads(posts)
    #users posts
    theposts = []
    all_posts = {}
    #all posts
    for user in user_following:    
        if posts_data[user] != []:
            #print (posts_data[user])
            #all_posts[user] = user
            #theposts.append(posts_data[user])
            all_posts[user] = posts_data[user]
        else:
            #all_posts[user] = user
            #print (posts_data[user])
            #theposts.append(posts_data[user])
            all_posts[user] = []
    #print(theposts[1][1]['time'])
    #filter
    
    #order posts
    for user in user_following:
        print(user)
        print(all_posts[user])
        if all_posts[user]!=[]:
            all_posts[user] = sorted(all_posts[user], key=operator.itemgetter('time'),reverse=True)
            print(all_posts[user])    
            
    """ 
    for post in user_posts:
        for key in post:
            print(post[key]) """
            
    #dict1 = user_posts[0]
    #print(dict1['status'])
    return '''
            The posts for {} are: {}
            they are following: {} '''.format(username, all_posts, user_following)
    #return Response(data, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')