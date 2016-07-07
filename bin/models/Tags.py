from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import * 
from PyQt5.QtXml import * 
import os.path
import sys

class Tags():
    """description of class"""
    
    def __init__( self, myController ):
        self.controller = myController
        self.tagList = []
        self.tagModel = QStandardItemModel( 0,1 )
        self.tagModel.setHeaderData( 0, Qt.Horizontal, QVariant( "TagList for Library:" ) )
        self.InitDefaultTags()
        if os.path.exists( "myTags.xml" ) == False:
            self.controller.PrintToLog( "No Tag library found, created new one" )
        else:
            self.parseXML()
    
    def InitDefaultTags( self ):
        self.AddTag( "IMPORTANT" )

    def AddTag( self, name ):
        self.tagList.append( name )
        self.tagModel.appendRow( QStandardItem( name ) )

    def parseXML( self ):
        xmlParser = QXmlSimpleReader()
        xmlContentHandler = myXmlContentHandler( self )
        xmlFile = QFile( "myTags.xml" )
        xmlInputSource = QXmlInputSource( xmlFile )    
        xmlParser.setContentHandler( xmlContentHandler )  
      
        if( xmlParser.parse( xmlInputSource ) ):
            self.controller.PrintToLog( "Parsed Tag-library Successfully!" )
        else:  
            self.controller.PrintToLog( "Parsing of Tag-library Failed!" )

class myXmlContentHandler( QXmlDefaultHandler ):    
    def __init__( self, tags ):
        super().__init__()
        self.myTags = tags

    def startElement( self, nameSpaceURI, localName, qName, atts ):
        if localName != "TagLibrary":
            self.myTags.AddTag( localName )
        #print( "Read Start Tag : " + localName + "\n" )
        #print( "Tag Attributes: " )
        #for num in range( 0, atts.length() ):    
        #    self.controller.PrintToLog( atts.type( num ) + "=" + atts.value( num ) + "\n" )
        #    self.controller.PrintToLog( "#####################################\n\n" )
        return True


