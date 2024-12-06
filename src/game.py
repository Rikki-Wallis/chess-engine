import pygame
from board import Board
from gui import GUI
from cursor import Cursor
from tile import Tile
from piece import Piece
from rook import Rook
from constants import *
import copy
import math
from pygame._sdl2 import Window




class Game():
    def __init__(self, gameBoard, gui, cursor):
        # Variables which exist to add extra functionality through their own objects
        self.gameBoard = gameBoard
        self.gui = gui
        self.cursor = cursor
        
        # Variables which provide information on the current move
        self.currentMove = (None, None) # [0] is the selected piece and [1] is the desired location of the piece
        self.currentLegalMoves = None
        self.hasMoveBeenMade = False
        
        self.selectedPiece = None
        self.selectedTile = None
        self.selectedPieceLegalMoves = None
        
    def selectPiece(self, currentColour):
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
            
            elif destinationTile.getPiece().colour == currentColour:
                self.selectPiece(currentColour)
            
            # Otherwise an invalid tile has been pressed and we should reset the self vars
            else:
                self.selectedPiece = None
                self.selectedPieceLegalMoves = None
                
                # Redrawing board and pieces
                self.gui.drawBoard()
                self.gui.drawPieces(self.gameBoard.board)
                
    def playMove(self, event, colour):
        # If the event is a mouse button down we should check if there is a piece there
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # Getting the correct colour pieces so that the program knows which colour we are
            colourBoard = self.gameBoard.getTemporaryColourBoard(colour)
            
            # Getting the current tile where the cursor is
            startTileIndex = self.cursor.mousePositionToTile()
            startTile = colourBoard[startTileIndex[0], startTileIndex[1]]
            
            # If the tile is not empty we should get the piece at the current tile
            if not startTile.isEmpty():
                piece = startTile.getPiece()
                
                # Getting the legal moves for the piece in the current position
                legalMoves = piece.getMoves(self.gameBoard.board)
                
                print('fired')
                
                # Drawing the legal moves to the screen
                self.gui.drawLegalMoves(legalMoves)
                
        # What should be done when the mouse is released
        if event.type == pygame.MOUSEBUTTONUP:
            
            # Getting the current tile where the cursor is
            endTileIndex = self.cursor.mousePositionToTile()
            endTile = self.gameBoard.board[endTileIndex[0], endTileIndex[1]]
            
            # If the endTile is a legalMove
            if legalMoves[endTileIndex[0], endTileIndex[1]].isValid():
                # Remove the piece from the current tile and add it to the new tile
                piece = startTile.removePiece()
                endTile.addPiece(piece)
                
                # Redrawing board
                self.gui.drawBoard()
                self.gui.drawPieces(self.gameBoard.board)
                
                # Refreshing screen
                pygame.display.update()
                
                # Returning False to break out of loop
                return False
            
        # Will keep the loop going by returning true
        return True
                
                    
                    
            
        