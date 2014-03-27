#!/usr/bin/env python
# coding: utf-8
DEBUG = 0
import csv
from bs4 import BeautifulSoup

f = csv.writer(open("../2-extracted_tweets/1.htm.csv", "wb+"), delimiter = '\t')
f.writerow(["username", "tweet_text"]) #csv column headings
 
soup = BeautifulSoup(open("../1-raw_html/1.htm")) #input html document


contents = soup.find_all("div", "content") 
#print litop
for row in contents:
    username = ""
    tweet_text = ""
    try:
        username = row.find_all("span","username js-action-profile-name")[0].text.encode('utf8')
        tweet_text = row.find_all("p","js-tweet-text tweet-text")[0].text.encode('utf8')
        if DEBUG :
            print username,tweet_text
        else :
            f.writerow( [username, tweet_text] )
    except:
        if DEBUG :
            print "error in fetching"

    

    
