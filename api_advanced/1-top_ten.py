#!/usr/bin/python3
""" Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json().get('data',{}).get('children', [])
        for post in data:
            print(post.get('data',{}).get('title'))
        
    else:
        print(None)
