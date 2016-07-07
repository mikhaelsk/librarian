#from .Library import *
from ..Controller import *
import os.path
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainModel():
    """files and folders model"""
    nodeId = 0
    def __init__( self, myController ):
        #super().__init__(0,1,self)
        self.nodeId = 0
        self.controller = myController
        libName = "MyLibrary"
        self.library = QStandardItemModel(0,1)
        self.library.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QVariant("TreeView of Library"))
        self.root = QStandardItem( libName )
        self.controller.PrintToLog( "Library initialized: " + libName )
        self.nodeId+=1
        self.library.appendRow(self.root)
        
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

    def SaveLibrary( self ):
        pass
        #TODO
            
    def _AddFileIntro( self, path, name ):
        #self.root.AddChild( Node( path + '\\' + name ) )
        self.root.appendRow( QStandardItem(path + '\\' + name )) 
        self.nodeId+=1
        
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