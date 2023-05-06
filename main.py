import opensimplex
import numpy as np
import random
from PIL import Image

opensimplex.random_seed()
size = 16
image = Image.new("RGB", (size, size))
image = np.array(image)

# Palette

red = [242, 99, 137]
pinkish = [191, 73, 150]
purplish = [113, 73, 140]
offWhite = [242, 237, 213]
bluish = [111, 135, 165]

palette = [offWhite, bluish, red, pinkish, purplish]


def allRandom(palette):
    for r in range(0, size):
        for c in range(0, size):
            if opensimplex.noise2(r, c) * 10 <= -2:
                image[r][c] = palette[0]
            if 0 >= opensimplex.noise2(r, c) * 10 > -4:
                image[r][c] = palette[1]
            if opensimplex.noise2(r, c) * 10 > 0:
                image[r][c] = palette[2]
            if opensimplex.noise2(r, c) * 10 > 2:
                image[r][c] = palette[3]
            if opensimplex.noise2(r, c) * 10 > 3:
                image[r][c] = palette[4]

    img = Image.fromarray(image, 'RGB')
    img.show()


allRandom(palette)
