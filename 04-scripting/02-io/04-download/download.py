import urllib.request as request
import sys

with request.urlopen(sys.argv[1]) as url:
    print(url.read())