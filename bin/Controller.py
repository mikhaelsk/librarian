from .views import *
from .models import *
from .utils import *
import sys
import os.path
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QFrame,
        QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy, QVBoxLayout,
        QWidget, QFileSystemModel, QAbstractItemView, QFileDialog, QInputDialog, QDialog, QPushButton, QLabel)

'''
main UI class inherited from the autogenerated by pyuic5 uimain.ui -o uimain.py
'''
class LibrarianMainWindow( Ui_MainWindow ):
        
    def __init__( self, window, mainController ):
        self.controller = mainController
        self.controller.SetMainWindow( self )
        ui = Ui_MainWindow()
        Ui_MainWindow.__init__( self )
        self.setupUi( window )
        self.inputPathLine.returnPressed.connect( self.AddFolder )
        self.inputPathLine.returnPressed.connect( self.AddFile )
        self.inputTagLine.returnPressed.connect( self.HandleAddTag )
        self.inputTagFilter.returnPressed.connect( self.HandleTagsApplied )
        self.controller.FinalizeInit()
      
        #self.addTagButton.clicked.connect(self.inputTagLine.update)
        #self.deleteTagButton.pressed.connect(self.listView.update)
        #self.inputTagFilter.returnPressed.connect(self.columnView.update)

    def setupUi( self, MainWindow ):
        super().setupUi( MainWindow )
        self.addFolderButton.clicked.connect( self.AddFolder )
        self.addFileButton.clicked.connect( self.AddFile )
        self.exitButton.triggered.connect( self.HandleClose )
        self.addTagButton.clicked.connect( self.HandleAddTag )
        self.deleteTagButton.clicked.connect( self.HandleDelTag )
        self.delFileFromLibButton.clicked.connect( self.HandleDelFileFromLib )
        self.listView.doubleClicked.connect( self.HandleClickOnTag )
        #self.listView.setSelectionMode( QAbstractItemView.ExtendedSelection )
        self.treeView.setSelectionMode( QAbstractItemView.ExtendedSelection )
        self.setTagsButton.clicked.connect( self.HandleSetTags )
        self.updateFilterButton.clicked.connect( self.HandleTagsApplied )
        self.createLibraryButton.triggered.connect( self.HandleCreateLib )
        self.openLibraryButton.triggered.connect( self.HandleOpenLib ) 
        self.saveLibraryButton.triggered.connect( self.HandleSaveLib )       
        self.saveLibraryToFileButton.triggered.connect( self.HandleSaveLibToFile )       
  
    '''
    Slots for signals:
    '''
    def AddFolder( self ):
        self.controller.AddFolder( self.inputPathLine.text() )
    
    def AddFile( self ):
        self.controller.AddFile( self.inputPathLine.text() )    

    def HandleClose( self ):
        #if self.controller.wereAnyChanges == True:
        #    dialog = QDialog()
            #dialog.setWindowModality( Qt.ApplicationModal )
        #    mydialog = CloseDialog( dialog )
        #    dialog.show()
        self.controller.SaveTags()

    def HandleAddTag( self ):
        self.controller.AddTag( self.inputTagLine.text() )
        #self.listView.update()

    def HandleDelTag( self ):
        self.controller.DelTag( self.listView.selectedIndexes() )

    def HandleSetTags( self ):
        self.controller.HandleSetTags()

    def HandleClickOnTag( self ):
        index = self.listView.selectedIndexes()[ 0 ]
        tagStr = self.controller.GetTagTextByIndex( index )
        self.inputTagFilter.setText( self.inputTagFilter.text() + tagStr + ' ' )
        #self.controller.nowActiveTags.add( tagStr )

    def HandleTagsApplied( self ):
        listOfTagsInStr = self.inputTagFilter.text().split()
        self.controller.FilterTheModel( listOfTagsInStr )

    def HandleDelFileFromLib( self ):
        self.controller.DelFilesFromLib( self.treeView.selectedIndexes() )

    def HandleOpenLib( self ):
        fname = QFileDialog.getOpenFileName( caption = 'Open Library Storage', filter="Libraries (*.lib)" )[ 0 ]        
        self.controller.ReadLibraryFromFile( fname )
        
        
    def HandleCreateLib( self ):
        text, ok = QInputDialog.getText( self.centralwidget, 'Create Library', 'Enter library name:' )
        if ok:
            self.controller.CreateNewLib( str( text ) )

    def HandleSaveLib( self ):
        self.controller.SaveModel()

    def HandleSaveLibToFile( self ):
        fname = QFileDialog.getSaveFileName( caption = 'Save Library to File', filter="Libraries (*.lib)" )[ 0 ]
        self.controller.SaveModel( fname )

    def EnableDisableExitButton( self, state ):
        self.saveLibraryButton.setEnabled( not state )
        self.saveLibraryToFileButton.setEnabled( not state )
        self.exitButton.setEnabled( state ) 
        QApplication.processEvents()

