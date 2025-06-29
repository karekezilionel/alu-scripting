#!/usr/bin/python3
"""This module prints the titles of the first 10 hot posts
from a given subreddit using Reddit's public API.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:hot.posts:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            for post in data:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    except Exception:
        print("None")
