#!/usr/bin/python3
"""Function to query posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints titles to the console or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 "}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print(None)
