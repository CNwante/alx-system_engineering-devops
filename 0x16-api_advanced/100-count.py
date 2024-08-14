#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit."""

    if instances is None:
        instances = {}

    # Normalize word_list to handle duplicates
    normalized_word_list = []
    for word in word_list:
        word_lower = word.lower()
        if word_lower not in normalized_word_list:
            normalized_word_list.append(word_lower)

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/CNwante)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(
        url, headers=headers,
        params=params,
        allow_redirects=False
    )

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return

    data = results.get("data")
    after = data.get("after")
    count += data.get("dist", 0)

    for c in data.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in normalized_word_list:
            times = sum(1 for t in title if t == word)
            if times > 0:
                instances[word] = instances.get(word, 0) + times

    if after is None:
        if len(instances) > 0:
            instances = sorted(instances.items(),
                               key=lambda kv: (-kv[1], kv[0]))
            for k, v in instances:
                print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
