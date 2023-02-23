# Given the name strings in a file, read all the names, convert them to corresponding ascii characters and calculate the sum


with open('D:\AI&DS\Python\Classes\Practice_ques\Questions\name.txt') as f:
        names = f.read().splitlines()
        print(names)
        names = [ord(name) for name in names]
        names = [sum(name) for name in names ]
        print(names)