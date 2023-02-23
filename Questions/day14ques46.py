# Find all the urls in a data in a file 

import re

with open('D:\AI&DS\Python\Classes\Practice_ques\Questions\url.txt', 'r') as f:
    data = f.read()
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data)
    print(urls)