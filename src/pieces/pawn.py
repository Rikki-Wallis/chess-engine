from pieces.piece import Piece
from constants import WHITE_PAWN, BLACK_PAWN
import copy

class Pawn(Piece):
    def __init__(self, colour, name, sameColourKing):
        """
        Init method for Bishop class
        
        params:
            colour (char) - The colour of the piece
            name (string) - The name of the piece
        """
        Piece.__init__(self, colour, name)
        self.moved = False
        self.value = 1
        self.type = WHITE_PAWN if colour == 'w' else BLACK_PAWN
        self.king = sameColourKing
        
        self.promotionIndex = 0 if colour == 'w' else 7
        self.startingIndex = 6 if colour == 'w' else 1

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
        # Getting the legnth of the rows and collumns
        rows = len(board)
        cols = len(board[0])
        
        # Defining the directions the bishop can move
        movingDirections = [(-1,0)] if self.colour == 'w' else [(1,0)]
        
        # Adding two square moves to the directions
        if self.position[0] == self.startingIndex:
            # twoSquareMoveDirections = [(2,0)] if self.colour == 'w' else [(-2,0)]
            movingDirections.append((-2,0) if self.colour == 'w' else (2,0))
            
        # Adding takable squares
        takingDirections = [(1,1), (1,-1)] if self.colour == 'b' else [(-1,1), (-1,-1)]
        
        # Creating a list to store the moves
        moves = []
        
        # Iteration over all moving directions
        for rowDirection, collumnDirection in movingDirections:
            
            # Obtaining the current position of the bishop
            row, col = self.position
        
            # Move to the next tile in the current position
            row += rowDirection
            col += collumnDirection
            
            # Out of bounds check
            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue
            
            # Obtaining tile at current position
            tile = board[row][col]
            
            # If the tile is empty add it to legal moves
            if tile.isEmpty():
                moves.append((row, col))
                
        # Checking if the pawn can take a piece
        for rowDirection, collumnDirection in takingDirections:
            # Obtaining the current position of the bishop
            row, col = self.position
        
            # Move to the next tile in the current position
            row += rowDirection
            col += collumnDirection
            
            # Out of bounds check
            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue
            
            # Obtaining tile at current position
            tile = board[row][col]
            
            if tile.isEmpty():
                continue
            elif tile.getPiece().colour != self.colour and not "King" in tile.getPiece().name:
                moves.append((row, col))
    
        return moves   