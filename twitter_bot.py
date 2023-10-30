# Import the Tweepy library. For installation instructions, please refer to the official documentation: https://docs.tweepy.org/en/stableinstall.html
import tweepy

# Insert your own Twitter API credentials and make sure to replace the placeholders with your actual keys and tokens.
api_key = "<your_api_key>"
api_secret = "<your_api_secret_key>"
bearer_token = r"<your_bearer_token>"
access_token = "<your_access_token_key>"
access_token_secret = "<your_access_secret_token_key>"

# Authentication
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# This is the tweet you want to post. You can modify the text to whatever you prefer. If you want to include a variable, use f-strings like this:
# i = 1
# client.create_tweet(text=f"Hello World! {i}")
client.create_tweet(text="Hello World!")