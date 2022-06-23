from Logic.Passes.pass_base import PassWithParams, ParamType

MAX_WIDTH = 2000
MAX_HEIGHT = 2000


class AreaCutterPass(PassWithParams):
    def __init__(self, name):
        super().__init__(name)

    def defineParams(self):
        self.params.addParam("x right", 400, 0, MAX_WIDTH, ParamType.NUMBER)
        self.params.addParam("width", 1000, 0, MAX_WIDTH, ParamType.NUMBER)

        self.params.addParam("y top", 150, 0, MAX_HEIGHT, ParamType.NUMBER)
        self.params.addParam("height", 250, 0, MAX_HEIGHT, ParamType.NUMBER)

    def apply(self, image):
        x_right = self.params.getValueByName("x right")
        x_left = x_right + self.params.getValueByName("width")

        y_top = self.params.getValueByName("y top")
        y_bottom = y_top + self.params.getValueByName("height")

        return image[y_top:y_bottom, x_right:x_left]
        # return cv.rectangle(image, (x_left, y_top), (x_right, y_bottom), (255, 0, 255), 3)