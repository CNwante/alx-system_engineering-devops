#!/usr/bin/python3
"""Function to query posts recursively on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively fetches and returns a list of all hot article titles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): Accumulates the titles of hot articles across recursive calls.
        after (str): The pagination token to get the next set of posts.

    Returns:
        list: A list of titles of all hot articles from the subreddit, or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /CNwante)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    posts = response.json().get("data")
    after = posts.get("after")
    count += posts.get("dist")
    for post in posts.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
