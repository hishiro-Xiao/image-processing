import PIL.Image

# formulation: s = c * r ^ gama, c=1, gama=0
# within which, scaling r to 0~1 first, then scaling to 0~255 in the end
img = PIL.Image.open('img/test.png')
gama = 2.2


def gama_convert(val):
    return round(pow(val/255, gama) * 255)


# my code 1
out = PIL.Image.new(img.mode, (img.size[0], img.size[1]))
for height in range(img.size[1]):
    for length in range(img.size[0]):
        pixel = img.getpixel((length, height))
        out.putpixel((length, height), (gama_convert(pixel[0]),
                                        gama_convert(pixel[1]),
                                        gama_convert(pixel[2]),
                                        pixel[3]))
# out.show()
out.save('img/test_gama_convert.png')

# my code 1 optimized
# out = PIL.Image.new(img.mode, (img.size[0], img.size[1]))
# for index in range(img.size[0] * img.size[1]):
#     x = index % img.size[0]
#     y = index // img.size[0]
#     pixel = img.getpixel((x, y))
#     out.putpixel((x, y), (gama_convert(pixel[0]),
#                           gama_convert(pixel[1]),
#                           gama_convert(pixel[2]),
#                           pixel[3]))
#
# out.save('img/test_gama_convert.png')

# my code 2
# out = img.point(lambda x: pow(x, gama))
# out.save('img/test_gama_convert_2.png')
