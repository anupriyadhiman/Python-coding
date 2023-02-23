# Fetch the data from a url and calculate the number of strings in it. 
import requests as req

resp = req.get("https://medium.com/@anupriyadhiman0605/classes-and-objects-an-inspiration-from-real-life-in-python-7deeaa01eaaf")
with open("text.txt", "w", encoding="utf-8") as file:
        file.write(resp.text)

with open("text.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)