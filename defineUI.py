from PySide6.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF

import actions

from chartConvert import Ui_Form as Ui_ChartConvert


class ChartConvert(QWidget, Ui_ChartConvert):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        chartConvertAction = actions.ChartConvertAction(self)

        self.toolButton.setIcon(FIF.MORE)
        self.toolButton.clicked.connect(lambda x: chartConvertAction.input_button_clicked())
        self.toolButton_2.setIcon(FIF.MORE)
        self.toolButton_2.clicked.connect(
            lambda x: chartConvertAction.output_button_clicked())
        self.toolButton_3.setIcon(FIF.MORE)
        self.toolButton_3.clicked.connect(
            lambda x: chartConvertAction.ffmpeg_button_clicked())
        self.pushButton.clicked.connect(
            lambda x: chartConvertAction.convert_button_clicked())
        self.comboBox.currentIndexChanged.connect(
            lambda x: chartConvertAction.chart_type_changed(x))
        chartConvertAction.window_init()
