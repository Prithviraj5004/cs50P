import requests
import sys
import json


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
songs=response.json()
for result in songs["results"]:
    print(result["trackName"])