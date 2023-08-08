import requests

# Set tags accordingly:
tags = ["speed metal", "stoner"]

# Use your own last.fm API key:
api_key = "<API-KEY>"

url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists"
url += "&api_key="+api_key
url += "&format=json"
url += "&limit=10000" # doesn't seem to have any effect

tag_result = []

for tag in tags:
    url_tag = url + "&tag=" + tag
    response = requests.get(url_tag)
    artists = response.json()["topartists"]["artist"]
    subresult = []
    for artist in artists:
        subresult.append(artist["name"])
    tag_result.append(subresult)

result = []

for i in range(len((tag_result))):
    if i == 0:
        result = tag_result[i]
    elif i < len(tag_result):
        result = list(set(result).intersection(set(tag_result[i])))

print(str(len(result)) + " artists found!")

for artist in result:
    print(artist)
