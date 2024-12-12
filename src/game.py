import pygame
from constants import *

"""
A class responsible for handling any event that may occur within the game
"""
class Game():
    
    def __init__(self, gameBoard, gui, cursor):
        """
        The game classes init method.
        
        params:
            gameBoard (Board) - The current board which the game will be on
            gui (GUI) - The current gui handling all the graphical aspects of the game
            cursor (Cursor) - The current cursor class which handles all mouse related things
        """
        # Variables which exist to add extra functionality through their own objects
        self.gameBoard = gameBoard
        self.gui = gui
        self.cursor = cursor
        
        # Variables which provide information on the current move
        self.selectedPiece = None
        self.selectedTile = None
        self.selectedPieceLegalMoves = None
        self.hasMoveBeenMade = False
        
    def selectPiece(self, currentColour):
        """
        A method which defines what happens when a user selects a piece. Draws legal moves to the screen
        and updates init variables to reflect the selection
        
        params:
            currentColour (char) - The current colour of who's turn it is
        """
        # Getting the current tile where the mouse is
        currentTileIndex = self.cursor.mousePositionToTile()
        currentTile = self.gameBoard.board[currentTileIndex[0], currentTileIndex[1]]
        
        # If the tile is not empty and contains a piece of the same colour of whos turn it is handle the event
        if not currentTile.isEmpty() and currentTile.getPiece().colour == currentColour:

            # Obtaining the piece on the current tile
            self.selectedPiece = currentTile.getPiece()
            self.selectedTile = currentTile
            
            # Obtaining the legal moves
            legalMoves = self.selectedPiece.getMoves(self.gameBoard.board)
            self.selectedPieceLegalMoves = self.selectedPiece.removeIllegalMoves(self.gameBoard.board, legalMoves, self.selectedPiece.king)
            
            # Drawing the moves to the screen
            self.gui.drawBoard()
            self.gui.drawPieces(self.gameBoard.board)
            self.gui.drawLegalMoves(self.selectedPieceLegalMoves)
        
    def handleClick(self, currentColour):
        """
        A method which handles a click down event. Depending on what the user clicks the outcome will be different.
        
        params:
            currentColour (char) - The current colour of who's turn it is
        """
        # If no piece has been selected yet, we should select the piece
        if self.selectedPiece == None:
            
            # Selecting the piece
            self.selectPiece(currentColour)
            
        # If a piece has been selected already we will need to find the destination that the piece should travel
        else:
            # Getting the current tile where the mouse is
            destinationTileIndex = self.cursor.mousePositionToTile()
            destinationTile = self.gameBoard.board[destinationTileIndex[0], destinationTileIndex[1]]
            
            # Seeing if the destination tile may be movable
            if destinationTileIndex in self.selectedPieceLegalMoves:
                # Remove the piece from the current tile and add it to the new tile
                piece = self.selectedTile.removePiece()
                destinationTile.addPiece(piece)
                
                # Updating whether the piece has moved
                piece.moved = True
                
                # Resetting current move
                self.selectedPiece = None
                self.selectedTile = None
                self.hasMoveBeenMade = True
                
                # Redrawing board
                self.gui.drawBoard()
                self.gui.drawPieces(self.gameBoard.board)
                
                # Refreshing screen
                pygame.display.update()
                
            elif destinationTile.castle:
                # Remove the piece from the current tile and add it to the new tile
                piece = self.selectedTile.removePiece()
                destinationTile.addPiece(piece)
                
                # Removing and placing the rook next to the king
                if destinationTileIndex[1] > 3:
                    rook = self.gameBoard.board[self.selectedPiece.position[0], 7].removePiece()
                    self.gameBoard.board[self.selectedPiece.position[0], 5].addPiece(rook)
                else:
                    rook = self.gameBoard.board[self.selectedPiece.position[0], 0].removePiece()
                    self.gameBoard.board[self.selectedPiece.position[0], 3].addPiece(rook)
                    
                # Updating whether the piece has moved
                piece.moved = True
                rook.moved = True
                
                # Resetting current move
                self.selectedPiece = None
                self.selectedTile = None
                self.hasMoveBeenMade = True
                
                # Redrawing board
                self.gui.drawBoard()
                self.gui.drawPieces(self.gameBoard.board)
                
                # Refreshing screen
                pygame.display.update()
            
            elif not destinationTile.isEmpty() and destinationTile.getPiece().colour == currentColour:
                self.selectPiece(currentColour)
            
            # Otherwise an invalid tile has been pressed and we should reset the self vars
            else:
                self.selectedPiece = None
                self.selectedPieceLegalMoves = None
                
                # Redrawing board and pieces
                self.gui.drawBoard()
                self.gui.drawPieces(self.gameBoard.board)
                
    def isKingInCheck(self, colour):
        # Getting the king piece
        king = self.gameBoard.getKing(colour)
        
        # Returning whether or not the king is in check
        return king.isUnderAttack(king.position, self.gameBoard.board)
    
    def isKingInCheckMate(self, colour):
        # If the king is not in check return false
        if not self.isKingInCheck(colour):
            return False
        
        # Otherwise the king is in check and we should check if the king can move anywhere
        if not len(self.gameBoard.getKing(colour).getMoves(self.gameBoard.board)) == 0:
            return False
        
        # If the king cant move anywhere we should check if a piece can block
        for piece in self.gameBoard.piecesDictionary[colour]:
            
            # Getting the pieces unfiltered moves
            unfilteredMoves = piece.getMoves(self.gameBoard.board)
            
            # Iterating over each move the piece can make to see if it can stop the check
            for move in piece.removeIllegalMoves(self.gameBoard.board, unfilteredMoves, piece.king):
                
                # Simulate the move
                originalTile = self.gameBoard.board[piece.position[0],piece.position[1]]
                destinationTile = self.gameBoard.board[move[0], move[1]]
            
                # Temporarily move the piece
                originalTilePiece = originalTile.removePiece()
                destinationTilePiece = destinationTile.removePiece()
                destinationTile.addPiece(originalTilePiece)
                
                # If there is no longer a check return false
                if not self.isKingInCheck(colour):
                    originalTile.addPiece(originalTilePiece)
                    destinationTile.addPiece(destinationTilePiece)
                    return False
                
                originalTile.addPiece(originalTilePiece)
                destinationTile.addPiece(destinationTilePiece)
                
        return True
                    