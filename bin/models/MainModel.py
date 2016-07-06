from .Library import *
from ..Controller import *
class MainModel():
    """files and folders model"""
    def __init__( self, myController ):
        self.controller = myController
        libName = "MyLibrary"
        self.library = Library( libName )
        self.controller.logger.WriteToLog( "Library initialized: " + libName )
        
    def AddFolder( self, path ):
        self.controller.logger.WriteToLog( "New Folder added: " + path )
        


