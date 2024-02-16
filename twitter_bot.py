
import tweepy

def main():

    api_key = ""
    api_secret = ""
    bearer_token = r""
    access_token = ""
    access_token_secret = ""

    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

    try:
        client.create_tweet(text="Hello World!")
        print("Tweet posted successfully")
    except:
        print("Tweet posting failed")

main()
