from PyQt5.QtGui import QStandardItemModel, QStandardItem 
from PyQt5.QtWidgets import QMessageBox, QCheckBox
from PyQt5.QtCore import * 
from PyQt5.QtXml import * 
import os.path
import sys

class Tags():
    """class for working with tags model:
        - adding tags
        - deletening tags
        - loading tags DB
        - saving tags DB
    """
    
    def __init__( self, myController ):
        self.controller = myController
        self.wereAnyChanges = False
        self.tagDict = {}
        self.tagModel = QStandardItemModel( 0,1 )
        self.tagModel.setHeaderData( 0, Qt.Horizontal, QVariant( "TagList for Library:" ) )
        #self.tagModel.itemChanged.connect( self.HandleTagChanged )
        self.InitDefaultTags()
        if os.path.exists( "myTags.xml" ) == False:
            self.controller.PrintToLog( "No Tag library found, created new one" )
        else:
            self.LoadTagsFromXML()
    
    def InitDefaultTags( self ):
        pass
        #self.AddTag( "IMPORTANT" )

    def AddTag( self, name ):
        newTag = QStandardItem( name )
        newTag.setFlags( Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable )
        newTag.setData( QVariant( Qt.Unchecked ), Qt.CheckStateRole )
        self.tagDict[ name ] = newTag
        self.tagModel.appendRow( newTag )
        self.tagModel.sort( Qt.AscendingOrder )
        self.wereAnyChanges = True

    #def HandleTagChanged( self, item ):
    #    if not item.checkState():
    #        return
    #    else:
    #        item.

    def LoadTagsFromXML( self ):
        xmlParser = QXmlSimpleReader()
        xmlContentHandler = myXmlContentHandler( self )
        xmlFile = QFile( "myTags.xml" )
        xmlInputSource = QXmlInputSource( xmlFile )    
        xmlParser.setContentHandler( xmlContentHandler )  
      
        if( xmlParser.parse( xmlInputSource ) ):
            self.controller.PrintToLog( "Tag-library successfully loaded!" )
        else:  
            self.controller.PrintToLog( "Parsing of Tag-library Failed!" )

    def SaveTagModel( self ):
        if self.wereAnyChanges == False:
            return
        QFile.remove( "myTags_bcp.xml" )
        xmlOldFile = QFile( "myTags.xml" )        
        xmlOldFile.rename( "myTags_bcp.xml" )

        xmlWriter = QXmlStreamWriter()
        xmlFile = QFile( "myTags.xml" )
        
        if ( xmlFile.open( QIODevice.WriteOnly ) == False ):    
            QMessageBox.warning( 0, "Error!", "Error opening file" )  
            QFile.remove( "myTags.xml" )
            xmlOldFile.rename( "myTags.xml" )  
        else :    
            xmlWriter.setDevice( xmlFile )	
            xmlWriter.writeStartDocument()
            xmlWriter.writeStartElement( "TagLibrary" )
            
            #lambdaFunc = lambda x: x[ 1 ]
            #self.tagDict = sorted( self.tagDict.keys(), key=lambdaFunc,
            #reverse=False )
            klist =  list( self.tagDict.keys() )
            klist.sort() 
            for tagName in klist:
                xmlWriter.writeStartElement( tagName )
                xmlWriter.writeEndElement() 
                xmlWriter.autoFormattingIndent()
            xmlWriter.writeEndElement()
            xmlWriter.writeEndDocument()
        self.controller.PrintToLog( "TagLibrary successfully saved!" )
        #if everything was written successfully, replace a tag file with new
        #one
        #QFile.remove( "myTags.xml" )
        #xmlFile.rename( "myTags.xml" )

    def DelTag( self, selectedIndexes ):
        for index in selectedIndexes:
            selectedItem = self.tagModel.itemFromIndex( index )
            del self.tagDict[ selectedItem.text() ]
            self.tagModel.removeRow( selectedItem.row() )
            

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
        #    self.controller.PrintToLog( atts.type( num ) + "=" + atts.value(
        #    num ) + "\n" )
        #    self.controller.PrintToLog(
        #    "#####################################\n\n" )
        return True


