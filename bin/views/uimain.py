# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uimain.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 681)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setIndent(1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.inputPathLine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPathLine.setObjectName("inputPathLine")
        self.horizontalLayout_3.addWidget(self.inputPathLine)
        self.addFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFolderButton.setObjectName("addFolderButton")
        self.horizontalLayout_3.addWidget(self.addFolderButton)
        self.addFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFileButton.setObjectName("addFileButton")
        self.horizontalLayout_3.addWidget(self.addFileButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setIndent(2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(40, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setIndent(1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.inputTagLine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTagLine.setMinimumSize(QtCore.QSize(150, 0))
        self.inputTagLine.setObjectName("inputTagLine")
        self.horizontalLayout_8.addWidget(self.inputTagLine)
        self.addTagButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTagButton.sizePolicy().hasHeightForWidth())
        self.addTagButton.setSizePolicy(sizePolicy)
        self.addTagButton.setObjectName("addTagButton")
        self.horizontalLayout_8.addWidget(self.addTagButton)
        self.deleteTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteTagButton.setObjectName("deleteTagButton")
        self.horizontalLayout_8.addWidget(self.deleteTagButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout_5.addWidget(self.listView)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setObjectName("columnView")
        self.horizontalLayout_4.addWidget(self.columnView)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 25)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setIndent(1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.inputTagFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTagFilter.setObjectName("inputTagFilter")
        self.horizontalLayout_7.addWidget(self.inputTagFilter)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setScaledContents(True)
        self.label.setIndent(1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setIndent(1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 60)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addFolderMenuBut = QtWidgets.QAction(MainWindow)
        self.addFolderMenuBut.setObjectName("addFolderMenuBut")
        self.addFileMenuBut = QtWidgets.QAction(MainWindow)
        self.addFileMenuBut.setObjectName("addFileMenuBut")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.exitButton = QtWidgets.QAction(MainWindow)
        self.exitButton.setObjectName("exitButton")
        self.menu.addAction(self.addFolderMenuBut)
        self.menu.addAction(self.addFileMenuBut)
        self.menu.addSeparator()
        self.menu.addAction(self.exitButton)
        self.menu_3.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.exitButton.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Librarian 0.1"))
        MainWindow.setAccessibleName(_translate("MainWindow", "lib_main"))
        MainWindow.setAccessibleDescription(_translate("MainWindow", "librarian program"))
        self.label_7.setText(_translate("MainWindow", "Path:"))
        self.addFolderButton.setText(_translate("MainWindow", "Add Folder"))
        self.addFileButton.setText(_translate("MainWindow", "Add File"))
        self.label_2.setText(_translate("MainWindow", "Number of documents:"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Tag Editor:"))
        self.addTagButton.setText(_translate("MainWindow", "add"))
        self.deleteTagButton.setText(_translate("MainWindow", "del"))
        self.label_4.setText(_translate("MainWindow", "Tag Filter:"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.label_6.setText(_translate("MainWindow", "Ok"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Вид"))
        self.menu_3.setTitle(_translate("MainWindow", "Справка"))
        self.addFolderMenuBut.setText(_translate("MainWindow", "Add Folder"))
        self.addFileMenuBut.setText(_translate("MainWindow", "Add File"))
        self.action_3.setText(_translate("MainWindow", "About"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))

