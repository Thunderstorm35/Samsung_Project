import cv2 as cv
from Logic.Passes.pass_base import PassBase

subtractor = cv.bgsegm.createBackgroundSubtractorGSOC()


class BGSubtractorGSOCPass(PassBase):
    def __init__(self, name):
        super().__init__(name)

    def apply(self, image):
        image = subtractor.apply(image)
        return image
