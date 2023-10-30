# README - Tweepy Tweet Posting Script

This Python script allows you to post a tweet on Twitter using the Tweepy library. Follow the steps below to set up the script and post a tweet.

## Prerequisites

Before using this script, make sure you have installed the Tweepy library by following the official instructions available [here](https://docs.tweepy.org/en/stable/install.html).

## Twitter API Key Configuration

1. Visit [https://developer.twitter.com/](https://developer.twitter.com/) and create a Twitter application to obtain your Twitter API keys.

2. Once you have obtained the Twitter API keys, replace the placeholders `<your_api_key>`, `<your_api_secret_key>`, `<your_bearer_token>`, `<your_access_token_key>`, and `<your_access_secret_token_key>` in the script with your actual keys. You can find them in your Twitter developer dashboard.

## Using the Script

1. Import the Tweepy library using the command `import tweepy` at the beginning of your script.

2. Replace the placeholders in the script with your actual Twitter API keys.

3. Use the `client.create_tweet(text="Your tweet text here")` function to create a tweet. Customize the tweet text by replacing `"Your tweet text here"` with the text you want to post.

   For example, to include a variable in the tweet, you can use f-strings like this:

   i = 1
   client.create_tweet(text=f"Hello World! {i}")

4. Execute the script with VsCode or with the following command line : python3 twitter_bot.py

## Uploading and Automating the Script on PythonAnywhere

If you want to run this script on PythonAnywhere, a cloud-based Python development environment, you can follow these steps:

1. Sign up for a PythonAnywhere account at [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/) if you haven't already.

2. After signing up, log in to your PythonAnywhere dashboard.

3. Click on the "Files" tab in your PythonAnywhere dashboard to access the file management system.

4. Upload your Python script to your PythonAnywhere account by clicking the "Upload a file" button. This will allow you to transfer your script to the cloud environment.

5. Then go to 'Tasks', select your script and the frequency and it's done !
