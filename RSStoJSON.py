import feedparser
import requests
import json
import xmltodict
import re

#for post in d.entries:
#    print (post['title'] + ": " + post['link'] + "\n")

# Filtered List Test
filtered_list = ['title', 'summary']

# Strip HTML data
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# CNN Parse Function
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


# New York Times Parse Function
def NYT(category):
    # URL to be parse
    URL = ""
    # Piece of URL
    tag = ""
    
    
    # Categories
    if category == "top-stories":
        #http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
        tag = "MostViewed"
    elif category == "world":
        tag = "World"
    elif category == "us":
        tag = "US"
    elif category == "business":
        tag = "Business"
    elif category == "politics":
        tag = "Politics"
    elif category == "technology":
        tag = "Technology"
    elif category == "health":
        tag = "Health"
    elif category == "entertainment":
        tag = "Sports" 
    elif category == "travel":
        tag = "Travel"
    elif category == "latest":
        tag = "HomePage"
    else:
        tag = "MostViewed"

    # Concatenated URL with category
    URL = "http://rss.nytimes.com/services/xml/rss/nyt/" + tag + ".xml"

    # Parse URL
    d = feedparser.parse(URL)

    # Return json version of RSS entries stripped of any HTML tags
    return str(striphtml(json.dumps(d.entries)))


# Huffington Post Parse Function
def Huff(category):
    # URL to be parse
    URL = ""
    # Piece of URL
    tag = ""


    # Categories
    if category == "top-stories":
        tag = "fifty"
    elif category == "world":
        tag = "world-news"
    elif category == "us":
        #https://www.huffpost.com/section/us-news/feed
        tag = "us-news"
    elif category == "business":
        tag = "business"
    elif category == "politics":
        tag = "politics"
    elif category == "technology":
        tag = "technology"
    elif category == "health":
        tag = "health"
    elif category == "entertainment":
        tag = "entertainment" 
    elif category == "travel":
        tag = "travel"
    elif category == "latest":
        tag = "fifty"
    else:
        tag = "fifty"



    # Concatenated URL with category
    URL = "https://www.huffpost.com/section/" + tag + "/feed"

    # Parse URL
    d = feedparser.parse(URL)

    # Return json version of RSS entries stripped of any HTML tags
    return str(striphtml(json.dumps(d.entries)))