from constants import WHITE_ROOK, BLACK_ROOK
from piece import Piece
import copy

"""
Class which defines the behaviour for the rook piece
"""
class Rook(Piece):
    
    def __init__(self, colour, name):
        """
        Init method for Rook class
        
        params:
            colour (char) - The colour of the piece
            name (string) - The name of the piece
        """
        Piece.__init__(self, colour, name)
        self.moved = False
        self.value = 5
        self.type = WHITE_ROOK if colour == 'w' else BLACK_ROOK

    def getMoves(self, board):
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
        # Copying the board so that permutations dont effect the board variable
        moves = copy.deepcopy(board)
        
        # Getting the current row and column
        currentRow = moves[self.position[0]]
        currentCollumn = [row[self.position[1]] for row in moves]

        # Splitting directions
        leftRow = currentRow[:self.position[1]][::-1]  # Reverse for left direction
        rightRow = currentRow[self.position[1] + 1:]   # Tiles to the right
        upCollumn = currentCollumn[:self.position[0]][::-1]  # Reverse for upward direction
        downCollumn = currentCollumn[self.position[0] + 1:]  # Tiles downward
        
        # Adding all directions to a list so that it can be iterated over
        directions = [leftRow, rightRow, upCollumn, downCollumn]
        
        # Iterating over all directions
        for direction in directions:
            
            # Iterating over the indices in the direction
            for tile in direction:
                
                # If the current tile is at the position of the current piece
                if tile.indexCoordinate == self.position:
                    pass
                
                # If the tile contains the current piece, pass
                elif tile.isEmpty():
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
                    break
                
                # If the tile contains an enemy piece set as takable
                elif tile.getPiece().colour != self.colour:
                    tile.setTakeable()
                    break 
        
        # Returning the moves board
        return moves