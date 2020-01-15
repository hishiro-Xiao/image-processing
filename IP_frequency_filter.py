import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import PIL.Image as Image

img = Image.open('img/Lena.jpg')
img = img.convert('L')
img_arr = np.array(img)
rows, cols = img_arr.shape

img_expand_arr = np.zeros((rows * 2, cols * 2))
for i in range(rows):
    for j in range(cols):
        img_expand_arr[i][j] = img_arr[i][j]

img_fu = np.fft.fft2(img_expand_arr)
img_fu = np.fft.fftshift(img_fu)

plt.subplot(121)
plt.imshow(img_arr, 'gray')
plt.title('Original')

plt.subplot(122)
plt.imshow(np.log(np.abs(img_fu)), 'gray')
plt.title('Fourier')
plt.show()

# 傅里叶反变换
img_convert_mat = np.fft.ifft2(np.fft.ifftshift(img_fu))
img_convert_mat = np.abs(img_convert_mat)
img_convert_mat = img_convert_mat[0:rows, 0:cols]

img_converted = Image.fromarray(img_convert_mat)
img_converted.show()
