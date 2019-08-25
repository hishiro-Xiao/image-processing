import PIL.Image as Image
import numpy as np
import sys
import time

start = time.time()

file = 'img/bqb.png'

img = Image.open(file)
img_arr = np.array(img)

width = img.size[0]
height = img.size[1]
size = width * height

out_width = width * 2
out_height = height * 2
out_size = out_width * out_height

out = Image.new(img.mode, (out_width, out_height))
for index in range(out_size):
    out_x = index % out_width
    out_y = index // out_width
    pixel = np.zeros(3)

    # 此处的img_x值为float值，还未四舍五入处理
    img_x = width / out_width * (out_x + 1) - 1
    img_y = height / out_height * (out_y + 1) - 1

    # 此处的img_x_int和img_y_int为int，用来表示距离(x,y)最近的四个点
    img_x_int = int(img_x)
    img_y_int = int(img_y)

    # 分别处理像素点落在左上角的点，左边界和上边界上的情况，
    # 不考虑其余点和其余边，是因为其余点和其余边，可以看作是其他像素的情况
    # 注意：由于numpy获取到的图片数组都是高度X宽度，所以下面img_arr的操作都是[y,x]的形式
    if img_x == img_x_int and img_y == img_y_int:
        pixel += img_arr[img_y_int, img_x_int]
    elif img_x == img_x_int:
        pixel += (img_y_int + 1 - img_y) * img_arr[img_y_int, img_x_int] + \
                 (img_y - img_y_int) * img_arr[img_y_int+1, img_x_int]
    elif img_y == img_y_int:
        pixel += (img_x_int + 1 - img_x) * img_arr[img_y_int, img_x_int] + \
                 (img_x - img_x_int) * img_arr[img_y_int, img_x_int+1]
    else:
        p11 = [img_x_int, img_y_int]
        p12 = [img_x_int+1, img_y_int]
        p21 = [img_x_int, img_y_int+1]
        p22 = [img_x_int+1, img_y_int+1]

        s11 = (img_x - img_x_int) * (img_y - img_y_int)
        s12 = (img_x_int+1 - img_x) * (img_y - img_y_int)
        s21 = (img_x - img_x_int) * (img_y_int+1 - img_y)
        s22 = (img_x_int+1 - img_x) * (img_y_int+1 - img_y)

        pixel += img_arr[p11[1], p11[0]] * s22 + \
                 img_arr[p12[1], p12[0]] * s21 + \
                 img_arr[p21[1], p21[0]] * s12 + \
                 img_arr[p22[1], p22[0]] * s11

    pixel = pixel.astype(int)
    out.putpixel((out_x, out_y), tuple(pixel))
out.save(file[0:-4] + '_BI' + file[-4:])

end = time.time()
print('Time : ' + str(round(end - start, 2)) + 's')
