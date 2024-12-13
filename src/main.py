import time
import pygame
from board import Board
from gui import GUI
from cursor import Cursor
from constants import *
from game import Game

# Initialising the game board
gameBoard = Board()
# Setting up pieces in the starting position 
gameBoard.setupStartingPosition()
# Initialising the pygame GUI
gui = GUI()
# Drawing the board to the screen
gui.drawBoard()

clock = pygame.time.Clock()

cursor = Cursor(gui)

game = Game(gameBoard, gui, cursor)

currentColour = 'w'

# Drawing the board to the screen
gui.drawBoard()
gui.drawPieces(gameBoard.board)

running = True

while running:
    clock.tick(60)

    # Event Handler
    for event in pygame.event.get():
        # If the player decides to quit out of the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # If the mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Getting the piece on the tile
            piece = cursor.mousePositionToPiece(gameBoard.board)
            
            # Handling the click
            game.handleClick(currentColour)
            
            # # While the mouse button is pressed down
            # while pygame.mouse.get_pressed()[0]:
            #     # gui.drawBoard()
            #     # gui.drawPieces(gameBoard.board, piece)
            #     # gui.drawLegalMoves(piece.getMoves(gameBoard.board))
            #     gui.drawPieceToCursor(piece, cursor)

        
    # If a move has been made switch the current colours turn and check if the king is in checkmate
    if game.hasMoveBeenMade == True:
        # Changing current colour
        currentColour = 'w' if currentColour == 'b' else 'b'
        
        # Resseting move counter
        game.hasMoveBeenMade = False
        
        # Checking if the king is in check
        if game.isKingInCheck(currentColour):
            
            # If the king is in check check if they are in checkmate
            if game.isKingInCheckMate(currentColour):
                
                # Printing the winner
                winnerColour = 'w' if currentColour == 'b' else 'b' 
                print(f'The winner is {winnerColour}')
                time.sleep(10)
                running = False
            