# Calculate how many times a string occurs in a given file.

with open("name.txt", "r", encoding="utf-8") as file:
        data = file.read()
str_occur = data.count("python")

print('Number of occurrences :', str_occur)