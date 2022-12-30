import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl();

	access_key = "SmjG56GR3GzdQPSh1VrA3824z"
	access_secret = "oUsRf9AzaU9GP14UGjmxSeVvycSfm7iseJm3TTsdCZdSiNt2q4"
	consumer_key = "1164551684481118209-cpINVTv8O9LIZOtOMPldKzQDuGWvfJ"
	consumer_secret = "irfqFa4zjnzao1gF3yaKtbKpJ2EAb2M1rgnGGydR3T44z"

		# Twitter Authentication
	auth = tweepy.OAuthHandler(access_key, access_secret)
	auth.set_access_token(consumer_key, consumer_secret) 


		# Creating an API object 
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name='@elonmusk', 
		                    # 200 is the maximum allowed count
		                    count=200,
		                    include_rts = False,
		                    # Necessary to keep full_text 
		                    # otherwise only the first 140 words are extracted
		                    tweet_mode = 'extended'
		                    )
	

	list = []
	for tweet in tweets:
	    text = tweet._json["full_text"]

	    refined_tweet = {"user": tweet.user.screen_name,
		                'text' : text,
		                'favorite_count' : tweet.favorite_count,
		                'retweet_count' : tweet.retweet_count,
		                'created_at' : tweet.created_at}
		
	    list.append(refined_tweet)
		
		
		
	df = pd.DataFrame(list)
	df.to_csv('s3://airflow-bucket-luan/refined_tweets.csv')                                    
