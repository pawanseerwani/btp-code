#!/usr/bin/env python

DEBUG = 0

import csv
import re
inp = open('../input/output-199.csv','r')

if not DEBUG : 
 out = open('output-199-pp.csv','w') 
 writer = csv.writer(out, delimiter = '\t') 
try :
    reader = csv.reader(inp)
    if not DEBUG :
        writer.writerow([
                        'username', 
                        'old_tweet', 
                        'pre_processed_tweet',
                        'hash_tags',
                        'exclamation count'
                        ])
    for row in reader : 
        row_str = str(row)[2:-2] #convert the row to string ignoring the square brackets and single quote
        row_arr = row_str.split('\\t') # split the string with tab delimiter
        #row_arr[3] = row_arr[3].decode('unicode')
        row_arr[3] = row_arr[3].decode('UTF-8')
        tweet_text = row_arr[3] # 3 is the index of tweet text
        tweet_text = tweet_text.encode('ascii', 'ignore')
        tweet_text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '' , tweet_text) # removes urls
        tweet_text = re.sub('pic\.twitter\.com[^ ]*', '', tweet_text ) # removes urls
        tweet_text = re.sub('@[^ ]*', '', tweet_text) # remove usernames
        tweet_text = re.sub('^RT','', tweet_text)  # remove RT : Reply-to
        hash_arr = re.findall('#[^ ]*', tweet_text) # extracts hash tags 
        hash_arr = [ re.sub('[^A-Za-z0-9]', '', word)  for word in hash_arr ] # removes spl chars from hash_arr
        exc_count = tweet_text.count('!')

        #remove hash tags at the end
        hash_split = tweet_text.split('#')
        tweet_text = '#'.join([ word for word in hash_split if word.count(' ') > 1 ] )
        #tweet_text = re.sub('\x..','',tweet_text) # remove encoding chars like \x23 \xd3
        tweet_text = re.sub('[^A-Za-z0-9 \$\.,-]', '' , tweet_text)    # removes spl chars
        tweet_text = re.sub('-', ' ' , tweet_text)    # removes spl chars
        tweet_text = re.sub('\.+', '.', tweet_text) # replace multiple dots with single dot
        tweet_text = re.sub(' +', ' ', tweet_text) # replace multiple spaces with single space
        tweet_text = tweet_text.strip() # strips leading and trailingspaces
        
        #for i in len(tweet_text) :

        if DEBUG :
            print row_arr[0]
            print row_arr[3], type(row_arr[3])
            print tweet_text, type(tweet_text)
            print ','.join(hash_arr)
            print exc_count
            print '\n'
            raw_input()
        if not DEBUG : 
            #Write to a new csv
            writer.writerow(
                            [
                                row_arr[0], # username
                                row_arr[3], # old tweet_text
                                tweet_text, # pre processed tweet_text
                            #TODO : join the hash_arr with ,
                                ','.join(hash_arr),    # hashtags in text
                                exc_count

                                ])
finally:
    inp.close()
    if not DEBUG :
        out.close()
