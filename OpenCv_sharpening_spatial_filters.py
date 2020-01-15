import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) == 1:
    file = 'img/Lena.jpg'
else:
    file = sys.argv[1]

img = cv2.imread(file)

filter = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

out = cv2.Laplacian(img, 3)
out2 = img - out

cv2.imwrite(file[:-4] + '_Laplacian' + file[-4:], out2)
