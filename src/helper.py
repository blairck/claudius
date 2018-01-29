""" Helper functions shared between 2 or more modules"""

def checkIfInt(value):
    """ Type checker for values to determine if they are of type int """
    if not isinstance(value, int):
        raise TypeError(("value is not an int. "
                         "value = {0}").format(value))

def checkIfCoordinateIsValid(x, y):
    """ Check if board values constitute a valid location on the board """
    valid = False
    even_values = (1, 3, 5, 7, 9)
    odd_values = (2, 4, 6, 8, 0)
    if y in odd_values:
        if x in odd_values:
            valid = True
    elif y in even_values:
        if x in even_values:
            valid = True
    if valid:
        return True
    else:
        raise ValueError(("Coordinate is not on the board: "
                         "({0}, {1})").format(x, y))
