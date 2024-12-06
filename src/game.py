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
            self.selectedPieceLegalMoves = self.selectedPiece.getMoves(self.gameBoard.board)
            
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
            if self.selectedPieceLegalMoves[destinationTileIndex[0], destinationTileIndex[1]].isValid():
                # Remove the piece from the current tile and add it to the new tile
                piece = self.selectedTile.removePiece()
                destinationTile.addPiece(piece)
                
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
                
                    
                    
            
        