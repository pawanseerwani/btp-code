DEBUG = 0

import csv
from senti_classifier import senti_classifier

if not DEBUG : 
    out = open('/home/rohan/Desktop/input/output-1-sent.csv','w') 
    writer = csv.writer(out, delimiter = '\t') 

inp = open('/home/rohan/Desktop/input/output-1-lem.csv','r')
reader = csv.reader(inp)

for row in reader : 
    row_str = str(row)[2:-2] #convert the row to string ignoring the square brackets and single quote
    row_arr = row_str.split('\\t') # split the string with tab delimiter
    tweet = row_arr[2] # 2 is the index of tweet text
    if tweet == '':
    	continue
    tweet=[tweet]
    pos,neg=senti_classifier.polarity_scores(tweet)

    if DEBUG:
        print (pos,neg)

    
    if not DEBUG :
        if pos>neg:
            sentiment='positive'
        elif pos<neg:
            sentiment='negative'
        else:
            sentiment='neutral'
        writer.writerow(
                            [
                                row_arr[0], # username
                                row_arr[1], #original tweet
                                row_arr[2], # tweet
                                pos, #positive score
                                neg, #negative score
                                sentiment #sentiment
                                ])
