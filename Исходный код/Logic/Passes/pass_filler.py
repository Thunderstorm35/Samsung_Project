from Logic.Passes.pass_base import PassBase


class FillerPass(PassBase):
    def __init__(self, name):
        super().__init__(name)

    def apply(self, image):
        return image
