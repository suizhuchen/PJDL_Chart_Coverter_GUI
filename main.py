# coding:utf-8
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FIF

from defineUI import ChartConvert


class Window(FluentWindow):

    def __init__(self):
        super().__init__()
        self.define_sub_windows()

        self.setWindowIcon(QIcon('./icons/winicon.png'))
        self.setWindowTitle('啤酒道理谱儿面转换器')
        self.resize(1200, 800)

    def define_sub_windows(self):
        self.ui_chart_convert = ChartConvert()

        self.addSubInterface(self.ui_chart_convert, FIF.SAVE_AS, '谱面转换')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    app.exec()
