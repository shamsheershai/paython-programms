# importing the module
import tweepy
 
# personal details
consumer_key ='pYQXIBu53yjTane6DbAWObyEL'
consumer_secret ='Y9ILNgzg9iEGFnZD6y89hj619eWrqeSp4BrJR7svpz3xsjn31k'
access_token ='2736882968-6oCW7hBOB5nSZ8nUZqE12Kk1WWjxb0USOn1Hgnb'
access_token_secret ='q6C49o3U6kYot1Zjl3Ha3imzXdGjUiSHepaXLegikcWAw'

 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
