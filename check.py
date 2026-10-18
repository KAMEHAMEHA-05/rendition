import numpy as np
import cv2

arr = np.array([[1, 0, 0],[1, 1, 0]], dtype=np.uint8)
arr = cv2.resize(arr, (3, 3))

print(arr)
print(np.array(arr))