""" Helper functions shared between 2 or more modules"""

from src import coordinate


def checkIfInt(value):
    """ Type checker for values to determine if they are of type int """
    if not isinstance(value, int):
        raise TypeError(("value is not an int. "
                         "value = {0}").format(value))

def checkIfCoordinateIsValid(x, y):
    """ Check if board values constitute a valid location on the board """
    valid = False
    odd_values = (1, 3, 5, 7, 9)
    even_values = (2, 4, 6, 8, 10)
    if y in even_values:
        if x in even_values:
            valid = True
    elif y in odd_values:
        if x in odd_values:
            valid = True
    if valid:
        return True
    else:
        raise ValueError(("Coordinate is not on the board: "
                          "({0}, {1})").format(x, y))


def getTupleOfAllCoordinates():
    """ Gets a tuple of all legal Coordinates on the board """
    return (coordinate.Coordinate(1, 1),
            coordinate.Coordinate(3, 1),
            coordinate.Coordinate(5, 1),
            coordinate.Coordinate(7, 1),
            coordinate.Coordinate(9, 1),
            coordinate.Coordinate(2, 2),
            coordinate.Coordinate(4, 2),
            coordinate.Coordinate(6, 2),
            coordinate.Coordinate(8, 2),
            coordinate.Coordinate(10, 2),
            coordinate.Coordinate(1, 3),
            coordinate.Coordinate(3, 3),
            coordinate.Coordinate(5, 3),
            coordinate.Coordinate(7, 3),
            coordinate.Coordinate(9, 3),
            coordinate.Coordinate(2, 4),
            coordinate.Coordinate(4, 4),
            coordinate.Coordinate(6, 4),
            coordinate.Coordinate(8, 4),
            coordinate.Coordinate(10, 4),
            coordinate.Coordinate(1, 5),
            coordinate.Coordinate(3, 5),
            coordinate.Coordinate(5, 5),
            coordinate.Coordinate(7, 5),
            coordinate.Coordinate(9, 5),
            coordinate.Coordinate(2, 6),
            coordinate.Coordinate(4, 6),
            coordinate.Coordinate(6, 6),
            coordinate.Coordinate(8, 6),
            coordinate.Coordinate(10, 6),
            coordinate.Coordinate(1, 7),
            coordinate.Coordinate(3, 7),
            coordinate.Coordinate(5, 7),
            coordinate.Coordinate(7, 7),
            coordinate.Coordinate(9, 7),
            coordinate.Coordinate(2, 8),
            coordinate.Coordinate(4, 8),
            coordinate.Coordinate(6, 8),
            coordinate.Coordinate(8, 8),
            coordinate.Coordinate(10, 8),
            coordinate.Coordinate(1, 9),
            coordinate.Coordinate(3, 9),
            coordinate.Coordinate(5, 9),
            coordinate.Coordinate(7, 9),
            coordinate.Coordinate(9, 9),
            coordinate.Coordinate(2, 10),
            coordinate.Coordinate(4, 10),
            coordinate.Coordinate(6, 10),
            coordinate.Coordinate(8, 10),
            coordinate.Coordinate(10, 10),)
