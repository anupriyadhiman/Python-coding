#Fetch the data from a url and save it to a file.

import requests as req

url = "https://medium.com/@anupriyadhiman0605/classes-and-objects-an-inspiration-from-real-life-in-python-7deeaa01eaaf"
response = req.get(url)
with open("url.txt", "w", encoding = 'utf-8') as url:
    url.write(response.text)
    