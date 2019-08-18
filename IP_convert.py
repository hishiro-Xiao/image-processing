import PIL.Image
import PIL.ImageOps

img = PIL.Image.open('img/test.png')

# my code
# img_resized = PIL.Image.new(img.mode, (img.size[0], img.size[1]) )
# for r in range(img_resized.size[1]):
#     for c in range(img_resized.size[0]):
#         pixel = img.getpixel((c, r))
#         red = 255 - pixel[0]
#         green = 255 - pixel[1]
#         blue = 255 - pixel[2]
#         img_resized.putpixel( (c, r), (red, green, blue, pixel[3]))
# img_resized.save('img/test_convert.png')

# code exapmle 1
# img = PIL.Image.eval(img, lambda x: 255 - x)

# code example 2
# out = img.point(lambda x: 255-x)
# out.show()
# out.save('img/test_convert_2.png')

# code exaple 3
# OSError: not supported for this image mode ？？？
# img = PIL.ImageOps.invert(img)
# img.show()
