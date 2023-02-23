# print a picture using matplotlib.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('D:\AI&DS\Python\Classes\Practice_ques\Questions\ironmanicon.webp')
imgplot = plt.imshow(img)
plt.show()