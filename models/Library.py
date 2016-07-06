class Library():
    """description of class"""
    def __init__(self, libName):
        self.root = Node(libName)
        
class Node():
    def __init__(self, nameTxt):      
        self.name = nameTxt
        