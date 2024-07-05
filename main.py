'''
Script that itializes a twikit client, 
Searches for tweets based on selected keywords,
Replies to the tweets with a selected text message

'''
import time
import random
from tqdm import tqdm
import os
from twikit import Client

def login_and_save_cookies(username, email, password, cookies_path):
    # Initialize client
    client = Client('en-US')

    # Login using credentials
    client.login(
        auth_info_1=username,
        auth_info_2=email,
        password=password
    )

    # Save cookies to a file
    client.save_cookies(cookies_path)
    print(f"Cookies saved to {cookies_path}")
    return client

def load_cookies_and_use_client(cookies_path):
    # Initialize client
    client = Client('en-US')

    # Load cookies from file
    client.load_cookies(cookies_path)
    print(f"Cookies loaded from {cookies_path}")
    return client

def initialize_client(username, email, password, cookies_path='cookies.json'):
    if os.path.exists(cookies_path):
        print("Trying to access cookies...")
        client = load_cookies_and_use_client(cookies_path)
    else:
        client = login_and_save_cookies(username, email, password, cookies_path)
    
    print(f"Logged in as: {username}")
    return client


def search_crypto_tweets(keyword, count=5):
    """
    Search for tweets containing the keyword related to crypto.
    """
    cursor = None

    result = client.search_tweet(query=keyword, product='Latest', count=count, cursor=cursor)

    return result


def main():
    # Define keywords to search for crypto groups/posts
    keywords = ['crypto', 'cryptocurrency', 'bitcoin', 'ethereum', 'blockchain']
    text = "Top !!!"
    # Search for tweets
    all_tweets = []
    for keyword in keywords:
        tweets = search_crypto_tweets(keyword)
        all_tweets.extend(tweets)

    # If no tweets found, exit
    if not all_tweets:
        print("No tweets found.")
        return
    for t in tqdm(all_tweets):
      print(f"Tweet text :", t.text)
      print("#"*50)
      try:
        t.reply(
            text,
            #media_ids=media_ids
        )
        print("Tweeted successfully!")
      except Exception as e:
        print("Error during tweeting")

      time.sleep(random.uniform(4.5, 10.1))

if __name__ == "__main__":
    # Example usage
    USERNAME = 'xxx'
    EMAIL = 'xxx@gmail.com'
    PASSWORD = 'xxx'
    cookies_path = 'cookies.json'

    # Initialize the client
    client = initialize_client(USERNAME, EMAIL, PASSWORD, cookies_path)
    main()



