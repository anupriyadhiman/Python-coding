# Calculate the weight of the word banana.(weight = sum of ascii values of all characters)


word = "banana"
counter = 0
for char in word:
    counter += ord(char)
print(f"Weight of the word {word} is {counter}")