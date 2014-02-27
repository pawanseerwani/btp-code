#!/usr/bin/env python
# coding: utf-8
import csv
from bs4 import BeautifulSoup

f = csv.writer(open("output-Hash-samsung-galaxy-note-gear.html.csv", "w"), delimiter = '\t')
f.writerow(["username", "time and date", "permalink", "tweettext", "URLlinked"]) #csv column headings
 
soup = BeautifulSoup(open("Hash-samsung-galaxy-note-gear.html")) #input html document


litop = soup.find_all("li", "js-stream-item stream-item stream-item expanding-stream-item") #li with class "js-stream-item..." form the anchor for each tweet. Where the link is specified below tells the code how to differentiate the ‘li’ values. It’s best to make sure that the input is English with latin characters.
#print litop
for li in litop:
    for link in li.find_all('li', 'js-stream-item stream-item stream-item expanding-stream-item'):
        link = li['id'][3]
    #print li
    divcont = li.find_all("div", "content")
    username = ""
    timedate = ""
    permalink = ""
    tweettext = ""
    URLlinked = ""
    try:
        username = li.find("span", "username js-action-profile-name").get_text() #sometimes this line will need to be changed to account for differences in the html files from different browers.
        timedate = li.find('a', "tweet-timestamp js-permalink js-nav js-tooltip").attrs['title'] #gets the time and date.
        permalink = li.find('a', "tweet-timestamp js-permalink js-nav js-tooltip").attrs['href'] #gets the permalink of the tweet. Adding https://www.twitter.com before it would link directly to the tweet on twitter.com.
        tweettext = li.find("p", "js-tweet-text tweet-text").get_text().encode('utf-8').replace('\n',"") #gets text of tweet, unfortunately it sometimes returns some other random characters as well. May need some fine tuning.
        URLlinked = li.find("a", "twitter-timeline-link").attrs['href'] #gives a URL given by a tweet. It seems safe to assume that users will only link one URL in their tweet.
       
    except: #this section duplicates the above when a URL is not found. Some fine tuning might negate the need for this section.
        print "no URL present"
        #username = li.find("span", "username js-action-profile-name").get_text()
        #timedate = li.find('a', "tweet-timestamp js-permalink js-nav").attrs['title']
        #permalink = li.find('a', "tweet-timestamp js-permalink js-nav").attrs['href']
        #tweettext = li.find("p", "js-tweet-text tweet-text").get_text().encode('utf-8').replace('\n',"")
        #URLlinked = ""
    print username, timedate, permalink, tweettext, URLlinked   
    f.writerow([username, timedate, permalink, tweettext, URLlinked]) #order in which outputs are placed in csv file, probably best to keep URLlinked at the end as not all entries will have these. The order does not matter.