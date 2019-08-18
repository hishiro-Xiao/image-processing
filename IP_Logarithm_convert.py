import PIL.Image
import math

# formulation : s = clog(1+r), c=10, base=e
img = PIL.Image.open('img/test.png')

# my code 1
# img_resized = PIL.Image.new(img.mode, (img.size[0], img.size[1]))
# for r in range(img.size[1]):
#     for c in range(img.size[0]):
#         pixel = img.getpixel((c, r))
#         red = round(10*math.log(pixel[0] + 1))
#         green = round(10*math.log(pixel[1] + 1))
#         blue = round(10*math.log(pixel[2] + 1))
#         img_resized.putpixel((c, r), (red, green, blue, pixel[3]))
# img_resized.show()
# img_resized.save('img/test_logarithm_convert.png')

# my code 2
# out = img.point(lambda x: 10*math.log(x+1))
# out.show()
# out.save('img/test_logarithm_convert_2.png')

# my code 3
# img = PIL.Image.eval(img, lambda x: round(10*math.log(x+1)))
# img.show()


