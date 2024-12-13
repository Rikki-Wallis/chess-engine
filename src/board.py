from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.pawn import Pawn
from tile import Tile
from pieces.king import King
import numpy as np

"""
Class which defines how the chess board behaves in the program
"""
class Board():
    
    def __init__(self):
        """
        The classes init method which initialises an np.array representing each tile on the board
        """
        self.board = np.array([
                                [Tile("a8", (0,0)), Tile("b8", (0,1)), Tile("c8", (0,2)), Tile("d8", (0,3)), Tile("e8", (0,4)), Tile("f8", (0,5)), Tile("g8", (0,6)), Tile("h8", (0,7))],
                                [Tile("a7", (1,0)), Tile("b7", (1,1)), Tile("c7", (1,2)), Tile("d7", (1,3)), Tile("e7", (1,4)), Tile("f7", (1,5)), Tile("g7", (1,6)), Tile("h7", (1,7))],
                                [Tile("a6", (2,0)), Tile("b6", (2,1)), Tile("c6", (2,2)), Tile("d6", (2,3)), Tile("e6", (2,4)), Tile("f6", (2,5)), Tile("g6", (2,6)), Tile("h6", (2,7))],
                                [Tile("a5", (3,0)), Tile("b5", (3,1)), Tile("c5", (3,2)), Tile("d5", (3,3)), Tile("e5", (3,4)), Tile("f5", (3,5)), Tile("g5", (3,6)), Tile("h5", (3,7))],
                                [Tile("a4", (4,0)), Tile("b4", (4,1)), Tile("c4", (4,2)), Tile("d4", (4,3)), Tile("e4", (4,4)), Tile("f4", (4,5)), Tile("g4", (4,6)), Tile("h4", (4,7))],
                                [Tile("a3", (5,0)), Tile("b3", (5,1)), Tile("c3", (5,2)), Tile("d3", (5,3)), Tile("e3", (5,4)), Tile("f3", (5,5)), Tile("g3", (5,6)), Tile("h3", (5,7))],
                                [Tile("a2", (6,0)), Tile("b2", (6,1)), Tile("c2", (6,2)), Tile("d2", (6,3)), Tile("e2", (6,4)), Tile("f2", (6,5)), Tile("g2", (6,6)), Tile("h2", (6,7))],
                                [Tile("a1", (7,0)), Tile("b1", (7,1)), Tile("c1", (7,2)), Tile("d1", (7,3)), Tile("e1", (7,4)), Tile("f1", (7,5)), Tile("g1", (7,6)), Tile("h1", (7,7))],
                              ])
        
    
    def setupStartingPosition(self):
        """
        A method which sets up the starting position of the black and white pieces in a 
        classic game of chess.
        """
        # Creating all the pieces on the board
        self.bKing = King('b', "King")
        self.wKing = King('w', "King")
        
        bARook = Rook('b', "aRook", self.bKing)
        bHRook = Rook('b', "hRook", self.bKing)
        
        bCBishop = Bishop('b', "cBishop", self.bKing)
        bFBishop = Bishop('b', "cBishop", self.bKing)
        
        bBKnight = Knight('b', "bKnight", self.bKing)
        bGKnight = Knight('b', "gKnight", self.bKing)
        
        bQueen = Queen('b', "Queen", self.bKing)
        
        bAPawn = Pawn('b', "aPawn", self.bKing)
        bBPawn = Pawn('b', "bPawn", self.bKing)
        bCPawn = Pawn('b', "cPawn", self.bKing)
        bDPawn = Pawn('b', "dPawn", self.bKing)
        bEPawn = Pawn('b', "ePawn", self.bKing)
        bFPawn = Pawn('b', "fPawn", self.bKing)
        bGPawn = Pawn('b', "gPawn", self.bKing)
        bHPawn = Pawn('b', "hPawn", self.bKing)
        
        
        wARook = Rook('w', "aRook", self.wKing)
        wHRook = Rook('w', "hRook", self.wKing)
        
        wCBishop = Bishop('w', "cBishop", self.wKing)
        wFBishop = Bishop('w', "fBishop", self.wKing)
        
        wBKnight = Knight('w', "bKnight", self.wKing)
        wGKnight = Knight('w', "gKnight", self.wKing)
        
        wQueen = Queen('w', "Queen", self.wKing)
        
        wAPawn = Pawn('w', "aPawn", self.wKing)
        wBPawn = Pawn('w', "bPawn", self.wKing)
        wCPawn = Pawn('w', "cPawn", self.wKing)
        wDPawn = Pawn('w', "dPawn", self.wKing)
        wEPawn = Pawn('w', "ePawn", self.wKing)
        wFPawn = Pawn('w', "fPawn", self.wKing)
        wGPawn = Pawn('w', "gPawn", self.wKing)
        wHPawn = Pawn('w', "hPawn", self.wKing)
        
        # Adding all the pieces to a list
        blackPieceList = [bARook, bHRook, bCBishop, bFBishop, bBKnight, bGKnight, bQueen, self.bKing, bAPawn, bBPawn, bCPawn, bDPawn, bEPawn, bFPawn, bGPawn, bHPawn]
        whitePieceList = [wARook, wHRook, wCBishop, wFBishop, wBKnight, wGKnight, wQueen, self.wKing, wAPawn, wBPawn, wCPawn, wDPawn, wEPawn, wFPawn, wGPawn, wHPawn]
        
        # Adding the pieces to the board and to the piece dictionary
        self.board[0,0].addPiece(bARook)
        self.board[0,7].addPiece(bHRook)
        self.board[0,2].addPiece(bCBishop)
        self.board[0,5].addPiece(bFBishop)
        self.board[0,1].addPiece(bBKnight)
        self.board[0,6].addPiece(bGKnight)
        self.board[0,3].addPiece(bQueen)
        self.board[0,4].addPiece(self.bKing)
        self.board[1,0].addPiece(bAPawn)
        self.board[1,1].addPiece(bBPawn)
        self.board[1,2].addPiece(bCPawn)
        self.board[1,3].addPiece(bDPawn)
        self.board[1,4].addPiece(bEPawn)
        self.board[1,5].addPiece(bFPawn)
        self.board[1,6].addPiece(bGPawn)
        self.board[1,7].addPiece(bHPawn)
        
        self.board[7,0].addPiece(wARook)
        self.board[7,7].addPiece(wHRook)
        self.board[7,2].addPiece(wCBishop)
        self.board[7,5].addPiece(wFBishop)
        self.board[7,6].addPiece(wGKnight)
        self.board[7,1].addPiece(wBKnight)
        self.board[7,3].addPiece(wQueen)
        self.board[7,4].addPiece(self.wKing)
        self.board[6,0].addPiece(wAPawn)
        self.board[6,1].addPiece(wBPawn)
        self.board[6,2].addPiece(wCPawn)
        self.board[6,3].addPiece(wDPawn)
        self.board[6,4].addPiece(wEPawn)
        self.board[6,5].addPiece(wFPawn)
        self.board[6,6].addPiece(wGPawn)
        self.board[6,7].addPiece(wHPawn)
        
        # Adding the piece lists to the dictionary
        self.piecesDictionary = {
            'w' : whitePieceList,
            'b' : blackPieceList
        }        
        
    def getKing(self, colour):
        return self.wKing if colour == 'w' else self.bKing
        