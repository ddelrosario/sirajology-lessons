import tweepy
from textblob import TextBlob

consumer_key = '0ltxKpoUBFnQOHXOOb0T8POdZ'
consumer_secret = 'dhCWexj7czj8doucccH61mrpyLb0P01M9uuWGLzfrtgTUPUaFP'

access_token = '96398704-bE2H2xX7srSxnNyYYUTuKZX3ve1p50CWTrrI4j7ss'
access_token_secret = 'rB5VAxORC9kSkTFDHRWfzL37H8CGtlMOFkQOWcbuBEoj9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('HamiltonCHI')

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
