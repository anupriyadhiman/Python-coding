# Given numbers ( in string format ) in a file, read them and create a pandas data frame object 

import pandas as pd
df = pd.read_csv('D:\AI&DS\Python\Classes\Practice_ques\Questions\string_num.txt', delimiter = "/n")
print(df)