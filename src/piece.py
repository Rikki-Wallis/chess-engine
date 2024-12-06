# Imports
from abc import ABC, abstractmethod

"""
Abstract class which represents the pieces in chess
"""
class Piece(ABC):
    
    """
    Init method which defines piece attributes
    params:
        colour (char) - The colour of the piece (b/w)
        name (string) - The name of the piece
    """
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        self.position = None
        self.type = None
    
    """
    Abstract method which when implemented will return
    what moves the piece can make.
    params:
        board (List[List]) - The board on which the game is being played on
    returns:
        returns an array of all the available tiles the piece can move too
    """
    @abstractmethod
    def getMoves(self, board):
        pass
    