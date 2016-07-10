#from .Library import *
from ..Controller import *
import os.path
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
#from PyQt5.QtCore import QAbstractTableModel
class MainModel():
    """files and folders model"""
    numberOfDocs = 0
    def __init__( self, myController ):
        #super().__init__(0,1,self)
        self.nodeId = 0
        self.controller = myController

        '''
        setup complete library model for treeView
        '''
        libName = "MyLibrary"
        self.library = QStandardItemModel( 0,1 )
        self.library.setHeaderData( 0, QtCore.Qt.Horizontal, QtCore.QVariant( "TreeView of Library:" ) )
        self.root = QStandardItem( libName )
        self.controller.PrintToLog( "Library initialized: " + libName )
        self.library.appendRow( self.root )
        self.itemDictionary = {}
        '''
        now setup the filtered model for tableView
        '''
        self.filteredModel = QStandardItemModel( 0,1 )
        self.filteredModel.setColumnCount( 2 )
        self.filteredModel.setHorizontalHeaderLabels( [ "Library filtered by tag", "path to file" ] )
        
    def AddFolder( self, folderPath ):
        #self.controller.logger.WriteToLog( "New Folder added: " + path )
        #currrentTree = os.walk( folderPath )
        for ( paths,dirs,files ) in os.walk( folderPath ):
            for file in files:
                self.controller.PrintToLog( "Found File: " + paths + "\\" + file )
                self._AddFileIntro( paths, file )
        self.controller.UpdateLibraryView()
        

    def AddFile( self, name ):
        curPath = os.path.dirname( name )
        curName = os.path.basename( name )
        self._AddFileIntro( curPath, curName )
        self.controller.PrintToLog( "Found File: " + curPath + "\\" + curName )
        self.controller.UpdateLibraryView()

    def SaveLibrary( self ):
        pass
        #TODO
            
    def _AddFileIntro( self, path, name ):
        #self.root.AddChild( Node( path + '\\' + name ) )
        currentItem = QStandardItem( path + '\\' + name ) 
        #currentItem.setFlags( Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable )
        #currentItem.setData( QVariant( Qt.Unchecked ), Qt.CheckStateRole )
        self.root.appendRow( currentItem ) 
        self.numberOfDocs += 1
        #for test:
        self.filteredModel.appendRow( [ QStandardItem( name ), QStandardItem( path ) ] )
        
        #self.itemDictionary.
'''       
class FilteredTableModel( QAbstractTableModel ): 
    def __init__( self, headerdata, parent = None, *args ): 
       
        QAbstractTableModel.__init__( self, parent, *args ) 
        self.arrayData = [ [] ]
        self.headerData = headerdata
 
    def rowCount( self, parent ): 
        return len( self.arrayData ) 
 
    def columnCount( self, parent ): 
        return len( self.arrayData[ 0 ] ) 
 
    def Data( self, index, role ): 
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        return QVariant( self.arrayData[ index.row() ][ index.column() ] ) 

    def HeaderData( self, col, orientation, role ):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant( self.headerData[ col ] )
        return QVariant()
'''

'''
folders = []
os.path.realpath(path)
while 1:
    path, folder = os.path.split(path)

    if folder != "":
        folders.append(folder)
    else:
        if path != "":
            folders.append(path)

        break

folders.reverse()
'''

'''
class Node(QStandardItem):
    def __init__( self, nameTxt ):      
        self.name = nameTxt
        self.children = []
    
    @property
    def Children( self ):
        return self.children

    def AddChild( self, node ):
        self.children.append( node )
'''