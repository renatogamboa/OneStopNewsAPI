import feedparser
import requests
import json
import xmltodict
import re

#for post in d.entries:
#    print (post['title'] + ": " + post['link'] + "\n")

filtered_list = ['title', 'summary']

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def CNN(category):
    
    # URL to be parse
    URL = ""
    # Piece of URL
    tag = ""
    
    
    # Categories
    if category == "top-stories":
        tag = "cnn_topstories"
    elif category == "world":
        tag = "cnn_world"
    elif category == "us":
        tag = "cnn_us"
    elif category == "business":
        tag = "money_latest"
    elif category == "politics":
        tag = "cnn_allpolitics"
    elif category == "technology":
        tag = "cnn_tech"
    elif category == "health":
        tag = "cnn_health"
    elif category == "entertainment":
        tag = "cnn_showbiz"
    elif category == "travel":
        tag = "cnn_travel"
    elif category == "latest":
        tag = "cnn_latest"
    else:
        tag = "cnn_topstories"


    # Concatenated URL with category
    URL = "http://rss.cnn.com/rss/" + tag + ".rss"

    # Parse URL
    d = feedparser.parse(URL)

    # Return json version of RSS entries stripped of any HTML tags
    return str(striphtml(json.dumps(d.entries)))
