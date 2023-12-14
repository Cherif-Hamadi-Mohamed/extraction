import tweepy
import pandas as pd

consumer_key = "wBkSAA" #API/Consumer key 
consumer_secret = "AAAAAAAAAAAAAAAAAAAAAPHdrQEAAAAAdcXFlxhkZHv6YrYSg5Ruo0CjfM8%3DvGCRpOpLT9Cfe120gThFrzTjb5a13GyXTft9pWqGA1pku2wYFt" #API/Consumer Secret Key
access_token = "1735004508453736448-P3Iqr5iuPsZTvGahYzRO5dI0ggU1Oi"    #Your Access token key
access_token_secret = "yuTWLVzos69EQV41Tk98wPi2L011cdEUNyWoqNweXqsHw" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "'ref''world cup'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
     