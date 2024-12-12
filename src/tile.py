"""
Class which defines the behaviour of the tiles that exist on the game board
"""
class Tile():
    
    def __init__(self, notation, indexCoordinate):
        """
        Init method for the tile class.
        
        params:
            notation (string) - The notation of the tile e.g. "a1"
            indexCoordinate (tuple(int, int)) - The index of the tile
        """
        self.notation = notation
        self.indexCoordinate = indexCoordinate
        self.contains = None
        self.movable = False
        self.check = False
        self.takeable = False
        self.castle = False
    
    def isEmpty(self):
        """
        A method that returns true if the tile is empty and false if it contains a piece.
        
        return:
            empty (bool) - True or False whether the tile is empty
        """
        # return True if self.contains == None else False
        return self.contains is None
        
    def getPiece(self):
        """
        A method that gets the piece on the current tile and returns it.
        
        return:
            piece (Piece) | None - If the tile is not empty returns the current piece, 
                                otherwise returns none
        """
        # Returning piece on the tile
        return self.contains
    
    def addPiece(self, piece):
        """
        A method which adds a piece to the tile.
        
        params:
            piece (Piece) - The piece we want to add to the tile
        """
        # Adding piece to tile
        self.contains = piece
        if piece != None:
            # Changing the location of the piece
            piece.position = self.indexCoordinate
    
    def removePiece(self):
        """
        A method which removes the current piece on the tile and returns it.
        
        return:
            piece (Piece) - The current piece on the tile
        """
        # Getting piece that is on the square
        piece = self.contains
        
        # Removing piece from self.contains
        self.contains = None
        
        # Returning piece that was on the square
        return piece
    
    def setMovable(self):
        """
        A method used for allowing the tile to be used for piece moves. This method is only
        used on temporary variables and never the original board itself.
        """
        self.movable = True
        
    def setCheck(self):
        """
        A method used for allowing the tile to be used for piece moves. This method is only
        used on temporary variables and never the original board itself.
        """
        self.check = True

    def setTakeable(self):
        """
        A method used for allowing the tile to be used for piece moves. This method is only
        used on temporary variables and never the original board itself.
        """
        self.takeable = True
        
    def setCastle(self):
        self.castle = True
        
    def isValid(self):
        """
        A method used to check if a tile is contained in a legal move
        
        return:
            bool - True or False whether the tile is contained in a legal move
        """
        if self.takeable or self.check or self.movable:
            return True
        else:
            return False
        
        