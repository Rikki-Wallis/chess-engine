from pieces.piece import Piece
from constants import WHITE_KING, BLACK_KING

from pieces.rook import Rook

class King(Piece):
    def __init__(self, colour, name):
        """
        Init method for King class
        
        params:
            colour (char) - The colour of the piece
            name (string) - The name of the piece
        """
        Piece.__init__(self, colour, name)
        self.moved = False
        self.value = None
        self.type = WHITE_KING if colour == 'w' else BLACK_KING
        self.king = self

    def getMoves(self, board):
        """
        Method which finds all the available moves that the king can make in a given position.
        
        params:
            board (List[List[Tile]]) - The current board that the moves are being found on.
        
        returns:
            moves (List[tuple(int, int)]) - A list of moves where each tuple is a (row, col) of each square
                                            the piece can move to
        """
        # Getting the king moves
        unfilteredMoves = self.getOnlyMoves(board)
            
        # Castling logic
        if not self.moved:
            # Getting pieces position
            row, col = self.position
            
            # King-side castling
            if self.kingSideCastling(board, row, col):
                unfilteredMoves.append((row, col+2))
                
            # Queen-side castling
            if self.queenSideCastling(board, row, col):
                unfilteredMoves.append((row, col-2))
                
        # Removing moves that put the king in check
        moves = []
        for coord in unfilteredMoves:
            
            # Simulate the move
            originalTile = board[self.position[0],self.position[1]]
            destinationTile = board[coord[0], coord[1]]
        
            # Temporarily move the piece
            originalTilePiece = originalTile.removePiece()
            destinationTilePiece = destinationTile.removePiece()
            destinationTile.addPiece(originalTilePiece)
            
            # If the king is not in check add it to the valid moves
            if not self.isUnderAttack(coord, board):
                moves.append(coord)
            
            # Resetting the tiles
            originalTile.addPiece(originalTilePiece)
            destinationTile.addPiece(destinationTilePiece)
            
        return moves   
    
    def getOnlyMoves(self, board):
        # Creating a list to store the available moves for the piece
        moves = []
        
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
            tile = board[row][col]
            
            # If the tile is empty add it to legal moves
            if tile.isEmpty():
                moves.append((row,col))
            # If the tile contains the same piece, pass
            elif tile.getPiece() == self:
                continue
            # If the tile contains the same coloured piece, break
            elif tile.getPiece().colour == self.colour:
                continue
            # If the tile contains a king of the opposite colour, set check and break
            elif "King" in tile.getPiece().name:
                moves.append((row,col))
                tile.setCastle()
                continue
            # Otherwise it must be the opponents piece
            else:
                moves.append((row,col))
                continue

        return moves
    
    def kingSideCastling(self, board, row, col):
        return  (isinstance(board[row][col+3].getPiece(),Rook) and not board[row][col+3].getPiece().moved
                and board[row][col+1].isEmpty() and board[row][col+2].isEmpty() and not self.isUnderAttack((row, col), board)
                and not self.isUnderAttack((row, col+1), board) and not self.isUnderAttack((row, col+2), board))
        
    def queenSideCastling(self, board, row, col):
        return (isinstance(board[row][col-4].getPiece(),Rook) and not board[row][col-4].getPiece().moved
                and board[row][col-1].isEmpty() and board[row][col-2].isEmpty() and board[row][col-3].isEmpty() 
                and not self.isUnderAttack((row, col), board) and not self.isUnderAttack((row, col-1), board) and not self.isUnderAttack((row, col-2), board))