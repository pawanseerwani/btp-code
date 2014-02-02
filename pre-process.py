#!/usr/bin/env python

DEBUG = 1

import csv
import re
inp = open('output-35.csv','r')

if not DEBUG : 
 out = open('output-35-pp.csv','w') 
 writer = csv.writer(out, delimiter = '\t') 
try :
    reader = csv.reader(inp)
    for row in reader : 
        row_str = str(row)[2:-2] #convert the row to string ignoring the square brackets and single quote
        row_arr = row_str.split('\\t') # split the string with tab delimiter
        tweet_text = row_arr[3] # 3 is the index of tweet text
        #tweet_text = tweet_text.decode('ascii', 'ignore')
        #Part 1
        tweet_text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '' , tweet_text) # removes urls
        tweet_text = re.sub('pic\.twitter\.com[^ ]*', '', tweet_text )
        tweet_text = re.sub('@[^ ]*', '', tweet_text) # removes tagged users
        #Part 2
        tweet_text = re.sub('\.+', '\.', tweet_text) # replace multiple dots with single dot
        #Part 3
        tweet_text = re.sub(' +', ' ', tweet_text) # replace multiple spaces with single space
        #Part 4
        tweet_text = tweet_text.strip() # strips leading and trailingspaces
        #Part 5
        tweet_text = re.sub('[^A-Za-z0-9 .,!-$]*', '' , tweet_text)
        #Part 6
        hash_arr  = re.findall('#[^ ]*', tweet_text) # extracts hash tags 
        tweet_text = re.sub('#[^ ]*', '', tweet_text) # removes hash tags
       
        print row_arr[0]
        print row_arr[3]
        print tweet_text
        print hash_arr
        print '\n'
        #raw_input()
        if not DEBUG : 
            #Write to a new csv
            writer.writerrow(
                            [
                                row_arr[0], # username
                                row_arr[3], # old tweet_text
                                tweet_text, # pre processed tweet_text
                                hash_arr    # hashtags in text
                                ])
finally:
    inp.close()
    if not DEBUG :
        out.close()
