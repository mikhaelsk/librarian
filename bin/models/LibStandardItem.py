from PyQt5.QtGui import QStandardItem

class LibStandardItem( QStandardItem ):
    """item base class for library"""
    def __init__( self, str ):
        super().__init__( str )
        self.tagList = []
        self.childCount = 0
        #self.childLis

    def setChild( self, newItem ):
        #TODO realize appending rows and child count
        super().setChild( self.childCount, newItem )
        self.childCount += 1

    def GetChilds( self ):
        cnt = self.childCount - 1
        childList = []
        while cnt >= 0:
            if self.child(cnt) != None:
                childList.append( self.child( cnt ) )
            cnt -= 1
        return childList
'''
    def DelChild( self, childToDelete ):
        if childToDelete in self.GetChilds():
            count = 0
            for child in self.GetChilds():
                if child.text() == childToDelete.text():
                    self.removeRow( childToDelete.row() )
                    break
                count += 1
'''




