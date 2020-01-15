from typing import List
from IP_add_noise import AddNoise
import IP_filter_8bit as ff

import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt

class Tools:
    @staticmethod
    def getFrequence(filenme) -> List:

        img = Image.open(filenme).convert('L')
        width, height = img.size[0], img.size[1]

        freq = 256 * [0]
        for index in range(width * height):
            x = index % width
            y = index // width
            freq[img.getpixel((x, y))] += 1

        return freq

    @staticmethod
    def getHistogram(filename):
        freq = Tools.getFrequence(filename)

        plt.title('Frequence')
        plt.bar(np.arange(0, 256), freq)
        plt.show()

    @staticmethod
    def addNoise(filename, noise_config):
        AddNoise.add_noise(filename, noise_config)

    @staticmethod
    def processByFilter(filename, filter):
        '''
            根据滤波器矩阵处理图片
        '''
        ff.Filter8bit.filter8bit(filename, filter)
