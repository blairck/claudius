""" The basic state of the game board """

class GameNode(object):
    """ Class that stores the basic state of the game board """
    def __init__(self):
        self.gameState = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
        self.leafP = None # float
        self.rootP = None # bool
        self.score = None # bool

    def print_board(self):
        """ Prints a simplified representation of the board """
        y_indices = list(range(10))
        y_indices.reverse()
        for y in y_indices:
            line = "{0}  {1}  {2}  {3}  {4}  {5}  {6}  {7}  {8}  {9}"
            print(line.format(self.gameState[0][y],
                              self.gameState[1][y],
                              self.gameState[2][y],
                              self.gameState[3][y],
                              self.gameState[4][y],
                              self.gameState[5][y],
                              self.gameState[6][y],
                              self.gameState[7][y],
                              self.gameState[8][y],
                              self.gameState[9][y],))

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
