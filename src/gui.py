import pygame
from pygame._sdl2 import Window

from constants import *
import math
from tile import Tile

"""
Class which handles all the GUI elements of the chess program.
"""
class GUI():
    
    """
    Init method of the class initialising the screen and loads the asset list
    """
    def __init__(self):
        self.assetList = self.importGraphics()
        self.initScreen()
        
    """
    Method which loads all of the piece assets and saves them into a dictionary
    
    returns:
        assetDict (Dictionary) - A dictionary with key, value pairs which allows an asset
                                 to be loaded given a piece type.
    """
    def importGraphics(self):
        # Importing Assests
        blackKing = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\Black King.png')
        blackQueen = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\Black Queen.png')
        blackBishop = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\Black Bishop.png')
        blackKnight = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\Black Knight.png')
        blackRook = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\Black Rook.png')
        blackPawn = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\Black Pawn.png')

        whiteKing = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\White King.png')
        whiteQueen = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\White Queen.png')
        whiteRook = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\White Rook.png')
        whiteBishop = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\White Bishop.png')
        whiteKnight = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\White Knight.png')
        whitePawn = pygame.image.load('C:\\Users\\rikki\\Desktop\\Personal Projects\\DGT Board\\Chess Assets\\White Pawn.png')
        
        # Creating a dictionary for all the assets
        assetDict = { BLACK_PAWN : blackPawn,
                      BLACK_ROOK : blackRook,
                      BLACK_KNIGHT : blackKnight,
                      BLACK_BISHOP : blackBishop,
                      BLACK_KING : blackKing,
                      BLACK_QUEEN : blackQueen,
                      WHITE_PAWN : whitePawn,
                      WHITE_ROOK : whiteRook,
                      WHITE_KNIGHT : whiteKnight,
                      WHITE_BISHOP : whiteBishop,
                      WHITE_KING : whiteKing,
                      WHITE_QUEEN : whiteQueen   
                    }
        
        # Returning the asset dictionary
        return assetDict
            
    """
    A method which initialises the pygame window and sets it to be adjustable.
    """
    def initScreen(self):
        # Initialising pygame
        pygame.init()

        # Defining Screen Variables
        screenWidth = 649
        screenHeight = 649
        
        # Initialising the screen
        self.screen = pygame.display.set_mode((screenWidth, screenHeight),pygame.RESIZABLE)
        
        # Maximizing the window
        Window.from_display_module().maximize()
    
    """
    A method which calculates the square size of each tile given the current screen size
    
    returns:
        squareSize (int) - The width of each tile dependent on the screen size
    """
    def getSquareSize(self):
        # Getting Screen Size
        screenSize = self.screen.get_size()
        
        # Obtaining the width of the screen
        width = screenSize[0]

        # Capping the width to the hieght of the screen
        if width > 649:
            width = 649

        # Returning square size
        return math.floor(width/8)
    
    """
    A method which draws the chess board and refreshes the screen
    """
    def drawBoard(self):
        # Getting the current square size depending on the width and hieght of the screen
        squareSize = self.getSquareSize()
        
        # Iterating over each row
        for row in range(BOARD_SIZE):
            
            # Iterating over each collumn
            for col in range(BOARD_SIZE):
                
                # Getting the right colour
                colour = BIEGE if (row + col) % 2 == 0 else BROWN
                
                # Calculate the top left corner of the square
                x = col * squareSize
                y = row * squareSize
                
                # Drawing the square to the screen
                pygame.draw.rect(self.screen, colour, (x, y, squareSize, squareSize))
                
        # Refreshing screen
        pygame.display.update()
    
    """
    A method similar to drawBoard however this method specifically focuses on drawing
    the piece assets to the screen corresponding to where the pieces are on the board.
    
    params:
        board (List[List[Tile]]) - The current board that the game is being played on
    """
    def drawPieces(self, board):
        # Getting the square size
        squareSize = self.getSquareSize()
        
        # Iterating over each row of the board
        for rowIndex, row in enumerate(board):
            
            # Iterating over each tile in the row
            for collumnIndex, tile in enumerate(row):
                
                # If the tile is empty we do not have to draw anything
                if tile.isEmpty():
                    pass
                
                # Otherwise we should draw the piece
                else:
                    # Getting the piece on the tile
                    piece = tile.getPiece()
                    
                    # Getting top left position of the square
                    topLeftx = collumnIndex * squareSize
                    topLefty = rowIndex * squareSize
                    
                    # Getting the size of the asset
                    asset = self.assetList[piece.type]
                    pieceWidth, pieceHeight = asset.get_size()
                    
                    # Calculating the centered position of the asset
                    centeredX = topLeftx + (squareSize - pieceWidth)/2
                    centeredY = topLefty + (squareSize - pieceHeight)/2
                    
                    # Getting the blit for the piece
                    self.screen.blit(asset, (centeredX, centeredY))
                    
        # Refreshing screen
        pygame.display.update()