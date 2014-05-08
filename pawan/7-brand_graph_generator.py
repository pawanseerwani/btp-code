from pylab import *
import csv
import re

import sys
if(len(sys.argv) != 3) :
    print "Error: Incorrect usage. Use %s <brand1> <brand2>" %(sys.argv[0]) 
    sys.exit(1)

brand0 = sys.argv[1]
brand1 = sys.argv[2]

inp = open('../6-brand_analysed_tweets/product_review_count.csv','rU')
reader = csv.reader(inp,dialect=csv.excel_tab)

brand_count = [ { 'name': brand0 ,  'pos' : 0, 'neg': 0, 'neu' : 0} ,  {'name': brand1, 'pos' : 0, 'neg': 0, 'neu' : 0} ]
for row in reader :
    if row[0] == brand0 : 
        brand_count[0]['pos'] += int(row[2])
        brand_count[0]['neg'] += int(row[3])
        brand_count[0]['neu'] += int(row[4])

    if row[0] == brand1 : 
        brand_count[1]['pos'] += int(row[2])
        brand_count[1]['neg'] += int(row[3])
        brand_count[1]['neu'] += int(row[4])



for i in range(2) :
    positive = brand_count[i]['pos']
    negative = brand_count[i]['neg']
    neutral = brand_count[i]['neu']

    total = positive + negative + neutral 

    if(total == 0 ) :
        sys.exit("Error: No data for graph generation")

    pos_frac = int(positive*100 /total)
    neg_frac = int(negative*100/total)
    neu_frac = 100 - (pos_frac + neg_frac)

    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Positive', 'Negative', 'Neutral'
    fracs = [pos_frac, neg_frac, neu_frac]
    explode=(0.05, 0, 0)

    pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True)#, startangle=90)
    # The default startangle is 0, which would start
    # the Frogs slice on the x-axis.  With startangle=90,
    # everything is rotated counter-clockwise by 90 degrees,
    # so the plotting starts on the positive y-axis.

    title('Brand :'+ brand_count[i]['name'], bbox={'facecolor':'0.8', 'pad':5})
    output = brand_count[i]['name'] + '.png'
    savefig('../7-graphs/brand_'+output)
    close()
