import numpy as np
import sys
import PIL.Image as Image
import time

# 常用滤波器
SMOOTH_FILTER_3 = {
    'value' : np.ones((3, 3)) / 9,
    'name' : 'smooth_filter_3'
}
SMOOTH_FILTER_5 = {
    'name' : 'smooth_filter_5',
    'value' : np.ones((5, 5)) / 25
}
SMOOTH_FILTER_11 = {
    'name' : 'smooth_filter_11',
    'value' : np.ones((11, 11)) / 121
}
LAPLACE_FILTER_1 = {
    'name' : 'laplace_filter_1',
    'value' : np.array([
                [0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]
            ])
}
LAPLACE_FILTER_2 = {
    'name' : 'laplace_filter_2',
    'value' : np.array([
                [1, 1, 1],
                [1, -8, 1],
                [1, 1, 1]
            ])
}
LAPLACE_FILTER_3 = {
    'name' : 'laplace_filter_3',
    'value' : np.array([
                [0, -1, 0],
                [-1, 4, -1],
                [0, -1, 0]
            ])
}
LAPLACE_FILTER_4 = {
    'name' : 'laplace_filter_4',
    'value' : np.array([
                [-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]
            ])
}
SOBEL_FILTER_1 = {
    'name' : 'sobel_filter_1',
    'value' : np.array([
                [-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]
            ])
}
SOBEL_FILTER_2 = {
    'name' : 'sobel_filter_2',
    'value' : np.array([
                [-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]
            ])
}

# 计算程序运行时间
start_time = time.time()

# 获取图片路径
if len(sys.argv) == 1:
    file = 'img/Lena.jpg'
else:
    file = sys.argv[1]

# 滤波器
filter_type = LAPLACE_FILTER_1
filter_name = filter_type['name']
filter = filter_type['value']
filter_size = filter.shape[0]   # 滤波器大小，如3X3
filter_length = filter.size     # 滤波器长度，如9个元素
filter = filter.reshape((filter_size ** 2, 1))
filter_temp = np.zeros(filter_size ** 2 * 3).reshape((filter_size ** 2, 1, 3))
for i in range(filter_length):
    filter_temp[i, 0, 0] = filter[i, 0]
    filter_temp[i, 0, 1] = filter[i, 0]
    filter_temp[i, 0, 2] = filter[i, 0]
filter = filter_temp

# 待处理图片
img = Image.open(file)
img_width, img_height = img.size
img_size = img_width * img_height

# 对原图片进行0拓展
img_expand_width = img_width + filter_size // 2 * 2
img_expand_height = img_height + filter_size // 2 * 2
img_expand = Image.new(img.mode, (img_expand_width, img_expand_height))
for i in range(img_expand_height):
    for j in range(img_expand_width):
        img_expand.putpixel((j, i), (0, 0, 0))
for i in range(img_height):
    for j in range(img_width):
        img_expand.putpixel((j + filter_size // 2, i + filter_size // 2), img.getpixel((j, i)))
img_expand_arr = np.array(img_expand)
# img_expand.save(file[:-4] + '_expand' + file[-4:])

# 滤波操作
out = Image.new(img.mode, (img_width, img_height))
for index in range(img_size):
    out_x = index % img_width
    out_y = index // img_width
    expand_y = out_x + filter_size // 2
    expand_x = out_y + filter_size // 2

    pixels = img_expand_arr[
             expand_x - filter_size // 2: expand_x + filter_size // 2 + 1,
             expand_y - filter_size // 2: expand_y + filter_size // 2 + 1
    ].reshape((filter_size ** 2, 1, 3))
    pixel_new = sum(filter * pixels)

    # 标定操作
    for i in range(3):
        if pixel_new[0, i] >= 255:
            pixel_new[0, i] = 255
        if pixel_new[0, i] <= 0:
            pixel_new[0, i] = 0
    pixel_tuple = (
        int(pixel_new[0, 0]),
        int(pixel_new[0, 1]),
        int(pixel_new[0, 2]),
    )
    out.putpixel((out_x, out_y), pixel_tuple)

out.save(file[:-4] + '_' + filter_name + file[-4:])

end_time = time.time()
print(str(round(end_time - start_time, 2)) + 's')
