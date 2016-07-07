from .Library import *
from ..Controller import *
import os.path

class MainModel():
    """files and folders model"""
    def __init__( self, myController ):
        self.controller = myController
        libName = "MyLibrary"
        self.library = Library( libName )
        self.controller.PrintToLog( "Library initialized: " + libName )
        
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
        self.library.AddNode( path, name )
        
        

