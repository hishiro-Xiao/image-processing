import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt

# convert 32bit color picture to 2-value picture (black-and-white)
# but still 32bit picture
img = Image.open('img/test.png')
width = img.size[0]
height = img.size[1]

out = Image.new(img.mode, (width, height))
for index in range(width * height):
    x = index % width
    y = index // width
    pixel = img.getpixel((x, y))
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    alpha = pixel[3]
    if (red + green + blue) / 3 <= 128:
        out.putpixel((x, y), (0, 0, 0, alpha))
    elif 128 < (red + green + blue) / 3 <= 255:
        out.putpixel((x, y), (255, 255, 255, alpha))

plt.figure('gaoxiong')
plt.imshow(out)
plt.show()

# out.save('img/IP_Piecewise_convert.png')
