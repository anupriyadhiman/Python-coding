# Encode a string by adding 10 to all the ascii characters of that string and decode it back 

def str_encode(string):
    en_str = ""
    for char in string:
        en_str += chr(ord(char) + 10)
    return en_str

def str_decode(string):
    de_str = ""
    for char in string:
        de_str += chr(ord(char) - 10)
    return de_str

if __name__ == "__main__":
    string = input("Enter a string: ")
    en_str = str_encode(string)
    print("Encoded string: ", en_str)
    de_str = str_decode(en_str)
    print("Decoded string: ", de_str)