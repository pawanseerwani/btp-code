#!/usr/bin/env python

DEBUG = 0

import csv
import re

import sys
if(len(sys.argv) != 2) :
    print "Error: Incorrect usage. Use %s <raw-html-file-name>" %(sys.argv[0]) 
    sys.exit(1)

input_file = sys.argv[1]

inp = open('../2-extracted_tweets/'+input_file+'.csv','r')

if not DEBUG : 
 out = open('../3-preprocessed_tweets/'+input_file+'.csv','w') 
 writer = csv.writer(out, delimiter = '\t') 

reader = csv.reader(inp)
if not DEBUG :
    writer.writerow([
                    'username', 
                    'old_tweet', 
                    'pre_processed_tweet',
                    'hash_tags',
                    'exclamation count'
                    ])
i=0
for row in reader : 
    if i == 0 :
        i += 1
        continue

    
    try :
        row_arr = row[0].split('\t') # split the string with tab delimiter
        username = row_arr[0]
        tweet = row_arr[1]
        username = [ username[i] for i in range(len(username)) if username[i].isalnum() or username[i] == ' ' ]
        tweet = [ tweet[i] for i in range(len(tweet)) if tweet[i].isalnum() or tweet[i] == ' ' ]
        username = ''.join(username)
        tweet = ''.join(tweet)

        #row_arr[1] = u' '.join(row_arr[1]).encode('utf-8').strip()
        #row_arr[1] = row_arr[1].decode('UTF-8')
        tweet_text = tweet
        #tweet_text = tweet_text.encode('ascii', 'ignore')
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
            #print row_arr[0]
            print row_arr[1]
            print tweet_text
            #print ','.join(hash_arr)
            #print exc_count
            print '\n'
            raw_input()
        else : 
            #Write to a new csv
                writer.writerow(
                                [
                                    row_arr[0], # username
                                    row_arr[1], # old tweet_text
                                    tweet_text, # pre processed tweet_text
                                #TODO : join the hash_arr with ,
                                    ','.join(hash_arr),    # hashtags in text
                                    exc_count

                                    ])
    except Exception as e:
        if DEBUG :
            print "error:"+str(e)

        
            


inp.close()
if not DEBUG :
    out.close()