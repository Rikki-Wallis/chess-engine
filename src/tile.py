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
        self.movable = False
        self.check = False
        self.takeable = False
    
    """
    A method that returns true if the tile is empty and false if it contains a piece.
    
    return:
        empty (bool) - True or False whether the tile is empty
    """
    def isEmpty(self):
        return True if self.contains == None else False
    
    """
    A method that gets the piece on the current tile and returns it.
    
    return:
        piece (Piece) | None - If the tile is not empty returns the current piece, 
                               otherwise returns none
    """
    def getPiece(self):
        # Returning piece on the tile
        return self.contains
    
    """
    A method which adds a piece to the tile.
    
    params:
        piece (Piece) - The piece we want to add to the tile
    """
    def addPiece(self, piece):
        # Adding piece to tile
        self.contains = piece
        # Changing the location of the piece
        piece.position = self.indexCoordinate
    
    """
    A method which removes the current piece on the tile and returns it.
    
    return:
        piece (Piece) - The current piece on the tile
    """
    def removePiece(self):
        # Getting piece that is on the square
        piece = self.contains
        
        # Removing piece from self.contains
        self.contains = None
        
        # Returning piece that was on the square
        return piece
    
    """
    A method used for allowing the tile to be used for piece moves. This method is only
    used on temporary variables and never the original board itself.
    """
    def setMovable(self):
        self.movable = True
        
    """
    A method used for allowing the tile to be used for piece moves. This method is only
    used on temporary variables and never the original board itself.
    """
    def setCheck(self):
        self.check = True

    """
    A method used for allowing the tile to be used for piece moves. This method is only
    used on temporary variables and never the original board itself.
    """
    def setTakeable(self):
        self.takeable = True
        
    def isValid(self):
        if self.takeable or self.check or self.movable:
            return True
    
        return False
        
        
    