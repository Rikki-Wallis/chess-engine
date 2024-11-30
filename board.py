from rook import Rook
from tile import Tile
import numpy as np


class Board():
    
    def __init__(self):
        self.board = np.array[
                                [Tile("a8", 0,0), Tile("b8", 0,1), Tile("c8", 0,2), Tile("d8", 0,3), Tile("e8", 0,4), Tile("f8", 0,5), Tile("g8", 0,6), Tile("h8", 0,7)],
                                [Tile("a7", 1,0), Tile("b7", 1,1), Tile("c7", 1,2), Tile("d7", 1,3), Tile("e7", 1,4), Tile("f7", 1,5), Tile("g7", 1,6), Tile("h7", 1,7)],
                                [Tile("a6", 2,0), Tile("b6", 2,1), Tile("c6", 2,2), Tile("d6", 2,3), Tile("e6", 2,4), Tile("f6", 2,5), Tile("g6", 2,6), Tile("h6", 2,7)],
                                [Tile("a5", 3,0), Tile("b5", 3,1), Tile("c5", 3,2), Tile("d5", 3,3), Tile("e5", 3,4), Tile("f5", 3,5), Tile("g5", 3,6), Tile("h5", 3,7)],
                                [Tile("a4", 4,0), Tile("b4", 4,1), Tile("c4", 4,2), Tile("d4", 4,3), Tile("e4", 4,4), Tile("f4", 4,5), Tile("g4", 4,6), Tile("h4", 4,7)],
                                [Tile("a3", 5,0), Tile("b3", 5,1), Tile("c3", 5,2), Tile("d3", 5,3), Tile("e3", 5,4), Tile("f3", 5,5), Tile("g3", 5,6), Tile("h3", 5,7)],
                                [Tile("a2", 6,0), Tile("b2", 6,1), Tile("c2", 6,2), Tile("d2", 6,3), Tile("e2", 6,4), Tile("f2", 6,5), Tile("g2", 6,6), Tile("h2", 6,7)],
                                [Tile("a1", 7,0), Tile("b1", 7,1), Tile("c1", 7,2), Tile("d1", 7,3), Tile("e1", 7,4), Tile("f1", 7,5), Tile("g1", 7,6), Tile("h1", 7,7)]
                              ]
        
    def setupStartingPosition(self):
        self.board[0,0].add(Rook('b', "aRook"))