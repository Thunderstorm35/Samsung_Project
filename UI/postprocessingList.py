from PyQt5.QtWidgets import *
from UI.postprocessingImage import postprocessorPasses, setCurrentPassIndex


class PostprocessingList(QListWidget):
    def __init__(self, parentWidget):
        super(QListWidget, self).__init__()
        self.parentWidget = parentWidget

        self.addItems([__pass__.name for __pass__ in postprocessorPasses])
        self.addItem("Postprocessing result")
        self.setMinimumWidth(250)

        self.currentItemChanged.connect(self.index_changed)

    def index_changed(self, i):
        setCurrentPassIndex(self.currentIndex().row())



