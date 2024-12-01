import pygame
from pygame._sdl2 import Window

from board import Board
from gui import GUI
from constants import *

# Initialising the game board
gameBoard = Board()
# Setting up pieces in the starting position 
gameBoard.setupStartingPosition()
# Initialising the pygame GUI
gui = GUI()
# Drawing the board to the screen
gui.drawBoard()

while True:
    gui.drawPieces(gameBoard.board)