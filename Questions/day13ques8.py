#Take user input and write it to a file.

with open("user.txt", "w") as user:
    user.write(input("Enter something: "))
    

    