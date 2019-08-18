import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
import sys

file = "img/1_5.jpg"

img = Image.open(file)
img = img.convert('L')

width = img.size[0]
height = img.size[1]

# 获取原图的直方图
freq = 256*[0]
for index in range(width * height):
    x = index % width
    y = index // width
    freq[ img.getpixel((x, y)) ] += 1

# 直方图均衡化
freq2 = 256*[0]
for i in range(len(freq2)):
    freq2[i] = round(255 / (width * height) * sum(freq[0:i+1]))

# 输出灰度均衡化之后的图
out = Image.new(img.mode, (width, height))
for i in range(width * height):
    x = i % width
    y = i // width
    out.putpixel((x, y), freq2[img.getpixel((x, y))])

plt.subplot(121)
plt.title('Original')
plt.bar(np.arange(0, 256), freq)

plt.subplot(122)
plt.title('After equalization')
plt.bar(np.arange(0, 256), out.histogram())

plt.show()

# out.save(file[0:-4]+'_histogram_equalizartion'+file[-4:])
