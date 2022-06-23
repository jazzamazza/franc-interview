from flask import Flask, redirect, render_template, jsonify, Response, request, url_for
from datetime import datetime
import json, operator

app = Flask(__name__)

@app.route('/')
def index_view():
    #username = request.args.get('username')
    #this loads the webpage from template file
    return render_template('index.html')

@app.route('/timeline', methods = ['POST', 'GET'])
def timeline_view():
    if request.method == 'POST':
        #get username from form
        username = request.form.get('username')
        try:
            timeline = get_timeline(username)
            return render_template('timeline.html', user = username, timeline = timeline)
        except:
            #not really an exception but if user isnt found just get returned to homepage
            return redirect('/')
 
#method to get timeline posts returns an ordered list of dictionaries       
def get_timeline(username):
    #load users.json
    with open('./users.json', 'r') as f:
        users = f.read()
    users_data = json.loads(users)
    f.close()

    #list of users to get tweets from incl. user itself
    user_following = users_data[username]
    user_following.append(username)
    
    #load posts.json
    with open('./posts.json', 'r') as f:
        posts = f.read()
    posts_data = json.loads(posts)
    f.close()
    
    #create list of all posts for timeline
    all_posts = []
    user_posts = {}
    for user in user_following:  
        #make sure user has posts  
        if posts_data[user] != []:
            for post in posts_data[user]:
                #get post dictionary
                user_posts = post
                #add user to dictionary containing post
                user_posts['username'] = user
                #add post to all posts
                all_posts.append(user_posts)
        else:
        #not really an error but at users with no posts are ignored
           print('Error: '+ user + ' has no posts')
    
    #order posts by time in descending order
    sorted_posts = sorted(all_posts, key=lambda by_item: by_item['time'], reverse=True)
    
    return sorted_posts

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

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')