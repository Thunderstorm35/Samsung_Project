from PyQt5.QtWidgets import *
from UI.postprocessingList import PostprocessingList
from UI.postprocessingImage import PostprocessingImage


class ContentArea(QSplitter):
    current_pass = None

    def __init__(self, statusBar):
        super(QSplitter, self).__init__()

        self.setLayout(QVBoxLayout())

        postprocessingList = PostprocessingList(self)
        self.addWidget(postprocessingList)

        postprocessingImage = PostprocessingImage(self, statusBar)
        self.addWidget(postprocessingImage)

        self.setChildrenCollapsible(False)
