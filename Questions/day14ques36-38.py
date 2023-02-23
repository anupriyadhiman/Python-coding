# Convert the above numpy matrix to a pandas data frame 

import numpy as np
import pandas as pd


array = np.array([[2,3,4],[5,6,7]])

print(array)
print(type(array))

df = pd.DataFrame(array, columns = ['Column_A','Column_B','Column_C'])

print(df)
print(type(df))

# Save the above data frame as a csv file
df.to_csv('my_csv.csv')

# Save the above data frame as a excel file
df.to_excel('my_excel.xlsx')


