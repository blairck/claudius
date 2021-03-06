""" The basic state of the game board """

from res import types
from res.types import getPieceAbbreviation
from src import coordinate

class GameNode(object):
    """ Class that stores the basic state of the game board """
    def __init__(self):
        self.gameState = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],]
        self.score = None # bool
        self.numberOfPiecesForA = None # count of player A pieces
        self.numberOfPiecesForB = None # count of player B pieces
        self.isCapture = False
        self.winningState = False
        self.pieceLastMoved = None
        self.directionDelta = None
        self.deltaLastMoved = None
        self.playerAMoveCount = None
        self.playerBMoveCount = None

    def __eq__(self, other):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.gameState[i][j] != other.gameState[i][j]:
                    return False
        return True

    def print_board(self):
        """ Prints the board in a way that is easy to understand """
        print("  1  2  3  4  5  6  7  8  9  0")
        line = "0{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}0"
        print(line.format(getPieceAbbreviation(self.gameState[0][9]),
                          getPieceAbbreviation(self.gameState[1][9]),
                          getPieceAbbreviation(self.gameState[2][9]),
                          getPieceAbbreviation(self.gameState[3][9]),
                          getPieceAbbreviation(self.gameState[4][9]),
                          getPieceAbbreviation(self.gameState[5][9]),
                          getPieceAbbreviation(self.gameState[6][9]),
                          getPieceAbbreviation(self.gameState[7][9]),
                          getPieceAbbreviation(self.gameState[8][9]),
                          getPieceAbbreviation(self.gameState[9][9]),))
        y_indices = list(range(9))
        y_indices.reverse()
        for y in y_indices:
            line = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{0}"
            print(line.format(y + 1,
                              getPieceAbbreviation(self.gameState[0][y]),
                              getPieceAbbreviation(self.gameState[1][y]),
                              getPieceAbbreviation(self.gameState[2][y]),
                              getPieceAbbreviation(self.gameState[3][y]),
                              getPieceAbbreviation(self.gameState[4][y]),
                              getPieceAbbreviation(self.gameState[5][y]),
                              getPieceAbbreviation(self.gameState[6][y]),
                              getPieceAbbreviation(self.gameState[7][y]),
                              getPieceAbbreviation(self.gameState[8][y]),
                              getPieceAbbreviation(self.gameState[9][y]),))
        print("  1  2  3  4  5  6  7  8  9  0")

    def setState(self, coordinate_arg, value):
        """ Modify value at a specific board location. """
        x = coordinate_arg.get_x_array()
        y = coordinate_arg.get_y_array()
        self.gameState[x][y] = value

    def getState(self, coordinate_arg):
        """ Get value from a specific board location. """
        x = coordinate_arg.get_x_array()
        y = coordinate_arg.get_y_array()
        return self.gameState[x][y]

    def playerWins(self):
        """ Determines if a player has won and returns which one """
        raise NotImplementedError

    def createStartingPosition(self):
        """ Set up gamenode with the regular starting position """
        odd_piece_rows = (1, 3, 5, 7, 9)
        even_piece_rows = (2, 4, 6, 8, 10)

        for y in (1, 3):
            for x in odd_piece_rows:
                self.setState(coordinate.Coordinate(x, y),
                              types.PLAYER_A_REGULAR)

        for y in (7, 9):
            for x in odd_piece_rows:
                self.setState(coordinate.Coordinate(x, y),
                              types.PLAYER_B_REGULAR)

        for y in (2, 4):
            for x in even_piece_rows:
                self.setState(coordinate.Coordinate(x, y),
                              types.PLAYER_A_REGULAR)

        for y in (8, 10):
            for x in even_piece_rows:
                self.setState(coordinate.Coordinate(x, y),
                              types.PLAYER_B_REGULAR)

    def countPlayerPieces(self, piecesToCount):
        """ Counts all pieces in list of piecesToCount"""
        count = 0
        for i in range(0, 10):
            for j in range(0, 10):
                if self.gameState[i][j] in piecesToCount:
                    count += 1
        return count

    def getPieceCount(self, playerAToPlay):
        """ Gets number of pieces a given player has"""
        if playerAToPlay is None:
            errorMessage = "playerAToPlay unassigned: {0}"
            raise ValueError(errorMessage.format(playerAToPlay))
        elif playerAToPlay:
            if self.numberOfPiecesForA:
                return self.numberOfPiecesForA
            playerPieces = (types.PLAYER_A_REGULAR, types.PLAYER_A_KING)
            self.numberOfPiecesForA = self.countPlayerPieces(playerPieces)
            return self.numberOfPiecesForA
        else:
            if self.numberOfPiecesForB:
                return self.numberOfPiecesForB
            playerPieces = (types.PLAYER_B_REGULAR, types.PLAYER_B_KING)
            self.numberOfPiecesForB = self.countPlayerPieces(playerPieces)
            return self.numberOfPiecesForB

    def playerAWins(self):
        """ Returns True if player A won, False otherwise """
        if self.playerBMoveCount == 0:
            self.score = 5000
            return True
        else:
            return False

    def playerBWins(self):
        """ Returns True if player B won, False otherwise """
        if self.playerAMoveCount == 0:
            self.score = -5000
            return True
        else:
            return False

    def determineWinningState(self):
        """ Set winningState if this node is in one """
        self.winningState = bool(self.playerAWins() or self.playerBWins())
