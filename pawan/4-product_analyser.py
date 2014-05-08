#!/usr/bin/env python
DEBUG = 0

import csv
import sys
from senti_classifier import senti_classifier

brand = ""
product = ""
feature = "" #TODO

if(len(sys.argv) != 4) :
    print "Error: Incorrect usage. Use %s <lemmatized-tweets-file-name> <brand-name> <product-name>" %(sys.argv[0]) 
    sys.exit(1)

input_file = sys.argv[1]
brand = sys.argv[2]
product = sys.argv[3]
output_file = brand+'_'+product


if not DEBUG : 
    #product wise results
    out = open('../5-product_analysed_tweets/'+output_file+'.csv','w') 
    writer = csv.writer(out, delimiter = '\t') 
    writer.writerow(
                    [
                        "tweet",
                        "sentiment",
                        "original_tweet"                        
                    ]
                )


inp = open('../4-lemmatized_tweets/'+input_file+'.csv','rU')
reader = csv.reader(inp,dialect=csv.excel_tab)



i = 0
count_pos = 0
count_neg = 0
count_neu = 0

prev_tweet=''

for row in reader : 
    i+=1
    if i == 1 :
        continue

    #row_str = str(row)[2:-2] #convert the row to string ignoring the square brackets and single quote
    #row_arr = row_str.split('\\t') # split the string with tab delimiter
    #tweet = row_arr[2] # 2 is the index of tweet text
    row_arr = row
    tweet = row[2]
    if tweet == '' or tweet == prev_tweet:
    	continue
    prev_tweet = tweet
    tweet=[tweet]
    pos,neg=senti_classifier.polarity_scores(tweet)
    #pos,neg = 0,0

    if DEBUG:
        print (pos,neg)

    
    if not DEBUG :
        if pos>neg:
            #sentiment='positive'
            sentiment = 1
            count_pos += 1
        elif pos<neg:
            #sentiment='negative'
            sentiment = -1
            count_neg += 1
        else:
            #sentiment='neutral'
            sentiment = 0
            count_neu += 1
        writer.writerow(
                            [
                                #row_arr[0], # username
                                #row_arr[1], #original tweet
                                row[2], # tweet
                                sentiment,
                                row[1], #original_tweet
                                #pos, #positive score
                                #neg, #negative score
                                #sentiment #sentiment
                                ])


#this is static, do not change the output file name, all product reviews go into this file
out_file = open('../6-brand_analysed_tweets/product_review_count.csv','a') 
out_writer = csv.writer(out_file, delimiter = '\t') 

'''
out_writer.writerow(
                [
                    "Brand",
                    "Product",
                    "positive_count",
                    "negative_count",
                    "neutral_count"
                ]
            )
'''
out_writer.writerow(
                [
                    brand,
                    product,
                    count_pos,
                    count_neg,
                    count_neu
                ]
            )
