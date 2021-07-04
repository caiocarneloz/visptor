import numpy as np

def to_grayscale(img):

    return np.dot(img[...,:3], [1/3,1/3,1/3])
