import pygame


class Cursor():
    
    def __init__(self, gui):
        self.gui = gui
    
    def getMousePosition(self):
        return pygame.mouse.get_pos()
    
    def mousePositionToTile(self):
        # Getting the current size of the squares
        squareSize = self.gui.getSquareSize()
        
        # Getting the current mouse position
        mousePosition = self.getMousePosition()
        
        # Determine index based on the current mouse position ensuring that it is within bounds
        rowIndex = min(mousePosition[1] // squareSize, 7)
        collumnIndex = min(mousePosition[0] // squareSize, 7)
        
        # Returning the index of the tile
        return (rowIndex, collumnIndex)
        
