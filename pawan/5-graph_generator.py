from pylab import *
import csv
import re

import sys
if(len(sys.argv) != 2) :
    print "Error: Incorrect usage. Use %s <output-filename>" %(sys.argv[0]) 
    sys.exit(1)

output = sys.argv[1] + ".png"

inp = open('../6-brand_analysed_tweets/product_review_count.csv','rU')
reader = csv.reader(inp,dialect=csv.excel_tab)
for row in reader :
    last_row = row

brand = last_row[0]
product = last_row[1]
positive = int(last_row[2])
negative = int(last_row[3])
neutral = int(last_row[4])

total = positive + negative + neutral
if(total == 0) :
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

title(product + ' (' + brand + ')', bbox={'facecolor':'0.8', 'pad':5})

savefig('../7-graphs/'+output)
