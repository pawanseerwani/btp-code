import csv
from senti_classifier import senti_classifier

out = open('./output/bench-compared-5.csv','w') 
writer = csv.writer(out, delimiter = '\t')
writer.writerow(['actual sentiment - small letters','','','','','','','','our sentiment - capital letters'])
writer.writerow(['posPOS','posNEG','posNEU','negPOS','negNEG','negNEU','neuPOS','neuNEG','neuNEU','POShitRATIO','NEGhitRATIO','NEUhitRATIO'])

inp = open('./output/bench-sent-5.csv','r')
reader = csv.reader(inp)
#actual sentiment - small letters
#our sentiment - capital letters
#row_arr[5] ->actual.........row_arr[8] ->our calculated
posPOS=0
posNEG=0
posNEU=0
negPOS=0
negNEG=0
negNEU=0
neuPOS=0
neuNEG=0
neuNEU=0

for row in reader : 
    row_str = str(row)[2:-2] #convert the row to string ignoring the square brackets and single quote
    row_arr = row_str.split('\\t') # split the string with tab delimiter
    if len(row_arr)<8:
    	continue
    if row_arr[5]=='positive':
    	if row_arr[8]=='positive':
    		posPOS+=1
    	elif row_arr[8]=='negative':
    		posNEG+=1
    	else:
    		posNEU+=1
    elif row_arr[5]=='negative':
    	if row_arr[8]=='positive':
    		negPOS+=1
    	elif row_arr[8]=='negative':
    		negNEG+=1
    	else:
    		negNEU+=1
    else:
    	if row_arr[8]=='positive':
    		neuPOS+=1
    	elif row_arr[8]=='negative':
    		neuNEG+=1
    	else:
    		neuNEU+=1
a=float(posPOS)/(posPOS+posNEU+posNEG)
b=float(negNEG)/(negNEG+negPOS+negNEU)
c=float(neuNEU)/(neuNEU+neuNEG+neuPOS)
writer.writerow(
                            [
                            posPOS,
                            posNEG,
                            posNEU,
                            negPOS,
                            negNEG,
                            negNEU,
                            neuPOS,
                            neuNEG,
                            neuNEU,
                            a,
                            b,
                            c
                                
                                ])	
