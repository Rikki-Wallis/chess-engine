"""
Class which defines the behaviour of the tiles that exist on the game board
"""
class Tile():
    
    """
    Init method for the tile class.
    
    params:
        notation (string) - The notation of the tile e.g. "a1"
        indexCoordinate (tuple(int, int)) - The index of the tile
    """
    def __init__(self, notation, indexCoordinate):
        self.notation = notation
        self.indexCoordinate = indexCoordinate
        self.contains = None
        
    def isEmpty(self):
        # Returns true if the tile is empty, else returns false
        return True if self.contains == None else False
    
    def getPiece(self):
        # Returning piece on the tile
        return self.contains
    
    def addPiece(self, piece):
        # Adding piece to tile
        self.contains = piece
        
    def removePiece(self):
        # Getting piece that is on the square
        piece = self.contains
        
        # Removing piece from self.contains
        self.contains = None
        
        # Returning piece that was on the square
        return piece
    
    def setMovable(self):
        self.movable = True
        
    def setCheck(self):
        self.check = True
        
    def setTakable(self):
        self.takable = True
        
        
    