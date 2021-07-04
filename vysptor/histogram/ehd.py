import numpy as np
from scipy.signal import convolve2d

class EdgeHistogramDescriptor:

    def __init__(self):

        self.features = None
        self.filters = np.array([[[1,-1],[1,-1]],
                                [[1,1],[-1,-1]],
                                [[np.sqrt(2),0],[0,-np.sqrt(2)]],
                                [[0,np.sqrt(2)],[-np.sqrt(2),0]],
                                [[2,-2],[-2,2]]])

    def extract(self, images):

        if images.ndim != 3:
            raise Exception("""Expected 3-dimensional \
            np array: '(img_count, width, height)'""")

        for img in images:

            w, h = img.shape
            swsize, shsize = int(w/4), int(h/4)

            for y in np.arange(0,h,swsize):
                for x in np.arange(0,w,shsize):

                    sw, sh = img[x:x+swsize, y:y+shsize].shape
                    bwsize, bhsize = int(sw/4), int(sh/4)

                    for by in np.arange(y,y+sh,bwsize):
                        for bx in np.arange(x,x+sw,bhsize):

                            sub_block = img[bx:bx+bwsize, by:by+bhsize]

                            for f in filters:
                                convolve2d(sub_block, f, mode='same')