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
    
while True:
    clock.tick(60)

    # Event Handler
    for event in pygame.event.get():
        # If the player decides to quit out of the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # If the mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handleClick(currentColour)
            # # While the mouse button is pressed down
            # while pygame.mouse.get_pressed()[0]:
        
    # If a move has been made switch the current colours turn
    if game.hasMoveBeenMade == True:
        currentColour = 'w' if currentColour == 'b' else 'b'
        game.hasMoveBeenMade = False
                
        


        


    
    