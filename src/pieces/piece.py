# Imports
from abc import ABC, abstractmethod

"""
Abstract class which represents the pieces in chess
"""
class Piece(ABC):
    
    def __init__(self, colour, name):
        """
        Init method which defines piece attributes
        params:
            colour (char) - The colour of the piece (b/w)
            name (string) - The name of the piece
        """
        self.colour = colour
        self.name = name
        self.position = None
        self.type = None
    
    @abstractmethod
    def getMoves(self, board):
        """
        Abstract method which when implemented will return
        what moves the piece can make.
        params:
            board (List[List]) - The board on which the game is being played on
        returns:
            returns an array of all the available tiles the piece can move too
        """
        pass
    
    
    def removeIllegalMoves(self, board, unfilteredMoves, sameColourKing):
        moves = []
        # Iterating over each move
        for coord in unfilteredMoves:
            # Simulate the move
            originalTile = board[self.position[0],self.position[1]]
            destinationTile = board[coord[0], coord[1]]
        
            # Temporarily move the piece
            originalTilePiece = originalTile.removePiece()
            destinationTilePiece = destinationTile.removePiece()
            destinationTile.addPiece(originalTilePiece)
            
            # If the king is not in check add it to the valid moves
            if not self.isUnderAttack((sameColourKing.position[0], sameColourKing.position[1]), board):
                moves.append(coord)
            
            # Resetting the tiles
            originalTile.addPiece(originalTilePiece)
            destinationTile.addPiece(destinationTilePiece)
            
        return moves

    def isUnderAttack(self, position, board):
        # Iterating over each row in the board
        for row in board:
            # Iterating over each tile in the board
            for tile in row:
                # If the tile contains a piece of the opposite colour
                if not tile.isEmpty() and tile.getPiece().colour != self.colour:
                    
                    # If the king is the piece only check where it can move to without checking checks
                    if "King" in tile.getPiece().name:
                        legalMoves = tile.getPiece().getOnlyMoves(board)
                        
                    # Otherwise, treat it as any other piece
                    else:
                        # Getting the legal moves for the opponent
                        legalMoves = tile.getPiece().getMoves(board)
                        
                    if position in legalMoves:
                        return True
                    
        return False