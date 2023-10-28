import requests
from bs4 import BeautifulSoup

# URL of the Twitter profile you want to scrape
url = "https://twitter.com/PahujaKuvam"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract tweet elements
    tweets = soup.find_all("div", class_="tweet")

    for tweet in tweets:
        # Extract and print the tweet text
        tweet_text = tweet.find("p", class_="tweet-text")
        if tweet_text:
            print(tweet_text.text)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
