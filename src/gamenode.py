""" The basic state of the game board """

from res.types import getPieceAbbreviation

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
        self.leafP = None # float
        self.rootP = None # bool
        self.score = None # bool
        self.isCapture = False
        self.winningState = False

    def __eq__(self, other):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.gameState[i][j] != other.gameState[i][j]:
                    return False
        return True

    def print_board(self):
        """ Prints the board in a way that is easy to understand """
        line = "0  {0}{1}{2}{3}{4}{5}{6}{7}{8}{9}"
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
            line = "{0}  {1}{2}{3}{4}{5}{6}{7}{8}{9}{10}"
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
        print("\n    1  2  3  4  5  6  7  8  9  0")

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
