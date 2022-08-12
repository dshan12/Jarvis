# Title :- URL Shortener
# The URL shortener is application which takes url input from user and shorts it
import pyshorteners


# url converter function
def make_short(url):
    shorturl = pyshorteners.Shortener().tinyurl.short(url)
    return shorturl