import tweepy

consumer_key = '*******************************'
consumer_secret = '*******************************'
access_token = '*******************************'
access_token_secret = '*******************************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

queries = ["#FreeMapMonday"]
tweets_per_query  = 10000

for tweet in tweepy.Cursor(api.search, q=queries, tweet_mode="extended").items(tweets_per_query):
    if tweet.user.screen_name == 'USGSstore':
        tweet.retweet()
    else:
        pass