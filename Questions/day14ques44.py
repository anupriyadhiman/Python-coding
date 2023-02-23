#Draw step function using matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 7, 9, 17])
y = np.array([1, 7, 17, 25, 48])
  
plt.step(x, y)
plt.show()