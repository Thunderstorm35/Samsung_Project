import cv2 as cv
from Logic.Passes.pass_base import PassWithParams, ParamType

MAX_WIDTH = 2000
MAX_HEIGHT = 2000


class ResizerPass(PassWithParams):
  def __init__(self, name):
    super().__init__(name)

  def defineParams(self):
    self.params.addParam("width", 64, 0, MAX_WIDTH, ParamType.NUMBER)
    self.params.addParam("height", 64, 0, MAX_HEIGHT, ParamType.NUMBER)

  def apply(self, image):
    return cv.resize(
      image,
      (
        self.params.getValueByName("width"),
        self.params.getValueByName("height")
      ),
      interpolation=cv.INTER_AREA
    )
