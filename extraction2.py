import tweepy

# Replace these with your Twitter API credentials
consumer_key = 'wBkSAA'
consumer_secret = 'AAAAAAAAAAAAAAAAAAAAAPHdrQEAAAAAdcXFlxhkZHv6YrYSg5Ruo0CjfM8%3DvGCRpOpLT9Cfe120gThFrzTjb5a13GyXTft9pWqGA1pku2wYFt'
access_token = '1735004508453736448-P3Iqr5iuPsZTvGahYzRO5dI0ggU1Oi'
access_token_secret = 'yuTWLVzos69EQV41Tk98wPi2L011cdEUNyWoqNweXqsHw'

# Set up Tweepy with your credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Specify the username and the number of tweets you want to extract
username = 'Elon Musk'
num_tweets = 10

# Extract tweets
tweets = tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items(num_tweets)

# Print the extracted tweets
for tweet in tweets:
    print(tweet.full_text)
    print('-' * 50)