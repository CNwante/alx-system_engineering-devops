#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.jsom"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /CNwante)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (ValueError, KeyError):
            return 0
    else:
        return 0
