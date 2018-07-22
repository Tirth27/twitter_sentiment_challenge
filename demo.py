import tweepy
from textblob import TextBlob
import csv


# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

#for tweet in public_tweets:
#    print(tweet.text)
#        
#    #Step 4 Perform Sentiment Analysis on Tweets
#    analysis = TextBlob(tweet.text)
#    print(analysis.sentiment, '\n')   
#print("")

#get public tweet in list
sentance_to_analyse = [[tweet.text]for tweet in public_tweets]

#Make row of tweets
with open('sentiment.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    file.writerow(['Tweet', 'Polarity'])
    file.writerows(sentance_to_analyse)

#perform sentiment analysis on tweets    
with open('sentiment.csv', 'r') as f:
    rows = csv.reader(f)
    sentiment_of_tweet = [["Positive"] if TextBlob(r[0]).sentiment.polarity >= 0 else ["Negative"] for r in rows]

'''
 csv doesnt support write column because variable-length lines are not really 
 supported on most filesystems. What you should do instead is collect all the 
 data in lists, then call zip() on them to transpose them after. 
'''
#collect data in list-[], tupple-()
data = [(sentance_to_analyse),(sentiment_of_tweet)]
zipp = zip(*data)
#print(zipp)

#write tweet and its sentiment     
with open('sentiment.csv', 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    
    file.writerow(['Tweet', 'Polarity'])
    file.writerows(zipp)
