#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or an error occurs, returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers for the subreddit, or 0 if invalid.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests errors
    # Reddit recommends setting a unique and descriptive User-Agent
    headers = {
        "User-Agent": "python:subreddit_subscriber_counter:v1.0 (by /u/wintermancer)"
    }

    try:
        # Make a GET request to the Reddit API
        # allow_redirects=False ensures that we do not follow redirects,
        # which can happen for invalid subreddits (redirecting to search results).
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        # and if it's not a redirect (status code is not 3xx)
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers from the JSON response
            # The structure is data -> data -> subscribers
            return data['data']['subscribers']
        else:
            # If status code is not 200 (e.g., 404 Not Found, or 3xx Redirect),
            # it indicates an invalid subreddit or an error.
            return 0
    except requests.exceptions.RequestException:
        # Catch any request-related errors (e.g., network issues, connection refused)
        return 0
