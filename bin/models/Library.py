class Library():
    """description of class"""
    def __init__( self, libName ):
        self.root = Node( libName )

    def AddNode( self, path, name ):
        self.root.AddChild( Node( path + '\\' + name ) )
            
        
class Node():
    def __init__( self, nameTxt ):      
        self.name = nameTxt
        self.children = []
    
    @property
    def Children( self ):
        return self.children

    def AddChild( self, node ):
        self.children.append( node )