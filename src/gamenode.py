""" The basic state of the game board """

class GameNode(object):
    """ Class that stores the basic state of the game board """
    def __init__(self):
        # int array, defaults to 0 in C
        self.gameState = [[-1, -1, 0, 0, 0, -1, -1],
                          [-1, -1, 0, 0, 0, -1, -1],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [-1, -1, 0, 0, 0, -1, -1],
                          [-1, -1, 0, 0, 0, -1, -1],]
        self.leafP = None # float
        self.rootP = None # bool
        self.score = None # bool

    def print_middle_rows(self, seperator=""):
        """ Print the middle 3 rows of the game board """
        # Element 7 in the template is the seperator
        row_template = "{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}"
        print(row_template.format(self.gameState[0][4],
                                  self.gameState[1][4],
                                  self.gameState[2][4],
                                  self.gameState[3][4],
                                  self.gameState[4][4],
                                  self.gameState[5][4],
                                  self.gameState[6][4],
                                  seperator))
        print(row_template.format(self.gameState[0][3],
                                  self.gameState[1][3],
                                  self.gameState[2][3],
                                  self.gameState[3][3],
                                  self.gameState[4][3],
                                  self.gameState[5][3],
                                  self.gameState[6][3],
                                  seperator))
        print(row_template.format(self.gameState[0][2],
                                  self.gameState[1][2],
                                  self.gameState[2][2],
                                  self.gameState[3][2],
                                  self.gameState[4][2],
                                  self.gameState[5][2],
                                  self.gameState[6][2],
                                  seperator))

    def print_board(self):
        """ Originally called 'print' """
        print("   {0}{1}{2}   ".format(self.gameState[2][6],
                                       self.gameState[3][6],
                                       self.gameState[4][6]))
        print("   {0}{1}{2}   ".format(self.gameState[2][5],
                                       self.gameState[3][5],
                                       self.gameState[4][5]))
        self.print_middle_rows()
        print("   {0}{1}{2}   ".format(self.gameState[2][1],
                                       self.gameState[3][1],
                                       self.gameState[4][1]))
        print("   {0}{1}{2}   ".format(self.gameState[2][0],
                                       self.gameState[3][0],
                                       self.gameState[4][0]))

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
