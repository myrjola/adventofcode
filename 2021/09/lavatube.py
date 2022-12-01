import numpy as np
import scipy.ndimage as ndimage

lavamap = np.array([list(map(int, list(line.strip()))) for line in open("test-input.txt", 'r').readlines()])

def local_minimum(array):
    print(array)
    return array[5]

n = 5
array = np.arange(n ** 2).reshape((n, n))

ndimage.generic_filter(array, local_minimum, size=3, mode='constant', cval=10)

padded_lavamap = np.pad(lavamap, pad_width=1, mode='constant', constant_values=10)

for y in range(1, padded_lavamap.shape[0]-1):
    for x in range(1, padded_lavamap.shape[1]-1):
        local_minimum = padded_lavamap[y,x]
        print(x, ", ", y)

