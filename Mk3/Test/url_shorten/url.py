import pyshorteners


def make_short(url_to_short):
    shorturl = pyshorteners.Shortener().tinyurl.short(url_to_short)
    return shorturl


a = input("What is your url:\n")
print(make_short(a))
