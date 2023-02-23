# Use a function from another file 


from day13ques18 import str_encode
from day13ques18 import str_decode

if __name__ == "__main__":
    string = input("Enter a string: ")
    en_str = str_encode(string)
    print("Encoded string: ", en_str)
    de_str = str_decode(en_str)
    print("Decoded string: ", de_str)

