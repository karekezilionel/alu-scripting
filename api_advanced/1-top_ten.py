#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts in a subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get('data', {}).get('title')
            print(title)

    except Exception:
        print(None)
