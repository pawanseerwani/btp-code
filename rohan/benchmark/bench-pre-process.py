import re
import csv
import sys
#sys.argv	
out = open('./output/bench-preprocess-5.csv','w') 
writer = csv.writer(out, delimiter = '\t')
inp=open('./output/bench-input-5.txt','r')
inp=inp.read()
inp = re.sub('#+', '#' , inp)
inp=inp.split('#')
i=1
pos_count=0
neg_count=0
regex=ur'\[[+|-][0-9]\]'
for row in inp:
	old=row
	neg=0
	pos=0
	row=row.replace('[t]','')
	row=row.replace('[u]','')
	row=row.replace('[p]','')
	row=row.replace('[s]','')
	row=row.replace('[cc]','')
	row=row.replace('[cs]','')
	sentiments=re.findall(regex,row)
	for sent in sentiments:
		sent=sent.replace('[','')
		sent=sent.replace(']','')
		if sent[0]=='-':
			neg+=int(sent[1])
		else:
			pos+=int(sent[1])
	if pos>neg:
		opinion='positive'
		pos_count+=1
	elif pos<neg:
		opinion='negative'
		neg_count+=1
	else:
		opinion='neutral'

	row = re.sub('[^A-Za-z \[\]\$\.,-]', '' , row)    # removes spl chars
	row = re.sub('\[\]','',row)
	row = re.sub('\.+', '.', row) # replace multiple dots with single dot
	row = re.sub(' +', ' ', row) # replace multiple spaces with single space
	row = row.strip() # strips leading and trailingspaces
	writer.writerow(
                            [
                                i, # username
                                '', #old, # old inp
                                row, # pre processed inp
                                pos,
                                neg,
                                opinion

                            ])
	i+=1

print'positive: ',pos_count
print'negative: ',neg_count
print'total: ',i
print'percentage +: ', float(pos_count)/i
print'percentage -: ', float(neg_count)/i