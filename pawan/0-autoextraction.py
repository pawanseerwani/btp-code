#from __future__ import print_function
from oauth import oauth_login 
import twitter
import sys
import re 
import csv

DEBUG = 0

if(len(sys.argv) != 3) :
    print "Error: Incorrect usage. Use %s <product-name> <limit>" %(sys.argv[0]) 
    sys.exit(1)

input_file = sys.argv[1]
search_term=sys.argv[1]
limit = sys.argv[2]
limit = limit if limit < 100 else 100
twitter_api = oauth_login()
twitter_rest = twitter.Twitter(auth=twitter_api.auth)
#stream = twitter_stream.statuses.filter(track=search_term,language='en')
rest = twitter_rest.search.tweets(q=search_term)

if not DEBUG : 
 out = open('../2-extracted_tweets/'+input_file+'.csv','w') 
 writer = csv.writer(out, delimiter = '\t') 
 writer.writerow([
                    'username', 
                    'tweet', 
                    'timestamp',
                    ])

i = 0
prev_tweet = ''
for tweet in rest['statuses']:
    if int(i) == int(limit) :
        break
    i += 1
    demo_text = re.sub(r'[^\x00-\x7F]+','', tweet['text'])
    username =  tweet['user']['screen_name']
    tweet_text =  demo_text
    timestamp =  tweet['created_at']

    #if prev_tweet == tweet_text :
    #    i -= 1
    #    continue
    if DEBUG : 
      print username, tweet_text, timestamp
    else :
        #print i, limit
        writer.writerow([
            username, tweet_text, timestamp
        ])
    prev_tweet = tweet_text
if not DEBUG :
    out.close()
