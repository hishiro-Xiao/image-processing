import cv2
import numpy as np

file = 'img/test.png'

img = cv2.imread(file)

# 中值滤波器 大小必须为奇数
filter = 11

out = cv2.medianBlur(img, filter)

cv2.imwrite(file[:-4] + '_MSF' + file[-4:], out)
