import PIL.Image as Image
import numpy as np
import sys
import time

start = time.time()
file = 'img/Lena.jpg'

img = Image.open(file)
img_width = img.size[0]
img_height = img.size[1]
img_size = img_width * img_height

# 均值滤波器
filter_size = 5
# 最后一个3是因为图片数组是三维数组，最后一个3表示rgb的三个值，如果处理png图片，则改为4
filter = np.ones((filter_size, filter_size, 3)) / filter_size ** 2
# 转换成“一维”数组
filter = filter.reshape((filter_size ** 2, 1, 3))

# 对原图像进行0扩充，由于原图像边缘像素无法获取像素，对这些“缺失”的部分进行人为扩充
# 扩充结束后将包含rgb值得三维数组转换成int值的二维数组，以便矩阵操作
img_expand_width = img_width + filter_size // 2 * 2
img_expand_height = img_height + filter_size // 2 * 2
img_expand = Image.new(img.mode, (img_expand_width, img_expand_height))
for x in range(img_expand_width):
    for y in range(img_expand_height):
        img_expand.putpixel((x, y), (0, 0, 0))
for x in range(img_width):
    for y in range(img_height):
        img_expand.putpixel((x + filter_size // 2, y + filter_size // 2), img.getpixel((x, y)))
img_expand_arr = np.array(img_expand)
# img_expand.save(file[:-4] + '_expand' + file[-4:])

out = Image.new(img.mode, (img_width, img_height))
for index in range(img_size):
    # 此处的xy为原图的坐标，要转换到img_expand中的数组坐标
    out_x = index % img_width
    out_y = index // img_width
    expand_y = out_x + filter_size // 2
    expand_x = out_y + filter_size // 2

    pixels = img_expand_arr[expand_x - filter_size // 2 : expand_x + filter_size // 2 + 1,
                            expand_y - filter_size // 2 : expand_y + filter_size // 2 + 1].reshape((filter_size ** 2, 1, 3))
    pixel_new = sum(filter * pixels)
    pixel_tuple = (
        int(pixel_new[0, 0]),
        int(pixel_new[0, 1]),
        int(pixel_new[0, 2])
    )
    out.putpixel((out_x, out_y), pixel_tuple)

out.save(file[0:-4] + '_SSF' + file[-4:])

end = time.time()
print(str(round(end - start, 2)) + 's')
