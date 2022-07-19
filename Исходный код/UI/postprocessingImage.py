import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2 as cv
from Logic.postprocessing import Postprocessor
from Logic.Passes.pass_bg_subtractor_gsoc import BGSubtractorGSOCPass
from Logic.Passes.pass_morphology import MorphologyPass
from Logic.Passes.pass_filler import FillerPass
from Logic.Passes.pass_area_cutter import AreaCutterPass
from Logic.Passes.pass_resizer import ResizerPass
from Logic.neural_network import model

labels = ['call_me', 'fingers_crossed','okay','paper','peace','rock','rock_on','scissor','thumbs','up']

stock = FillerPass("Stock image")
gsoc = BGSubtractorGSOCPass("Background subtractor GSOC")
morph = MorphologyPass("Morphology pass")
cutter = AreaCutterPass("Area cutter")
resizer = ResizerPass("Resizer")

postprocessorPasses = [stock, gsoc, cutter, morph, resizer]
currentPassIndex = 0


def setCurrentPassIndex(new_index):
    global currentPassIndex
    currentPassIndex = new_index


def getCurrentPass():
    global postprocessorPasses
    global currentPassIndex
    if currentPassIndex < len(postprocessorPasses):
        return postprocessorPasses[currentPassIndex]
    else:
        return None


class PostprocessingImage(QLabel):
    def __init__(self, parentWidget, statusBar):
        super(QLabel, self).__init__()
        self.parentWidget = parentWidget

        self.worker = Worker(statusBar)
        self.worker.start()
        self.worker.frameCaptured.connect(self.onFrameCaptured)

    def __del__(self):
        self.worker.stop()

    def onFrameCaptured(self, image):
        self.setPixmap(QPixmap.fromImage(image))


class Worker(QThread):
    frameCaptured = pyqtSignal(QImage)
    postprocessor = Postprocessor(postprocessorPasses)
    isActive = False

    def __init__(self, statusBar):
        super(Worker, self).__init__()
        self.statusBar = statusBar

    def postprocessFrame(self, image):
        if currentPassIndex < len(postprocessorPasses):
            self.postprocessor.setImage(postprocessorPasses[currentPassIndex].apply(image))
        else:
            self.postprocessor.setImage(image).process()
        postprocessingResult = self.postprocessor.getImage()

        if currentPassIndex == len(postprocessorPasses):
            x = postprocessingResult.reshape(-1, 64, 64, 1)
            x = np.true_divide(x, 255)
            p = model.predict(x)
            self.statusBar.showMessage(labels[np.argmax(p)])

        return postprocessingResult

    def convertToQtFormat(self, image):
        result = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        result = cv.flip(result, 1)

        result = QImage(result.data, result.shape[1], result.shape[0], QImage.Format_RGB888)
        return result

    def run(self):
        self.isActive = True
        capture = cv.VideoCapture(0)
        while self.isActive:
            ret, frame = capture.read()
            if ret:
                postprocessingResult = self.postprocessFrame(frame)
                convertedToQt = self.convertToQtFormat(postprocessingResult)
                self.frameCaptured.emit(convertedToQt)
        capture.release()

    def stop(self):
        self.isActive = False
        self.quit()
