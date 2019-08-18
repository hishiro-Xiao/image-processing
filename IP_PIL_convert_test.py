import PIL.Image as Image
import matplotlib.pyplot as plt

img = Image.open('img/test.png')

img = img.convert('L')
plt.figure('gaoxiong')
plt.imshow(img)
plt.show()
# img.save('img/test_convert_L.jpg')
