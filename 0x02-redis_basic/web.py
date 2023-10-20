#!/usr/bin/env python3
"""
Caching request module
"""
import requests
from cachetools import Cache, TTLCache
from functools import wraps

# Create a cache with a 10-second expiration time
cache = TTLCache(maxsize=100, ttl=10)

def track_url_access(url):
    # Create a key for tracking URL accesses
    return f"count:{url}"

def get_page(url):
    # Check if the URL is already in the cache
    if url in cache:
        # Return the cached HTML content
        return cache[url]

    # If the URL is not in the cache, fetch the HTML content
    response = requests.get(url)

    # Track the URL access count
    access_key = track_url_access(url)
    access_count = cache.get(access_key, 0)
    cache[access_key] = access_count + 1

    # Cache the HTML content with the URL as the key
    cache[url] = response.text

    return response.text

# Decorator for caching and tracking URL accesses
def cache_and_track_url_access(func):
    @wraps(func)
    def wrapper(url):
        # Check if the URL is already in the cache
        if url in cache:
            # Return the cached HTML content
            return cache[url]

        # Call the original function to fetch the HTML content
        html_content = func(url)

        # Track the URL access count
        access_key = track_url_access(url)
        access_count = cache.get(access_key, 0)
        cache[access_key] = access_count + 1

        # Cache the HTML content with the URL as the key
        cache[url] = html_content

        return html_content
    return wrapper

# Usage of the get_page function with caching and tracking
if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/https://example.com"

    # Call the decorated function to get the page
    cached_get_page = cache_and_track_url_access(get_page)
    html_content = cached_get_page(url)

    # Print the HTML content and URL access count
    print(html_content)
    access_count = cache.get(track_url_access(url), 0)
    print(f"Access Count for {url}: {access_count}")

