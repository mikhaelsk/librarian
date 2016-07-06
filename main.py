from bin import *
'''
MAIN function of this application
'''
if __name__ == "__main__":
    app = QApplication( sys.argv )
    mygui = QtWidgets.QMainWindow()
    controller = Controller()
    librarian = LibrarianMainWindow( mygui, controller )
    mygui.show()
    
    sys.exit( app.exec_() )