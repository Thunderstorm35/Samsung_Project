class Postprocessor:
    def __init__(self, passesSequence, image=None):
        self.image = image
        self.passesSequence = passesSequence

    def setImage(self, image):
        self.image = image
        return self

    def getImage(self):
        return self.image

    def process(self):
        for __pass__ in self.passesSequence:
            self.setImage(__pass__.apply(self.image))
        return self
