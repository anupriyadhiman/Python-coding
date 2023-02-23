# 42 - Draw sin wave using matplotlib.
import matplotlib.pyplot as plt
import numpy as np
X = np.arange(0,5*np.pi,0.2) 

Y1 = np.sin(X)
Y2 = np.cos(X)
  

figure, axis = plt.subplots(2)
  
# For Sine Function
axis[0].plot(X, Y1)
axis[0].set_title("Sine Function")
  
# For Cosine Function
axis[1].plot(X, Y2)
axis[1].set_title("Cosine Function")

plt.show()