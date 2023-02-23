#Construct a 2x5 numpy matrix by taking all the numbers as input from user 

import numpy as np
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(Row, Column)
print(matrix)