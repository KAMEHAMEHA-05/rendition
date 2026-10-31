from matplotlib.pyplot import imshow, show, draw
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
obj = imshow(a)
for t in range(0,10):
    obj.set_data(a)
    draw()

    for i in range(0,a.shape[0]):
        for j in range(0,a.shape[1]):
            a[i][j] += 1
