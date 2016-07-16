# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClosingLibrarianDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClosingAppDialog(object):
    def setupUi(self, ClosingAppDialog):
        ClosingAppDialog.setObjectName("ClosingAppDialog")
        ClosingAppDialog.resize(308, 194)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClosingAppDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 241, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(ClosingAppDialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 231, 112))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.retranslateUi(ClosingAppDialog)
        self.buttonBox.accepted.connect(ClosingAppDialog.accept)
        self.buttonBox.rejected.connect(ClosingAppDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClosingAppDialog)

    def retranslateUi(self, ClosingAppDialog):
        _translate = QtCore.QCoreApplication.translate
        ClosingAppDialog.setWindowTitle(_translate("ClosingAppDialog", "Dialog"))
        self.label.setText(_translate("ClosingAppDialog", "Application is closing"))
        self.label_2.setText(_translate("ClosingAppDialog", "but you did not save"))
        self.label_3.setText(_translate("ClosingAppDialog", "your model or tags."))
        self.label_4.setText(_translate("ClosingAppDialog", "Do you want to save them?"))

