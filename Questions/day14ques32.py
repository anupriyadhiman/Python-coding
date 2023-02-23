#given numbers ( in string format ) in a file, read them and create a numpy array

import numpy as np
with open('string_num.txt') as f:
    numbers = f.read().splitlines()
    numbers = [int(number) for number in numbers]
    print(numbers)
    numbers = np.array(numbers)
    print(numbers)

