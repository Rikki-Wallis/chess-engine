from piece import Piece
import copy

"""
Class which defines the behaviour for the rook piece
"""
class Rook(Piece):
    
    """
    Init method for Rook class
    
    params:
        colour (char) - The colour of the piece
        name (string) - The name of the piece
    """
    def __init__(self, colour, name):
        Piece.__init__(colour, name)
        self.moved = False
        self.value = 5

    """
    Method which finds all the available moves that the rook can make in a given position.
    Declared as a static method so that the queen can use this method to incorporate its
    own movements.
    
    params:
        board (List[List[Tile]]) - The current board that the moves are being found on.
    
    returns:
        moves (List[List[Tile]]) - An updated deep copy of the board which has the tiles set to where the
                                   rook can move to.
    """
    @staticmethod
    def getMoves(self, board):
        # Copying the board so that permutations dont effect the board variable
        moves = copy.deepcopy(board)

        # Slicing the row and collumn of the rook
        currentRow = moves[self.position[0], :]
        currentCollumn = moves[:, self.position[1]]
        
        # Converting current row to positive and negative directions
        leftRow = currentRow[self.position[0]:]
        rightRow = currentRow[:self.position[0]]
        
        # Converting current collumn to positive and negative directions
        upCollumn = currentCollumn[:self.position[1]]
        downCollumn = currentCollumn[self.position[1]:]
        
        # Flipping leftRow and upCollumn
        leftRow[::-1]
        upCollumn[::-1]
        
        # Adding all directions to a list so that it can be iterated over
        directions = [leftRow, rightRow, upCollumn, downCollumn]
        
        # Iterating over all directions
        for direction in directions:
            
            # Iterating over the indices in the direction
            for tile in direction:
                
                # If the tile contains the current piece, pass
                if tile.isEmpty():
                    # Setting tile to be movable
                    tile.setMovable()
                
                # If we are looking at the same piece making the move pass
                elif tile.getPiece() == self:
                    pass
                
                # If the tile contains another piece of the same colour, break out of the loop
                elif tile.getPiece().colour == self.colour:
                    break
                
                # If the tile contains a king
                elif "King" in tile.getPiece().name:
                    tile.setCheck()
                
                # If the tile contains an enemy piece set as takable
                elif tile.getPiece().colour != self.colour:
                    tile.setTakeable()
                    

        # Flipping leftRow and upCollumn to the original
        leftRow[::-1]
        upCollumn[::-1]
        
        # Returning the moves board
        return moves