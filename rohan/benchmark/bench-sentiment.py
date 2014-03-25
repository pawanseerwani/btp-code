DEBUG = 0

import csv
from senti_classifier import senti_classifier

if not DEBUG : 
    out = open('./output/bench-sent-5.csv','w') 
    writer = csv.writer(out, delimiter = '\t') 

inp = open('./output/bench-lem-5.csv','r')
reader = csv.reader(inp)
i=1
pos_count=0
neg_count=0
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
            pos_count+=1
        elif pos<neg:
            sentiment='negative'
            neg_count+=1
        else:
            sentiment='neutral'
        writer.writerow(
                            [
                                row_arr[0], # username
                                row_arr[1], #original tweet
                                row_arr[2], # tweet
                                row_arr[3], #pos
                                row_arr[4], #neg
                                row_arr[5], #opinion
                                pos, #positive score
                                neg, #negative score
                                sentiment #sentiment
                                ])
    i+=1

print'positive: ',pos_count
print'negative: ',neg_count
print'total: ',i
print'percentage +: ', float(pos_count)/i
print'percentage -: ', float(neg_count)/i


