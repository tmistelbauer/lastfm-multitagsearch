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

# Add results of each individual search in a list and append it to tag_result
for tag in tags:
    url += "&tag=" + tag
    response = requests.get(url)
    artists = response.json()["topartists"]["artist"]
    subresult = []
    for artist in artists:
        subresult.append(artist["name"])
    tag_result.append(subresult)

result = []

# Go through all lists and intersect them
for i in range(len((tag_result))):
    # If result is still empty, fill it with the first tag list:
    if i == 0:
        result = tag_result[i]
    elif i < len(tag_result):
        result = list(set(result) & set(tag_result[i]))

print(str(len(result)) + " artists found!")
print(result)
