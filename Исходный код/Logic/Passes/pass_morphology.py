import cv2 as cv
import numpy as np
from Logic.Passes.pass_base import PassBase

KERNEL_SIZE = 4
kernel = np.ones((KERNEL_SIZE, KERNEL_SIZE), np.uint8)


class MorphologyPass(PassBase):
    def __init__(self, name):
        super().__init__(name)

    def apply(self, image):
        global kernel
        return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
