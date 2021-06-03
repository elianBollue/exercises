import urllib.request as request
import json
import sys
import re

artist = re.sub(' ', '%20', sys.argv[1])
title = re.sub(' ', '%20', sys.argv[2])

with request.urlopen(f"https://api.lyrics.ovh/v1/{artist}/{title}") as url:
    print(json.loads(url.read())['lyrics'])