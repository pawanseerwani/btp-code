#!/usr/bin/env python
DEBUG = 0

import csv
import sys

allowed_brands = ["apple", "samsung", "ms", "sony", "nike", "adidas"]
allowed_products = [] #TODO
brand = ""
product = ""
feature = "" #TODO

'''
if(len(sys.argv) != 3) :
    print "Error: Incorrect usage. Use %s <brand-name> <product-name>" %(sys.agrv[0]) 
    sys.exit(1)


brand = sys.argv[1]
product = sys.agrv[2]
'''
from senti_classifier import senti_classifier

if not DEBUG : 
    out = open('../5-sentiment_analyzed_tweets/1.htm.csv','w') 
    writer = csv.writer(out, delimiter = '\t') 

inp = open('../4-lemmatized_tweets/1.htm.csv','r')
reader = csv.reader(inp)

writer.writerow(
                    [
                        "Brand",
                        "Product",
                        "Feature(s)",
                        "sentiment",
                        "tweet"
                    ]
                )


i = 0
for row in reader : 
    i+=1
    if i == 1 :
        continue

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
            #sentiment='positive'
            sentiment = 1
        elif pos<neg:
            #sentiment='negative'
            sentiment = -1
        else:
            #sentiment='neutral'
            sentiment = 0
        writer.writerow(
                            [
                                #row_arr[0], # username
                                #row_arr[1], #original tweet
                                brand,
                                product,
                                feature,
                                row_arr[2], # tweet
                                sentiment
                                #pos, #positive score
                                #neg, #negative score
                                #sentiment #sentiment
                                ])
