from flask import Flask, request, render_template 
from TopaxAPI import get_html, get_last_link, get_new_posts
import bs4 as bs 
import vars 

import json 

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/watchTopic/", methods=['GET'])
def watch_topic() : 
    url = request.args.to_dict(flat=False)['url'][0]
    vars.topax = url 
    vars.data = get_html(vars.topax)
    vars.soup = bs.BeautifulSoup(vars.data,'lxml')

    # On va à la dernière page 

    link = get_last_link() 

    if link != None : 
        vars.topax = link 
        vars.data = get_html(vars.topax)
        vars.soup = bs.BeautifulSoup(vars.data,'lxml')

    return json.dumps({'response' : url})

@app.route("/getLastPosts/", methods=['GET'])
def get_last_posts() : 
    url = request.args.to_dict(flat=False)['url'][0]

    posts = get_new_posts() 

    return json.dumps({'posts' : posts})