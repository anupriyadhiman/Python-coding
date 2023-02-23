# Given a user_input as a string, calculate its md5 hash


import hashlib
input1 = input("enter a string:")
result = hashlib.md5(input1.encode())
print(result.hexdigest())
