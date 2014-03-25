DEBUG = 0
thresh_noun=100
thresh_verb=100
thresh_adj=100
thresh_adv=100

import csv
import nltk
from nltk.corpus.reader.wordnet import VERB
from nltk.corpus.reader.wordnet import ADJ
from nltk.corpus.reader.wordnet import ADV
from nltk.corpus.reader.wordnet import NOUN
wnl=nltk.stem.WordNetLemmatizer()

if not DEBUG : 
    out = open('./output/bench-lem-5.csv','w') 
    writer = csv.writer(out, delimiter = '\t') 

inp = open('./output/bench-preprocess-5.csv','r')
reader = csv.reader(inp)

dic_noun = {}
dic_verb = {}
dic_adj = {}
dic_adv  = {}

for row in reader : 
    row_str = str(row)[2:-2] #convert the row to string ignoring the square brackets and single quote
    row_arr = row_str.split('\\t') # split the string with tab delimiter
    tweet = row_arr[2] # 3 is the index of tweet text
    if tweet == '':
    	continue
    tweet=tweet.decode("utf8")
    tweet=tweet.lower()
    tweet=nltk.word_tokenize(tweet)
    tweet=nltk.pos_tag(tweet)
    lem_tweet = ''
    for tweet_word in tweet:
        if tweet_word[1] == 'JJ' or tweet_word[1] == 'JJR' or tweet_word[1] == 'JJS':
            lem_tweet_word = wnl.lemmatize(tweet_word[0],ADJ)
            if dic_adj.has_key(lem_tweet_word) :
                dic_adj[lem_tweet_word]+=1
            else:
                dic_adj[lem_tweet_word]=1
        elif tweet_word[1]== 'RB' or tweet_word[1]== 'RBR' or tweet_word[1]== 'RBS' or tweet_word[1]== 'WRB':
            lem_tweet_word = wnl.lemmatize(tweet_word[0],ADV)
            if dic_adv.has_key(lem_tweet_word):
                dic_adv[lem_tweet_word]+=1
            else:
                dic_adv[lem_tweet_word]=1
        elif tweet_word[1]== 'VB' or tweet_word[1]== 'VBD' or tweet_word[1]== 'VBG' or tweet_word[1]== 'VBN' or tweet_word[1]== 'VBP' or tweet_word[1]== 'VBZ':
            lem_tweet_word = wnl.lemmatize(tweet_word[0],VERB)
            if dic_verb.has_key(lem_tweet_word):
                dic_verb[lem_tweet_word]+=1
            else:
                dic_verb[lem_tweet_word]=1
        elif tweet_word[1]== 'NN' or tweet_word[1]== 'NNS' or tweet_word[1]== 'NNP' or tweet_word[1]== 'NNPS':
            lem_tweet_word = wnl.lemmatize(tweet_word[0],NOUN)
            if dic_noun.has_key(lem_tweet_word):
                dic_noun[lem_tweet_word]+=1
            else:
                dic_noun[lem_tweet_word]=1
        else:
            lem_tweet_word = '' #tweet_word[0]
        if DEBUG :
            if lem_tweet_word != tweet_word[0]:
                print tweet_word[0], lem_tweet_word , '\n'
        if not DEBUG :
            lem_tweet = lem_tweet + ' ' + lem_tweet_word 
    if not DEBUG :
        writer.writerow(
                            [
                                row_arr[0], # username
                                row_arr[1], # old tweet_text
                                lem_tweet, # tokenized and lemmitized tweet
                                row_arr[3],
                                row_arr[4],
                                row_arr[5],
                                ])
#for item in sorted(dic_noun):
#    print(item, ' ', dic_noun[item])
list_noun=[]
list_adj=[]
list_verb=[]
list_adv=[]

if not DEBUG : 
    out_noun = open('./dictionary/noun.csv','w') 
    writer2 = csv.writer(out_noun, delimiter = '\t') 

    import operator
    #print(sorted(dic_adj.iteritems(), key=operator.itemgetter(1), reverse=True))
    sort_noun = sorted(dic_noun.iteritems(), key=operator.itemgetter(1), reverse=True)
    for item in sort_noun:
        if item[1]>=thresh_noun:
            writer2.writerow(
                [
                    item[0].encode('ascii','replace'),
                    item[1]

                ]

                )
            #list_noun.append(item)
        else:
            break

    out_verb = open('./dictionary/verb.csv','w') 
    writer2 = csv.writer(out_verb, delimiter = '\t') 
    sort_verb = sorted(dic_verb.iteritems(), key=operator.itemgetter(1), reverse=True)
    for item in sort_verb:
        if item[1]>=thresh_verb:
            writer2.writerow(
                [
                    item[0].encode('ascii','replace'),
                    item[1]

                ]

                )
            #list_verb.append(item)
        else:
            break

    out_adj = open('./dictionary/adj.csv','w') 
    writer2 = csv.writer(out_adj, delimiter = '\t') 
    sort_adj = sorted(dic_adj.iteritems(), key=operator.itemgetter(1), reverse=True)
    for item in sort_adj:
        if item[1]>=thresh_adj:
            writer2.writerow(
                [
                    item[0].encode('ascii','replace'),
                    item[1]

                ]

                )
            #list_adj.append(item)
        else:
            break

    out_adv = open('./dictionary/adv.csv','w') 
    writer2 = csv.writer(out_adv, delimiter = '\t') 
    sort_adv = sorted(dic_adv.iteritems(), key=operator.itemgetter(1), reverse=True)
    for item in sort_adv:
        if item[1]>=thresh_adv:
            writer2.writerow(
                [
                    item[0].encode('ascii','replace'),
                    item[1]

                ]

                )
            #list_adv.append(item)
        else:
            break