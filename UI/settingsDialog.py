from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Logic.Passes.pass_base import ParamType


class SettingsDialog(QDialog):
    def __init__(self, params):
        super(QDialog, self).__init__()
        self.setWindowTitle("Settings Dialog")

        layout = QVBoxLayout()

        self.paramsList = params.getParamsList()
        for param in self.paramsList:
            label = QLabel(param.getName())
            layout.addWidget(label)

            if param.getType() == ParamType.SLIDER:
                slider = QSlider(Qt.Horizontal)
                slider.valueChanged.connect(self.onSliderSettingChanged(param))
                slider.setMinimum(param.getMin())
                slider.setMaximum(param.getMax())
                slider.setValue(param.getValue())
                layout.addWidget(slider)

            elif param.getType() == ParamType.NUMBER:
                spinBox = QSpinBox()
                spinBox.valueChanged.connect(self.onSpinBoxSettingChanged(spinBox, param))
                spinBox.setMinimum(param.getMin())
                spinBox.setMaximum(param.getMax())
                spinBox.setValue(param.getValue())
                layout.addWidget(spinBox)

        self.setLayout(layout)

    @staticmethod
    def onSliderSettingChanged(param):
        def func(value):
            param.setValue(value)
        return func

    @staticmethod
    def onSpinBoxSettingChanged(spinBox, param):
        def func():
            param.setValue(spinBox.value())
        return func
