import PIL.Image as Image
import numpy as np

img = Image.open('img/Lena_L.jpg')
sharpen_model = Image.open('img/Lena_L_laplace_filter_1.jpg')

img_arr = np.array(img)
sharpen_model_arr = np.array(sharpen_model)

img_width, img_height = img.size

for y in range(img_height):
    for x in range(img_width):
        img_arr[y, x] = int(img_arr[y, x]) - int(sharpen_model_arr[y, x])

out = Image.fromarray(img_arr)
out.save('img/Lena_L_sharpen.jpg')
