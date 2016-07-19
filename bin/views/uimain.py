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
        MainWindow.resize(1047, 715)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setIndent(1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.inputPathLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPathLine.sizePolicy().hasHeightForWidth())
        self.inputPathLine.setSizePolicy(sizePolicy)
        self.inputPathLine.setMinimumSize(QtCore.QSize(300, 0))
        self.inputPathLine.setObjectName("inputPathLine")
        self.horizontalLayout_3.addWidget(self.inputPathLine)
        self.addFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFolderButton.setObjectName("addFolderButton")
        self.horizontalLayout_3.addWidget(self.addFolderButton)
        self.addFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFileButton.setObjectName("addFileButton")
        self.horizontalLayout_3.addWidget(self.addFileButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setIndent(2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.numOfDocsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numOfDocsLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.numOfDocsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfDocsLabel.setObjectName("numOfDocsLabel")
        self.horizontalLayout_3.addWidget(self.numOfDocsLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.delFileFromLibButton = QtWidgets.QPushButton(self.centralwidget)
        self.delFileFromLibButton.setObjectName("delFileFromLibButton")
        self.horizontalLayout_3.addWidget(self.delFileFromLibButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setIndent(2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.numOfTagedDocsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numOfTagedDocsLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.numOfTagedDocsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfTagedDocsLabel.setObjectName("numOfTagedDocsLabel")
        self.horizontalLayout_3.addWidget(self.numOfTagedDocsLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        self.treeView.setObjectName("treeView")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setIndent(1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.inputTagLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputTagLine.setMinimumSize(QtCore.QSize(150, 0))
        self.inputTagLine.setObjectName("inputTagLine")
        self.horizontalLayout_8.addWidget(self.inputTagLine)
        self.addTagButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTagButton.sizePolicy().hasHeightForWidth())
        self.addTagButton.setSizePolicy(sizePolicy)
        self.addTagButton.setObjectName("addTagButton")
        self.horizontalLayout_8.addWidget(self.addTagButton)
        self.deleteTagButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteTagButton.setObjectName("deleteTagButton")
        self.horizontalLayout_8.addWidget(self.deleteTagButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.tagTableView = QtWidgets.QTableView(self.layoutWidget)
        self.tagTableView.setObjectName("tagTableView")
        self.verticalLayout.addWidget(self.tagTableView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.setTagsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.setTagsButton.setEnabled(True)
        self.setTagsButton.setObjectName("setTagsButton")
        self.horizontalLayout_4.addWidget(self.setTagsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableView = QtWidgets.QTableView(self.splitter_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setIndent(1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.inputTagFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTagFilter.setObjectName("inputTagFilter")
        self.horizontalLayout_7.addWidget(self.inputTagFilter)
        self.updateFilterButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateFilterButton.setObjectName("updateFilterButton")
        self.horizontalLayout_7.addWidget(self.updateFilterButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 60)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 21))
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
        self.addFileMenuBut.setEnabled(True)
        self.addFileMenuBut.setObjectName("addFileMenuBut")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.openLibraryButton = QtWidgets.QAction(MainWindow)
        self.openLibraryButton.setObjectName("openLibraryButton")
        self.exitButton = QtWidgets.QAction(MainWindow)
        self.exitButton.setEnabled(True)
        self.exitButton.setObjectName("exitButton")
        self.createLibraryButton = QtWidgets.QAction(MainWindow)
        self.createLibraryButton.setObjectName("createLibraryButton")
        self.saveLibraryButton = QtWidgets.QAction(MainWindow)
        self.saveLibraryButton.setObjectName("saveLibraryButton")
        self.saveLibraryToFileButton = QtWidgets.QAction(MainWindow)
        self.saveLibraryToFileButton.setObjectName("saveLibraryToFileButton")
        self.doNotSaveExitButton = QtWidgets.QAction(MainWindow)
        self.doNotSaveExitButton.setObjectName("doNotSaveExitButton")
        self.saveTagsButton = QtWidgets.QAction(MainWindow)
        self.saveTagsButton.setObjectName("saveTagsButton")
        self.closeLibraryButton = QtWidgets.QAction(MainWindow)
        self.closeLibraryButton.setObjectName("closeLibraryButton")
        self.actionDon_t_Save_and_Close_Library = QtWidgets.QAction(MainWindow)
        self.actionDon_t_Save_and_Close_Library.setObjectName("actionDon_t_Save_and_Close_Library")
        self.menu.addAction(self.addFileMenuBut)
        self.menu.addAction(self.addFolderMenuBut)
        self.menu.addSeparator()
        self.menu.addAction(self.createLibraryButton)
        self.menu.addAction(self.openLibraryButton)
        self.menu.addSeparator()
        self.menu.addAction(self.saveLibraryButton)
        self.menu.addAction(self.saveLibraryToFileButton)
        self.menu.addAction(self.saveTagsButton)
        self.menu.addSeparator()
        self.menu.addAction(self.closeLibraryButton)
        self.menu.addSeparator()
        self.menu.addAction(self.exitButton)
        self.menu.addAction(self.doNotSaveExitButton)
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
        self.label_2.setText(_translate("MainWindow", "Total number of documents:"))
        self.numOfDocsLabel.setText(_translate("MainWindow", "0"))
        self.delFileFromLibButton.setText(_translate("MainWindow", "Delete From Library"))
        self.label_3.setText(_translate("MainWindow", "Taged documents:"))
        self.numOfTagedDocsLabel.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Tag Editor:"))
        self.addTagButton.setText(_translate("MainWindow", "add"))
        self.deleteTagButton.setText(_translate("MainWindow", "del"))
        self.setTagsButton.setText(_translate("MainWindow", "Set checked Tags for selected Items in treeview"))
        self.label_4.setText(_translate("MainWindow", "Tag Filter:"))
        self.updateFilterButton.setText(_translate("MainWindow", "Update the Filtered Library!"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.label_6.setText(_translate("MainWindow", "Ok"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Вид"))
        self.menu_3.setTitle(_translate("MainWindow", "Справка"))
        self.addFolderMenuBut.setText(_translate("MainWindow", "Add Folder"))
        self.addFileMenuBut.setText(_translate("MainWindow", "Add File"))
        self.action_3.setText(_translate("MainWindow", "About"))
        self.openLibraryButton.setText(_translate("MainWindow", "Open Library"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.createLibraryButton.setText(_translate("MainWindow", "Create New Library"))
        self.saveLibraryButton.setText(_translate("MainWindow", "Save Library"))
        self.saveLibraryToFileButton.setText(_translate("MainWindow", "Save Library To File"))
        self.doNotSaveExitButton.setText(_translate("MainWindow", "Don\'t Save and Exit"))
        self.saveTagsButton.setText(_translate("MainWindow", "Save Tags"))
        self.closeLibraryButton.setText(_translate("MainWindow", "Close Library"))
        self.actionDon_t_Save_and_Close_Library.setText(_translate("MainWindow", "Don\'t Save and Close Library"))

