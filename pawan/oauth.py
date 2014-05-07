import twitter

def oauth_login():
	CONSUMER_KEY = 'HNe0HtDBn4jYkjIyr4XuA'
	CONSUMER_SECRET ='b8jPvulf7lPM5qLuP1MFmlPuefbbrPfq8GuU6WqBoI'
	OAUTH_TOKEN ='269117144-lXD9Uk5iVx5n4F9FP2wG7bn75Eu5q39Ipq79Oxmp'
	OAUTH_TOKEN_SECRET ='SzEF8AqlclZYcmnztD3BP4HMvmiMbzPosKO9KRM0dabli'
	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api =twitter.Twitter(auth=auth)
	return twitter_api