from .views import *
from .models import *
from .utils import *
import sys
import os.path
from PyQt5.QtXml import *
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
        #self.deleteTagButton.pressed.connect(self.tagTableView.update)
        #self.inputTagFilter.returnPressed.connect(self.columnView.update)

    def setupUi( self, MainWindow ):
        super().setupUi( MainWindow )
        self.addFolderButton.clicked.connect( self.AddFolder )
        self.addFileButton.clicked.connect( self.AddFile )
        self.exitButton.triggered.connect( self.HandleClose )
        self.addTagButton.clicked.connect( self.HandleAddTag )
        self.deleteTagButton.clicked.connect( self.HandleDelTag )
        self.delFileFromLibButton.clicked.connect( self.HandleDelFileFromLib )
        self.tagTableView.doubleClicked.connect( self.HandleClickOnTag )
        #self.tagTableView.setSelectionMode(
        #QAbstractItemView.ExtendedSelection )
        self.treeView.setSelectionMode( QAbstractItemView.ExtendedSelection )
        self.setTagsButton.clicked.connect( self.HandleSetTags )
        self.updateFilterButton.clicked.connect( self.HandleTagsApplied )
        self.createLibraryButton.triggered.connect( self.HandleCreateLib )
        self.openLibraryButton.triggered.connect( self.HandleOpenLib ) 
        self.saveLibraryButton.triggered.connect( self.HandleSaveLib )       
        self.saveLibraryToFileButton.triggered.connect( self.HandleSaveLibToFile )   
        self.saveTagsButton.triggered.connect( self.HandleSaveTags )
        self.doNotSaveExitButton.triggered.connect( self.HandleDoNotSave )
        self.closeLibraryButton.triggered.connect( self.HandleCloseLibrary )    
  
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
        #self.tagTableView.update()

    def HandleDelTag( self ):
        self.controller.DelTag( self.tagTableView.selectedIndexes() )

    def HandleSetTags( self ):
        self.controller.HandleSetTags()

    def HandleClickOnTag( self ):
        index = self.tagTableView.selectedIndexes()[ 0 ]
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
        if fname == "":
            return      
        self.controller.ReadLibraryFromFile( fname )        
        
    def HandleCreateLib( self ):
        text, ok = QInputDialog.getText( self.centralwidget, 'Create Library', 'Enter library name:' )
        if ok:
            self.controller.CreateNewLib( str( text ) )

    def HandleSaveLib( self ):
        self.controller.SaveModel()

    def HandleSaveLibToFile( self ):
        fname = QFileDialog.getSaveFileName( caption = 'Save Library to File', filter="Libraries (*.lib)" )[ 0 ]
        if fname == "":
            return
        self.controller.SaveModel( fname )

    def HandleSaveTags( self ):
        self.controller.SaveTags()

    def HandleDoNotSave( self ):
        self.controller.SetDoNotSave()

    def HandleCloseLibrary( self ):
        self.controller.CloseLibrary()

    def EnableDisableExitButton( self, state ):
        self.saveLibraryButton.setEnabled( not state )
        self.saveLibraryToFileButton.setEnabled( not state )
        self.exitButton.setEnabled( state )
        self.createLibraryButton.setEnabled( state )
        self.openLibraryButton.setEnabled( state ) 
        self.closeLibraryButton.setEnabled( not state )
        QApplication.processEvents()
    
    def EnableDisableCloseButton( self, state ):
        self.closeLibraryButton.setEnabled( state )
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
        self.doNotSaveFlag = False
        self.parsedElement = None

    def FinalizeInit( self ):
        self.mainwindow.treeView.setModel( self.model.library )
        self.mainwindow.tagTableView.setSortingEnabled( True )
        self.mainwindow.tagTableView.setModel( self.tags.tagModel )
        self.mainwindow.tableView.setSortingEnabled( True )
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
            self.parsedElement = self.model.AddFile( txt )  
        self.mainwindow.numOfDocsLabel.setText( str( self.model.numberOfDocs ) )
        self.mainwindow.numOfTagedDocsLabel.setText( str( self.model.numberOfTagedDocs ) )
        self.mainwindow.tableView.resizeColumnsToContents()
        self.wereAnyChangesInModel = True
        self.mainwindow.EnableDisableExitButton( False )

    def SaveModel( self, filename = None ):
        if self.doNotSaveFlag == True:
            return
        if self.wereAnyChangesInTags == True:
            self.tags.SaveTagModel()
            self.wereAnyChangesInTags = False
        if self.wereAnyChangesInModel == True:
            if filename == "":
                return   #user did not select filename and closed the dialog window
            if filename == None:
                filename = self.currentLibFileName
            self.SaveLibrary( filename )
            #self.model.SaveLibrary()
            #self.tags.SaveTagModel()
            self.wereAnyChangesInModel = False
            self.mainwindow.EnableDisableExitButton( True )
            self.mainwindow.EnableDisableCloseButton( True )

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
                    currentCount = int( self.tags.tagNameToTagItemsDict[ tagName ][ 1 ].text() ) 
                    self.tags.tagNameToTagItemsDict[ tagName ][ 1 ].setText( str( currentCount + 1 ) )
                else:
                    self.tagToNumOfDocsDict[ tagName ] = count
                    self.tagToItemDict[ tagName ] = [] #set()
                    self.tags.tagNameToTagItemsDict[ tagName ][ 1 ].setText( str( count ) )
                
                
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

    def SetTagToItem( self, item, tagName ):
        if tagName in self.tagToItemDict.keys():
            self.tagToNumOfDocsDict[ tagName ] += 1
        else:
            self.tagToNumOfDocsDict[ tagName ] = 1
            self.tagToItemDict[ tagName ] = []
        item.tagsList.append( tagName )
        self.tagToItemDict[ tagName ].append( item.accessibleText() )
        currentCount = int( self.tags.tagNameToTagItemsDict[ tagName ][ 1 ].text() ) 
        self.tags.tagNameToTagItemsDict[ tagName ][ 1 ].setText( str( currentCount + 1 ) ) 
        #self.tags.UpdateNumInModel()

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
        self.mainwindow.numOfTagedDocsLabel.setText( str( self.model.numberOfTagedDocs ) )

    def RefreshFilteredView( self ):
        self.mainwindow.tableView.resizeColumnsToContents()

    def ReadLibraryFromFile( self, fileName ):
        self.currentLibFileName = fileName
        #self.model.OpenLibrary( fname )
        xmlParser = QXmlSimpleReader()
        xmlContentHandler = myXmlContentHandlerForModel( self )
        xmlFile = QFile( fileName )
        xmlInputSource = QXmlInputSource( xmlFile )    
        xmlParser.setContentHandler( xmlContentHandler )  
      
        if( xmlParser.parse( xmlInputSource ) ):
            self.PrintToLog( "Library successfully loaded!" )
            self.mainwindow.EnableDisableExitButton( False )
        else:  
            self.PrintToLog( "Parsing of library Failed!" )
            self.mainwindow.EnableDisableExitButton( True )

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
            xmlWriter.writeStartElement( "root" ) #write the library name
            xmlWriter.writeAttribute( "name", self.model.root.text() )
            self.GetAndSaveChildItems( xmlWriter, self.model.root )
            '''
            itemNameList = list( self.itemNameToItemDict.keys() )
            itemNameList.sort()
            for itemName in itemNameList:
                currentItem = self.itemNameToItemDict[ itemName ]
                if currentItem.accessibleDescription != "dir":
                    pass
            '''
            #for item in self.model.root#TODO parse treeview model to file
            xmlWriter.writeEndElement()
            xmlWriter.autoFormattingIndent()
            xmlWriter.writeEndDocument()
        return True

    def GetAndSaveChildItems( self, xmlWriter, parentItem ):
        if parentItem.childCount != 0:
            childList = parentItem.GetChilds()
            childList.sort()
            dirChildList = []
            for item in childList:
                if item.accessibleDescription() == "dir":
                    dirChildList.append( item )
                else:
                    xmlWriter.writeStartElement( "element" )
                    xmlWriter.writeAttribute( "name", item.accessibleText() )
                    for tag in item.tagsList:
                        xmlWriter.writeStartElement( "tag" )
                        xmlWriter.writeAttribute( "name", tag )
                        xmlWriter.writeEndElement()
                    
                    self.GetAndSaveChildItems( xmlWriter, item )
                    xmlWriter.writeEndElement()
                    xmlWriter.autoFormattingIndent()
            
            for item in dirChildList:
                self.GetAndSaveChildItems( xmlWriter, item )

    def SetDoNotSave( self ):
        self.doNotSaveFlag = True
        #os.system(cmd)
        QtCore.QCoreApplication.instance().quit()

    def CloseLibrary( self ):
        self.SaveModel()
        self.model.CloseLibrary()
        self.tagToItemDict = {}
        self.tagToNumOfDocsDict = {}
        self.mainwindow.treeView.setModel( self.model.library )
        #self.mainwindow.EnableDisableExitButton( True )
        self.mainwindow.numOfDocsLabel.setText( "0" )
        self.mainwindow.numOfTagedDocsLabel.setText( "0" )
        self.parsedElement = None
        

class myXmlContentHandlerForModel( QXmlDefaultHandler ):    
    def __init__( self, controller ):
        super().__init__()
        self.controller = controller
        self.model = controller.model
        self.currentItem = None

    def startElement( self, nameSpaceURI, localName, qName, atts ):
        if localName == "root":
            if atts.localName( 0 ) == "name":
                self.model.InitLibrary( atts.value( 0 ) )
            else:
                return False
        elif localName == "element":
            if atts.localName( 0 ) == "name":
                #self.currentItem = QStandardItem( atts.value( 0 ) )
                #self.model.root.setChild( self.currentItem )
                self.controller.AddFile( atts.value( 0 ) )
            else:
                return False
        elif localName == "tag":
            if atts.localName( 0 ) == "name":
                self.controller.SetTagToItem( self.controller.parsedElement, atts.value( 0 ) )
                            
        #    self.myTags.AddTag( localName )
        return True
            
