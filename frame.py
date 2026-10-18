import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.transform import resize

def box(arr, w, h, x, y):
    for a in range(x, x+w):
        for b in range(y, y+h):
            arr[b, a] = 255

def graphic_or(arr1, arr2):
    res = np.zeros(shape=arr1.shape, dtype=np.uint8)
    count_alt = 0
    for i, (y1, y2) in enumerate(zip(arr1, arr2)):
        for j, (x1, x2) in enumerate(zip(y1, y2)):
            if int(x1)==0:
                res[i, j] = x2
                count_alt+=1
            else:
                res[i, j] = x1
    print(np.sum(res))
    print(count_alt)
    return res


arr1 = np.zeros(shape=(100, 100), dtype=np.uint8)
arr2 = np.zeros(shape=(150, 150), dtype=np.uint8)

box(arr1, 20, 50, 5, 0)
#box(arr1, 30, 50, 40, 0)
box(arr1, 20, 50, 75, 0)

box(arr2, 20, 50, 40, 0)
print(np.sum(arr1))

plt.imshow(arr2, cmap='gray')
plt.show()
arr2 = cv2.resize(arr2, (100, 100))
print(np.sum(arr2))
# plt.imshow(arr2, cmap='gray')
# plt.show()
# plt.imshow(arr2, cmap='gray', vmin=0, vmax=1)
# plt.show()
arr2*=np.uint8(0.5)

print(np.array([1, 1, 0, 0, 1, 1])*0.5)

plt.imshow(arr2, cmap='gray', vmin=0, vmax=1)
plt.show()

arr = graphic_or(arr1, arr2)

# plt.imshow(arr, cmap='gray', vmin=0, vmax=1)
# plt.show()