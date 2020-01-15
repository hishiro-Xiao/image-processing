import IP_util
import numpy as np
import math

blur_radius = 3
sigma = 1.5

filter_size = blur_radius * 2 + 1
gaussian_filter = [[0 for _ in range(filter_size)] for _ in range(filter_size)]

# print(gaussian_filter)

for i in range(filter_size):
    for j in range(filter_size):
        rr = (blur_radius - i) ** 2 + (blur_radius - j) ** 2
        gaussian_filter[i][j] = 1 / (2 * math.pi * sigma ** 2) * math.exp((-rr) / (2 * sigma ** 2))

# print(gaussian_filter)

gaussian_filter = np.array(gaussian_filter)
arr_sum = sum(sum(gaussian_filter))
gaussian_filter = gaussian_filter / arr_sum

IP_util.Tools.processByFilter('img/Lena_L.jpg', gaussian_filter)
