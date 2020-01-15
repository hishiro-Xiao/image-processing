import PIL.Image as Image
import random
import numpy as np

# 默认的噪声的配置信息
salt_and_pepper = {
    'number'  : 1000,
    'salt'    : 255,
    'pepper'  : 0,
}
guassian = {
    'name' : 'guassian',
    'number' : 1000,
}

file = 'img/Lena.jpg'

class AddNoise:
    def __init__(self, filename):
        self.filename = filename
        self.noise_config = salt_and_pepper

    @staticmethod
    def add_noise(filename, noise_config):
        img = Image.open(filename).convert('L')
        img_arr = np.array(img)
        width, height = img.size

        if noise_config['name'] == 'salt-and-pepper':
            random.seed()
            for i in range(noise_config['number']):
                x = random.randrange(width)
                y = random.randrange(height)
                img.putpixel((x, y), random.choice([noise_config['salt'], noise_config['pepper']]))

            img.save(filename[:-4] + '_' + noise_config['name'] + filename[-4:])

        if noise_config['name'] == 'gaussian':
            miu = sum(img_arr) / len(img_arr)
            sigma = sum(pow(img_arr - miu, 2))

            random.seed()
            for i in range(noise_config['number']):
                x = random.randrange(width)
                y = random.randrange(height)
                img.putpixel((x, y), )

        print('Image Processed Successfully.')
        print('Picture is stored at :' + filename[:-4] + '_' + noise_config['name'] + filename[-4:])
