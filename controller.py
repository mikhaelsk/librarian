from views import *
from models import *
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QFrame,
        QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy, QVBoxLayout,
        QWidget)

class LibrarianMainWindow(Ui_MainWindow):
    def __init__(self, window):
        
        ui = Ui_MainWindow()
        #ui.setupUi(mygui)
        Ui_MainWindow.__init__(self)
        self.setupUi(window)
        
    #def __init__(self):
     #   super().__init__()
     #   LibrarianMainWindow.setupUi()
      #  self.initUI()
        #QApplication.__init__(self, args)
        #self.maindialog = Ui_MainWindow()
        #self.setActiveWindow(self.maindialog)
        #self.maindialog.show()
        #self.exec()
    #def initUI(self):
     #   self.show()
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mygui = QtWidgets.QMainWindow()
    librarian = LibrarianMainWindow(mygui)
    mygui.show()
    sys.exit(app.exec_())
    
    
#http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
