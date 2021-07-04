import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from vysptor.histogram import EdgeHistogramDescriptor
from vysptor.utils import to_grayscale


image = Image.open('img.jpg')
image = np.array(image)
images = np.array([image, image])

images = to_grayscale(images)
plt.imshow(images[0], cmap='gray')

ehd = EdgeHistogramDescriptor()

for img in images:
    print('---')
    print(img)