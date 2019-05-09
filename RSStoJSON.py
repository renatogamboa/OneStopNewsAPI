import feedparser
import atoma
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

def CNN_topstories():
    d = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')

    return str(striphtml(json.dumps(d.entries)))
