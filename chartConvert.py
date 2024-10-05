# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartConvert.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, ComboBox, LineEdit,
    PlainTextEdit, PrimaryPushButton, ToolButton)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1207, 750)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label = BodyLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = LineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = ToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_2 = BodyLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = LineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.toolButton_2 = ToolButton(Form)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_3.addWidget(self.toolButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = CheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = CheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = BodyLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.comboBox = ComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = BodyLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_3 = LineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.toolButton_3 = ToolButton(Form)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_5.addWidget(self.toolButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_5 = BodyLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.lineEdit_4 = LineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.label_6 = BodyLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.lineEdit_5 = LineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_10.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.plainTextEdit_2 = PlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.plainTextEdit_2)

        self.plainTextEdit = PlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setMaximumBlockCount(0)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = PrimaryPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(240, 60))
        self.pushButton.setMaximumSize(QSize(240, 60))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8981\u8f6c\u6362\u8c31\u9762\u5305\u76ee\u5f55\uff1a", None))
        self.toolButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u540e\u66f2\u5305\u76ee\u5f55\uff1a", None))
        self.toolButton_2.setText("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u5c1d\u8bd5\u8f6c\u6362\u56fe\u7247\u4e3aJPG", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u5c1d\u8bd5\u8f6c\u6362\u4e3a\u89c4\u8303\u97f3\u9891", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8981\u8f6c\u6362\u8c31\u9762\u6587\u4ef6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ffmpeg.exe \u4f4d\u7f6e\uff1a", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u82e5\u5f00\u542f\u8f6c\u6362\u97f3\u9891\u9009\u9879\uff0c\u5219\u6b64\u9879\u5fc5\u586b\uff01\u9ed8\u8ba4\u4f1a\u5c1d\u8bd5\u8bfb\u53d6\u8f6f\u4ef6.exe\u6587\u4ef6\u76ee\u5f55\u4e0b\u7684ffmpeg.exe", None))
        self.toolButton_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u66f2\u4f5c\u8005\uff1a", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u975ePJDL\u6a21\u5f0f\u53ef\u7528", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u96be\u5ea6\u540d\uff1a", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u975ePJDL\u6a21\u5f0f\u53ef\u7528", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u7528\u6765\u663e\u793a\u6b4c\u66f2\u4fe1\u606f\uff08\u4ec5PJDL\u6a21\u5f0f\u53ef\u7528\uff09", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u7528\u6765\u663e\u793a\u65e5\u5fd7", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8f6c\u6362", None))
    # retranslateUi

