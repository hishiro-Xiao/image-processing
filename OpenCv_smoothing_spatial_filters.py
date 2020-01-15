import cv2
import numpy as np
import sys

def SSF(_file):
    file = _file
    img = cv2.imread(file)

    # 滤波器
    filter_size = 5
    filter = (filter_size, filter_size)

    out = cv2.blur(img, filter)

    cv2.imwrite(file[:-4] + '_SSF' + file[-4:], out)

    print('Process succeed.')

if __name__ == '__main__':
    SSF(sys.argv[1])
