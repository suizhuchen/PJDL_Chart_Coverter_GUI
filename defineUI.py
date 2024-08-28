from PySide6.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF

import actions

from chartConvert import Ui_Form as Ui_ChartConvert


class ChartConvert(QWidget, Ui_ChartConvert):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toolButton.setIcon(FIF.MORE)
        self.toolButton.clicked.connect(lambda x: actions.ChartConvertAction.input_button_clicked(self))
        self.toolButton_2.setIcon(FIF.MORE)
        self.toolButton_2.clicked.connect(
            lambda x: actions.ChartConvertAction.output_button_clicked(self.lineEdit_2, self.lineEdit))
        self.pushButton.clicked.connect(
            lambda x: actions.ChartConvertAction.convert_button_clicked(self, self.lineEdit, self.lineEdit_2,
                                                                        self.checkBox, self.checkBox_2,
                                                                        self.plainTextEdit))
