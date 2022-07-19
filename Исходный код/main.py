import sys
from PyQt5.QtWidgets import *
from UI.contentArea import ContentArea
from UI.settingsDialog import SettingsDialog
from UI.postprocessingImage import getCurrentPass
from Logic.Passes.pass_base import PassWithParams

TITLE = "Main window"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(TITLE)

        self._createMenuBar()
        self._createContentArea(self.statusBar())

    def _createMenuBar(self):
        menuBar = self.menuBar()

        exitMenu = menuBar.addAction("&Exit")
        exitMenu.triggered.connect(qApp.quit)

        settingsMenu = menuBar.addAction("&Settings")
        settingsMenu.triggered.connect(self._showSettingsDialog)

    def _createContentArea(self, statusBar):
        contentArea = ContentArea(statusBar)
        self.setCentralWidget(contentArea)

    @staticmethod
    def _showSettingsDialog():
        currentPass = getCurrentPass()
        if isinstance(currentPass, PassWithParams):
            settingsDialog = SettingsDialog(currentPass.params)
            settingsDialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
