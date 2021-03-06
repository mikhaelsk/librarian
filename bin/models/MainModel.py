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
    
    def __init__( self, myController ):
        self.nodeId = 0
        self.controller = myController
        '''
        setup complete library model for treeView
        '''
        #libName = "MyLibrary"
        self.library = QStandardItemModel( 0,1 )
        self.library.setHeaderData( 0, QtCore.Qt.Horizontal, QtCore.QVariant( "TreeView of Library:" ) )
        self.numberOfDocs = 0
        self.numberOfTagedDocs = 0
        #self.root = QStandardItem( libName )
        #self.controller.PrintToLog( "Library initialized: " + libName )
        #self.library.appendRow( self.root )
        self.itemNameToItemDict = {}
        
        #self.itemNameList = []
        
        '''
        now setup the filtered model for tableView
        '''
        self.filteredModel = QStandardItemModel( 0,1 )
        self.filteredModel.setColumnCount( 3 )
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file", "tags" ] )
    
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
        newElement = self._AddFileIntro( pathAndName, pathList, curName )
        self.controller.PrintToLog( "Found File: " + pathAndName )
        self.controller.UpdateLibraryView()
        return newElement        
            
    def _AddFileIntro( self, pathAndName, pathList, fileName ):
        if pathAndName in self.itemNameToItemDict.keys():
            return
        accumulated = ""
        previousItem = self.root
        for dir in pathList:
            accumulated = accumulated + "\\" + dir
            if accumulated in self.itemNameToItemDict.keys():
                previousItem = self.itemNameToItemDict[ accumulated ][ 0 ]
            else:
                newDirItem = LibStandardItem( dir )
                newDirItem.setAccessibleText( accumulated )
                newDirItem.setAccessibleDescription( "dir" )
                #previousItem.appendRow( newDirItem )
                previousItem.setChild( newDirItem )
                self.itemNameToItemDict[ accumulated ] = [ newDirItem, None ]
                previousItem = newDirItem
                
                                
        currentItem = LibStandardItem( fileName )
        currentItem.setAccessibleText( pathAndName )
        #currentItem.setFlags( Qt.ItemIsUserCheckable | Qt.ItemIsEnabled |
        #Qt.ItemIsSelectable )
        #currentItem.setData( QVariant( Qt.Unchecked ), Qt.CheckStateRole )
        
        #previousItem.appendRow( currentItem )
        previousItem.setChild( currentItem )
        previousItem.sortChildren( 0 )
        currentItemTags = LibStandardItem( str( currentItem.tagList ) )
        self.itemNameToItemDict[ pathAndName ] = [ currentItem, currentItemTags ]
        #self.itemNameList.append( pathAndName )
        self.numberOfDocs += 1
        self.numberOfTagedDocs += 1
        curPath = os.path.dirname( pathAndName )
        self.filteredModel.appendRow( [ LibStandardItem( fileName ), LibStandardItem( curPath ), currentItemTags ] )
        return currentItem
    
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
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file", "tags" ] )
        if itemNameList == None:
            self.controller.RefreshFilteredView()
            return
        
        if itemNameList == {}:
            self.numberOfTagedDocs = 0
            #for itemName in self.itemNameList:
            klist = list( self.itemNameToItemDict.keys() ) 
            klist.sort() 
            for itemName in klist:
                if self.itemNameToItemDict[ itemName ][ 0 ].accessibleDescription() != "dir":
                    curPath = os.path.dirname( itemName )
                    curName = os.path.basename( itemName )
                    self.filteredModel.appendRow( [ LibStandardItem( curName ), LibStandardItem( curPath ), LibStandardItem( str( self.itemNameToItemDict[ itemName ][ 0 ].tagList ) ) ] )
                    self.numberOfTagedDocs += 1
        else:
            itemList = list( itemNameList )
            itemList.sort()
            self.numberOfTagedDocs = len( itemList )
            for itemName in itemNameList:
                curPath = os.path.dirname( itemName )
                curName = os.path.basename( itemName )
                self.filteredModel.appendRow( [ LibStandardItem( curName ), LibStandardItem( curPath ), LibStandardItem( str( self.itemNameToItemDict[ itemName ][ 0 ].tagList ) ) ] )
        self.controller.RefreshFilteredView()

    def DelItems( self, itemsToDelete ):
        for itemToDelete in itemsToDelete:
            if itemToDelete.accessibleDescription() != "dir":
                self.numberOfDocs -= 1
            previousItem = itemToDelete.parent()
            del self.itemNameToItemDict[ itemToDelete.accessibleText() ]
            #previousItem.DelChild( itemToDelete )
            previousItem.removeRow( itemToDelete.row() )
            #self.itemNameList.remove( itemToDelete.text() )
            #itemToDelete.removeRow( itemToDelete.row() )
            
        self.UpdateFilteredModel( {} )    

    def CloseLibrary( self ):
        self.library.clear()
        self.filteredModel.clear()
        self.library = QStandardItemModel( 0,1 )
        self.library.setHeaderData( 0, QtCore.Qt.Horizontal, QtCore.QVariant( "TreeView of Library:" ) )
        self.itemNameToItemDict = {}
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file", "tags" ] )
        self.root = None
        self.numberOfDocs = 0
        self.numberOfTagedDocs = 0
        self.controller.RefreshFilteredView()





            

