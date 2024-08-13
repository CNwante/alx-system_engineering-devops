#!/usr/bin/python3
"""Function to query posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Prints the title of the top 10 hot posts in a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /CNwante)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print(None)
