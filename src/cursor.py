import pygame

"""
A class which handles anything to do with the cursor on the window. This can be done without a class
but this makes the process much more simple.
"""
class Cursor():
    
    def __init__(self, gui):
        """
        The Cursor classes init method.
        
        params:
            gui (GUI) - The gui class that handles all gui processes within the game
        """
        self.gui = gui
    
    def getMousePosition(self):
        """
        A simple method that returns the current mouse position
        
        return:
            mousePosition (tuple(int, int)) - The current position of the mouse in the pygame window
        """
        return pygame.mouse.get_pos()
    
    def mousePositionToTile(self):
        """
        A method which maps the current mouse position to the corresponding tile on the board.
        
        return:
            tileIndex (tuple(int, int)) - The tile index corresponding to the current position of the mouse
        """
        # Getting the current size of the squares
        squareSize = self.gui.getSquareSize()
        
        # Getting the current mouse position
        mousePosition = self.getMousePosition()
        
        # Determine index based on the current mouse position ensuring that it is within bounds
        rowIndex = min(mousePosition[1] // squareSize, 7)
        collumnIndex = min(mousePosition[0] // squareSize, 7)
        
        # Returning the index of the tile
        return (rowIndex, collumnIndex)
        
