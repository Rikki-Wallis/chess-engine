from constants import WHITE_BISHOP, BLACK_BISHOP
from pieces.piece import Piece

"""
Class which defines the behaviour for the bishop piece
"""
class Bishop(Piece):
    
    def __init__(self, colour, name, sameColourKing):
        """
        Init method for Bishop class
        
        params:
            colour (char) - The colour of the piece
            name (string) - The name of the piece
        """
        Piece.__init__(self, colour, name)
        self.moved = False
        self.value = 3
        self.type = WHITE_BISHOP if colour == 'w' else BLACK_BISHOP
        self.king = sameColourKing

    def getMoves(self, board):
        """
        Method which finds all the available moves that the bishop can make in a given position.
        Declared as a static method so that the queen can use this method to incorporate its
        own movements.
        
        params:
            board (List[List[Tile]]) - The current board that the moves are being found on.
        
        returns:
            moves (List[tuple(int, int)]) - A list of moves where each tuple is a (row, col) of each square
                                            the piece can move to
        """
        # Creating a list to store the available moves for the piece
        moves = []
        
        # Getting the legnth of the rows and collumns
        rows = len(board)
        cols = len(board[0])
        
        # Defining the directions the bishop can move
        directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
        
        # Iteration over all diagonal directions
        for rowDirection, collumnDirection in directions:
            
            # Obtaining the current position of the bishop
            row, col = self.position
            
            while True:
                # Move to the next tile in the current position
                row += rowDirection
                col += collumnDirection
                
                # Out of bounds check
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    break
                
                # Obtaining tile at current position
                tile = board[row][col]
                
                # If the tile is empty add it to legal moves
                if tile.isEmpty():
                    moves.append((row,col))
                # If the tile contains the same piece, pass
                elif tile.getPiece() == self:
                    pass
                # If the tile contains the same coloured piece, break
                elif tile.getPiece().colour == self.colour:
                    break
                # If the tile contains a king of the opposite colour, set check and break
                elif "King" in tile.getPiece().name:
                    moves.append((row,col))
                    break
                # Otherwise it must be the opponents piece
                else:
                    moves.append((row,col))
                    break
        
        return moves
    
