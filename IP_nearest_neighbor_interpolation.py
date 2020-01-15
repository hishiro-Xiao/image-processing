import PIL.Image as Image
import time

start = time.time()

file = 'img/IMG_1489.jpg'
img = Image.open(file)

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
    img_x = round( width / out_width * (out_x + 1) - 1)
    img_y = round( height / out_height * (out_y + 1) - 1)
    out.putpixel( (out_x, out_y), img.getpixel((img_x, img_y)))

out.save(file[0:-4]+'_NNI'+file[-4:])

end = time.time()
print('Time : ' + str(round(end - start, 2)) + 's')
