#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
  """Returns the number of subscribers for a given subreddit."""
  url = f"https://www.reddit.com/r/{subreddit}/about.jsom"
  headers = {'User-Agent': 'my-app/0.0.1'}

  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    try:
      data = response.json()
      return data['data']['subscribers']
    except (ValueError, KeyError):
      return 0
  else: return 0
