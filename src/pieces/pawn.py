from src.pieces.piece import Piece
from constants import WHITE_KING, BLACK_KING
import copy

class Pawn(Piece):
    def __init__(self, colour, name):
        """
        Init method for Bishop class
        
        params:
            colour (char) - The colour of the piece
            name (string) - The name of the piece
        """
        Piece.__init__(self, colour, name)
        self.moved = False
        self.value = None
        self.type = WHITE_KING if colour == 'w' else BLACK_KING

    def getMoves(self, board):
        """
        Method which finds all the available moves that the rook can make in a given position.
        Declared as a static method so that the king can use this method to incorporate its
        own movements.
        
        params:
            board (List[List[Tile]]) - The current board that the moves are being found on.
        
        returns:
            moves (List[List[Tile]]) - An updated deep copy of the board which has the tiles set to where the
                                       king can move to.
        """
        # Copying the board so that permutations dont effect the board variable
        moves = copy.deepcopy(board)
        
        # Getting the legnth of the rows and collumns
        rows = len(board)
        cols = len(board[0])
        
        # Defining the directions the bishop can move
        directions = [(-1,-1), (-1,1), (1,-1), (1,1), (1,0), (-1,0), (0,1), (0,-1)]
        
        # Iteration over all diagonal directions
        for rowDirection, collumnDirection in directions:
            
            # Obtaining the current position of the bishop
            row, col = self.position
        
            # Move to the next tile in the current position
            row += rowDirection
            col += collumnDirection
            
            # Out of bounds check
            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue
            
            # Obtaining tile at current position
            tile = moves[row][col]
            
            # If the tile is empty add it to legal moves
            if tile.isEmpty():
                tile.setMovable()
            # If the tile contains the same piece, pass
            elif tile.getPiece() == self:
                continue
            # If the tile contains the same coloured piece, break
            elif tile.getPiece().colour == self.colour:
                continue
            # If the tile contains a king of the opposite colour, set check and break
            elif "King" in tile.getPiece().name:
                tile.setCheck()
                continue
            # Otherwise it must be the opponents piece
            else:
                tile.setTakeable()
                continue
    
        return moves   