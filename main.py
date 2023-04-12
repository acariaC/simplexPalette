import opensimplex
import numpy as np
import random
from PIL import Image

opensimplex.random_seed()
size = 16
image = Image.new("RGB", (size, size))
image = np.array(image)

# Palette
blue = [28, 12, 91]
purple = [61, 44, 141]
lavender = [145, 107, 191]
pinkish = [201, 150, 204]

palette = [blue, purple, lavender, pinkish]


def allRandom(palette):
    for r in range(0, size):
        for c in range(0, size):
            if opensimplex.noise2(r, c)*10 < 0:
                image[r][c] = palette[0]
            if opensimplex.noise2(r, c) * 10 > 0:
                image[r][c] = palette[1]
                if opensimplex.noise2(r, c) * 10 > 1:
                    image[r][c] = palette[2]
                    if opensimplex.noise2(r, c) * 10 > 2:
                        image[r][c] = palette[3]

    img = Image.fromarray(image, 'RGB')
    img.show()


allRandom(palette)