class CloseDialog( Ui_ClosingAppDialog ):
    def __init__( self, qdialog ):
        ui = Ui_ClosingAppDialog()
        Ui_ClosingAppDialog.__init__( self )
        self.setupUi( qdialog )
    def accept( self ):
        pass
    def reject( self ):
        pass
        
class Controller():
    def __init__( self ):
        self.logger = Logger()        
        self.model = MainModel( self )
        self.tags = Tags( self )
        self.logger.WriteToLog( "Init Done\n" )
        self.tagToItemDict = {}
        self.tagToNumOfDocsDict = {}
        self.nowActiveTags = set()
        self.wereAnyChangesInModel = False
        self.wereAnyChangesInTags = False
        self.currentLibFileName = None

    def FinalizeInit( self ):
        self.mainwindow.treeView.setModel( self.model.library )
        self.mainwindow.listView.setModel( self.tags.tagModel )
        self.mainwindow.tableView.setModel( self.model.filteredModel )
        self.mainwindow.tableView.resizeColumnsToContents()
        self.mainwindow.EnableDisableExitButton( True )
        self.mainwindow.exitButton.setEnabled( True )
        
    def PrintToLog( self, txt ):
        self.logger.WriteToLog( txt )

    def SetMainWindow( self, newMainWindow ):
        self.mainwindow = newMainWindow

    def UpdateLibraryView( self ):
        self.mainwindow.treeView.setModel( self.model.library )

    def AddFolder( self, txt ):
        if os.path.isdir( txt ):
            self.logger.WriteToLog( 'Added new path: ' + txt )
            self.model.AddFolder( txt )  
        self.mainwindow.numOfDocsLabel.setText( str( self.model.numberOfDocs ) )
        self.mainwindow.numOfTagedDocsLabel.setText( str( self.model.numberOfTagedDocs ) )
        self.mainwindow.tableView.resizeColumnsToContents()
        self.wereAnyChangesInModel = True
        #self.mainwindow.EnableDisableExitButton( False )
    
    def AddFile( self, txt ):
        if os.path.isfile( txt ):
            self.logger.WriteToLog( 'Added new path: ' + txt )
            self.model.AddFile( txt )  
        self.mainwindow.numOfDocsLabel.setText( str( self.model.numberOfDocs ) )
        self.mainwindow.numOfTagedDocsLabel.setText( str( self.model.numberOfTagedDocs ) )
        self.mainwindow.tableView.resizeColumnsToContents()
        self.wereAnyChangesInModel = True
        self.mainwindow.EnableDisableExitButton( False )

    def SaveModel( self, filename = None ):
        if self.wereAnyChangesInTags == True:
            self.tags.SaveTagModel()
            self.wereAnyChangesInTags = False
        if self.wereAnyChangesInModel == True:
            if self.currentLibFileName == None:
                return #no lib was created; user exited by red cross
            if filename == None:
                filename = self.currentLibFileName
            self.SaveLibrary( filename )
            self.model.SaveLibrary()
            #self.tags.SaveTagModel()
            self.wereAnyChangesInModel = False
            self.mainwindow.EnableDisableExitButton( True )

    def SaveTags( self ):
        self.tags.SaveTagModel()

    def AddTag( self, txt ):
        self.tags.AddTag( txt )
        self.wereAnyChangesInTags = True
        #self.mainwindow.EnableDisableExitButton( False )

    def DelTag( self, selectedItemIndexes ):
        self.tags.DelTag( selectedItemIndexes )
        self.wereAnyChangesInTags = True
        #self.mainwindow.EnableDisableExitButton( False )

    def HandleSetTags( self ):
        tagsSelected = []
        selectedIndexesInTreeView = self.mainwindow.treeView.selectedIndexes()
        count = len( selectedIndexesInTreeView )
        for tagName in self.tags.tagDict.keys():
            tagItem = self.tags.tagDict[ tagName ]
            if tagItem.checkState() == Qt.Checked:
                tagsSelected.append( tagName )
                if tagName in self.tagToItemDict.keys():
                    self.tagToNumOfDocsDict[ tagName ] += count
                else:
                    self.tagToNumOfDocsDict[ tagName ] = count
                    self.tagToItemDict[ tagName ] = [] #set()
                
        #fill the tag to item dictionary
        for index in selectedIndexesInTreeView:
             item = self.model.library.itemFromIndex( index )
             for tag in tagsSelected:
                 item.tagsList.append( tag )
             for tag in tagsSelected:
                 self.tagToItemDict[ tag ].append( item.accessibleText() )
                 #add( item.text() )
        self.wereAnyChangesInModel = True
        self.mainwindow.EnableDisableExitButton( False )

    def GetTagTextByIndex( self, index ):
        return self.tags.tagModel.itemFromIndex( index ).text()

    def FilterTheModel( self, listOfTags ):
        #arrange tags by the minimal count of documents with this tag:
        if listOfTags == []:
            return
        currentTagToNumOfDocsDict = {}
        try:
            for tagName in listOfTags:
                currentTagToNumOfDocsDict[ tagName ] = self.tagToNumOfDocsDict[ tagName ]
        except KeyError:
            currentItemList = None 
        else:
            lambdaFunc = lambda x: x[ 1 ]
            currentTagToNumOfDocsDict = sorted( currentTagToNumOfDocsDict.items(), key=lambdaFunc, reverse=False )
            lengthOfList = len( listOfTags )
            currentItemList = set( self.tagToItemDict[ currentTagToNumOfDocsDict[ 0 ][ 0 ] ] )
            countOfIntersections = 1
            while countOfIntersections < lengthOfList:
                currentItemList = currentItemList & set( self.tagToItemDict[ currentTagToNumOfDocsDict[ countOfIntersections ][ 0 ] ] )
                countOfIntersections += 1
        finally:           
            self.model.UpdateFilteredModel( currentItemList )
            self.mainwindow.numOfTagedDocsLabel.setText( str( self.model.numberOfTagedDocs ) )

    def DelFilesFromLib( self, indexes ):
        self.model.DelItems( indexes )
        self.mainwindow.numOfDocsLabel.setText( str( self.model.numberOfDocs ) )
        self.wereAnyChangesInModel = True
        self.mainwindow.EnableDisableExitButton( False )

    def RefreshFilteredView( self ):
        self.mainwindow.tableView.resizeColumnsToContents()

    def ReadLibraryFromFile( self, fname ):
        self.currentLibFileName = fname
        self.model.InitLibrary( fname )
        myLibFile = open( fname, 'r' )
        with myLibFile:
            #TODO parse xml
            pass #data = f.read()

    def CreateNewLib( self, libName ):
        self.model.InitLibrary( libName )
        self.wereAnyChangesInModel = True
        self.mainwindow.EnableDisableExitButton( False )
        self.currentLibFileName = libName + ".lib"

    def SaveLibrary( self, fileName ):
        xmlWriter = QXmlStreamWriter()
        xmlFile = QFile( fileName )
        if ( xmlFile.open( QIODevice.WriteOnly ) == False ):    
            QMessageBox.warning( 0, "Error!", "Error opening file" )  
            QFile.remove( fileName )
            xmlOldFile.rename( fileName )  
        else :    
            xmlWriter.setDevice( xmlFile )	
            xmlWriter.writeStartDocument()
            xmlWriter.writeStartElement( self.model.root.text() ) #write the library name
            #TODO parse treeview model to file 
            xmlWriter.writeEndElement()
            xmlWriter.writeEndDocument()
            
