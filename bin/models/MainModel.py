#from .Library import *
#from ..Controller import *
from .LibStandardItem import *
import os.path
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

#from PyQt5.QtCore import QAbstractTableModel
class MainModel():
    """files and folders model"""
    numberOfDocs = 0
    numberOfTagedDocs = 0
    def __init__( self, myController ):
        self.nodeId = 0
        self.controller = myController
        '''
        setup complete library model for treeView
        '''
        #libName = "MyLibrary"
        self.library = QStandardItemModel( 0,1 )
        self.library.setHeaderData( 0, QtCore.Qt.Horizontal, QtCore.QVariant( "TreeView of Library:" ) )
        #self.root = QStandardItem( libName )
        #self.controller.PrintToLog( "Library initialized: " + libName )
        #self.library.appendRow( self.root )
        self.itemNameToItemDict = {}
        
        #self.itemNameList = []
        
        '''
        now setup the filtered model for tableView
        '''
        self.filteredModel = QStandardItemModel( 0,1 )
        self.filteredModel.setColumnCount( 2 )
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file" ] )
    
    def InitLibrary( self, libName = "MyLibrary" ):
        self.root = LibStandardItem( libName )
        self.library.appendRow( self.root )
        self.controller.PrintToLog( "Library initialized: " + libName )  
           
    def AddFolder( self, folderPath ):
        for ( paths,dirs,files ) in os.walk( folderPath ):
            for file in files:
                self.controller.PrintToLog( "Found File: " + paths + "\\" + file )
                pathList = self.ParseDirPath( paths )
                self._AddFileIntro( paths + "\\" + file, pathList, file )
        self.controller.UpdateLibraryView()       

    def AddFile( self, pathAndName ):
        curPath = os.path.dirname( pathAndName )
        curName = os.path.basename( pathAndName )
        pathList = self.ParseDirPath( curPath )
        self._AddFileIntro( pathAndName, pathList, curName )
        self.controller.PrintToLog( "Found File: " + pathAndName )
        self.controller.UpdateLibraryView()        
            
    def _AddFileIntro( self, pathAndName, pathList, fileName ):
        if pathAndName in self.itemNameToItemDict.keys():
            return
        accumulated = ""
        previousItem = self.root
        for dir in pathList:
            accumulated = accumulated + "\\" + dir
            if accumulated in self.itemNameToItemDict.keys():
                previousItem = self.itemNameToItemDict[ accumulated ]
            else:
                newDirItem = LibStandardItem( dir )
                newDirItem.setAccessibleText( accumulated )
                newDirItem.setAccessibleDescription( "dir" )
                #previousItem.appendRow( newDirItem )
                previousItem.setChild( newDirItem )
                self.itemNameToItemDict[ accumulated ] = newDirItem
                previousItem = newDirItem
                
                                
        currentItem = LibStandardItem( fileName )
        currentItem.setAccessibleText( pathAndName )
        #currentItem.setFlags( Qt.ItemIsUserCheckable | Qt.ItemIsEnabled |
        #Qt.ItemIsSelectable )
        #currentItem.setData( QVariant( Qt.Unchecked ), Qt.CheckStateRole )
        
        #previousItem.appendRow( currentItem )
        previousItem.setChild( currentItem )
        self.itemNameToItemDict[ pathAndName ] = currentItem
        #self.itemNameList.append( pathAndName )
        self.numberOfDocs += 1
        self.numberOfTagedDocs += 1
        curPath = os.path.dirname( pathAndName )
        self.filteredModel.appendRow( [ LibStandardItem( fileName ), LibStandardItem( curPath ) ] )
    
    def ParseDirPath( self, dirPath ):
        currentDriveAndPath = os.path.splitdrive( dirPath )
        currentDrive = currentDriveAndPath[ 0 ]
        curPath = currentDriveAndPath[ 1 ]
        folders = []
        while 1:
            curPath, folder = os.path.split( curPath )
            if folder != "":
                folders.append( folder )
            else:
                if curPath != "" and curPath != "\\":
                    folders.append( curPath )
                break
        folders.reverse()
        folders.insert( 0, currentDrive )
        return folders
          
    def UpdateFilteredModel( self, itemNameList ):
        self.filteredModel.clear()
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file" ] )
        if itemNameList == None:
            self.controller.RefreshFilteredView()
            return
        
        if itemNameList == {}:
            self.numberOfTagedDocs = 0
            #for itemName in self.itemNameList:
            klist = list( self.itemNameToItemDict.keys() ) 
            klist.sort() 
            for itemName in klist:
                if self.itemNameToItemDict[ itemName ].accessibleDescription() != "dir":
                    curPath = os.path.dirname( itemName )
                    curName = os.path.basename( itemName )
                    self.filteredModel.appendRow( [ LibStandardItem( curName ), LibStandardItem( curPath ) ] )
                    self.numberOfTagedDocs += 1
        else:
            itemList = list( itemNameList )
            itemList.sort()
            self.numberOfTagedDocs = len( itemList )
            for itemName in itemNameList:
                curPath = os.path.dirname( itemName )
                curName = os.path.basename( itemName )
                self.filteredModel.appendRow( [ LibStandardItem( curName ), LibStandardItem( curPath ) ] )
        self.controller.RefreshFilteredView()

    def DelItems( self, indexes ):
        for index in indexes:
            itemToDelete = self.library.itemFromIndex( index )
            #previousItem = self.itemNameToItemDict[
            #itemToDelete.accessibleText() ][ 1 ]
            previousItem = itemToDelete.parent()
            del self.itemNameToItemDict[ itemToDelete.accessibleText() ]
            #self.itemNameList.remove( itemToDelete.text() )
            previousItem.removeRow( itemToDelete.row() )
            self.numberOfDocs -= 1
            self.UpdateFilteredModel( {} )

    def CloseLibrary(self):
        self.library.clear()
        self.filteredModel.clear()
        self.library = QStandardItemModel( 0,1 )
        self.library.setHeaderData( 0, QtCore.Qt.Horizontal, QtCore.QVariant( "TreeView of Library:" ) )
        self.itemNameToItemDict = {}
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file" ] )
        self.root = None
        self.controller.RefreshFilteredView()
        numberOfDocs = 0
        numberOfTagedDocs = 0




            

