""" Helper functions for unit tests """

from contextlib import contextmanager
from io import StringIO
import sys

from res import types
from src import coordinate
from src import gamenode

@contextmanager
def captured_output():
    """ Redirects stdout to StringIO so we can inspect Print statements """
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

def parse_board_input(description):
    gnObject1 = gamenode.GameNode()

    # Remove any lines that are not part of the board
    cleanDescription = []
    for line in description:
        if line[0] != ' ':
            cleanDescription.append(line)

    # Even:
    # coordinate x = 2 * j
    # coordinate y = 10 - i
    # description x = i
    # description y = 6 * j + 5
    # Odd:
    # coordinate x = 2 * j - 1
    # coordinate y = 10 - i
    # description x = i
    # description y = 6 * j + 2

    # Do item #0 of board_description. This corresponds to y=10 on board
    gnObject1.setState(coordinate.Coordinate(2, 10),
                       types.getPieceIntValueFromChar(cleanDescription[0][5]))
    gnObject1.setState(coordinate.Coordinate(4, 10),
                       types.getPieceIntValueFromChar(cleanDescription[0][11]))
    gnObject1.setState(coordinate.Coordinate(6, 10),
                       types.getPieceIntValueFromChar(cleanDescription[0][17]))
    gnObject1.setState(coordinate.Coordinate(8, 10),
                       types.getPieceIntValueFromChar(cleanDescription[0][23]))
    gnObject1.setState(coordinate.Coordinate(10, 10),
                       types.getPieceIntValueFromChar(cleanDescription[0][29]))

    # Do item #1 of board_description. This corresponds to y=9 on board
    gnObject1.setState(coordinate.Coordinate(1, 9),
                       types.getPieceIntValueFromChar(cleanDescription[1][2]))
    gnObject1.setState(coordinate.Coordinate(3, 9),
                       types.getPieceIntValueFromChar(cleanDescription[1][8]))
    gnObject1.setState(coordinate.Coordinate(5, 9),
                       types.getPieceIntValueFromChar(cleanDescription[1][14]))
    gnObject1.setState(coordinate.Coordinate(7, 9),
                       types.getPieceIntValueFromChar(cleanDescription[1][20]))
    gnObject1.setState(coordinate.Coordinate(9, 9),
                       types.getPieceIntValueFromChar(cleanDescription[1][26]))

    # Do item #2 of board_description. This corresponds to y=8 on board
    gnObject1.setState(coordinate.Coordinate(2, 8),
                       types.getPieceIntValueFromChar(cleanDescription[2][5]))
    gnObject1.setState(coordinate.Coordinate(4, 8),
                       types.getPieceIntValueFromChar(cleanDescription[2][11]))
    gnObject1.setState(coordinate.Coordinate(6, 8),
                       types.getPieceIntValueFromChar(cleanDescription[2][17]))
    gnObject1.setState(coordinate.Coordinate(8, 8),
                       types.getPieceIntValueFromChar(cleanDescription[2][23]))
    gnObject1.setState(coordinate.Coordinate(10, 8),
                       types.getPieceIntValueFromChar(cleanDescription[2][29]))

    # Do item #3 of board_description. This corresponds to y=7 on board
    gnObject1.setState(coordinate.Coordinate(1, 7),
                       types.getPieceIntValueFromChar(cleanDescription[3][2]))
    gnObject1.setState(coordinate.Coordinate(3, 7),
                       types.getPieceIntValueFromChar(cleanDescription[3][8]))
    gnObject1.setState(coordinate.Coordinate(5, 7),
                       types.getPieceIntValueFromChar(cleanDescription[3][14]))
    gnObject1.setState(coordinate.Coordinate(7, 7),
                       types.getPieceIntValueFromChar(cleanDescription[3][20]))
    gnObject1.setState(coordinate.Coordinate(9, 7),
                       types.getPieceIntValueFromChar(cleanDescription[3][26]))

    # Do item #4 of board_description. This corresponds to y=6 on board
    gnObject1.setState(coordinate.Coordinate(2, 6),
                       types.getPieceIntValueFromChar(cleanDescription[4][5]))
    gnObject1.setState(coordinate.Coordinate(4, 6),
                       types.getPieceIntValueFromChar(cleanDescription[4][11]))
    gnObject1.setState(coordinate.Coordinate(6, 6),
                       types.getPieceIntValueFromChar(cleanDescription[4][17]))
    gnObject1.setState(coordinate.Coordinate(8, 6),
                       types.getPieceIntValueFromChar(cleanDescription[4][23]))
    gnObject1.setState(coordinate.Coordinate(10, 6),
                       types.getPieceIntValueFromChar(cleanDescription[4][29]))

    # Do item #5 of board_description. This corresponds to y=5 on board
    gnObject1.setState(coordinate.Coordinate(1, 5),
                       types.getPieceIntValueFromChar(cleanDescription[5][2]))
    gnObject1.setState(coordinate.Coordinate(3, 5),
                       types.getPieceIntValueFromChar(cleanDescription[5][8]))
    gnObject1.setState(coordinate.Coordinate(5, 5),
                       types.getPieceIntValueFromChar(cleanDescription[5][14]))
    gnObject1.setState(coordinate.Coordinate(7, 5),
                       types.getPieceIntValueFromChar(cleanDescription[5][20]))
    gnObject1.setState(coordinate.Coordinate(9, 5),
                       types.getPieceIntValueFromChar(cleanDescription[5][26]))

    # Do item #6 of board_description. This corresponds to y=4 on board
    gnObject1.setState(coordinate.Coordinate(2, 4),
                       types.getPieceIntValueFromChar(cleanDescription[6][5]))
    gnObject1.setState(coordinate.Coordinate(4, 4),
                       types.getPieceIntValueFromChar(cleanDescription[6][11]))
    gnObject1.setState(coordinate.Coordinate(6, 4),
                       types.getPieceIntValueFromChar(cleanDescription[6][17]))
    gnObject1.setState(coordinate.Coordinate(8, 4),
                       types.getPieceIntValueFromChar(cleanDescription[6][23]))
    gnObject1.setState(coordinate.Coordinate(10, 4),
                       types.getPieceIntValueFromChar(cleanDescription[6][29]))

    # Do item #7 of board_description. This corresponds to y=3 on board
    gnObject1.setState(coordinate.Coordinate(1, 3),
                       types.getPieceIntValueFromChar(cleanDescription[7][2]))
    gnObject1.setState(coordinate.Coordinate(3, 3),
                       types.getPieceIntValueFromChar(cleanDescription[7][8]))
    gnObject1.setState(coordinate.Coordinate(5, 3),
                       types.getPieceIntValueFromChar(cleanDescription[7][14]))
    gnObject1.setState(coordinate.Coordinate(7, 3),
                       types.getPieceIntValueFromChar(cleanDescription[7][20]))
    gnObject1.setState(coordinate.Coordinate(9, 3),
                       types.getPieceIntValueFromChar(cleanDescription[7][26]))

    # Do item #8 of board_description. This corresponds to y=2 on board
    gnObject1.setState(coordinate.Coordinate(2, 2),
                       types.getPieceIntValueFromChar(cleanDescription[8][5]))
    gnObject1.setState(coordinate.Coordinate(4, 2),
                       types.getPieceIntValueFromChar(cleanDescription[8][11]))
    gnObject1.setState(coordinate.Coordinate(6, 2),
                       types.getPieceIntValueFromChar(cleanDescription[8][17]))
    gnObject1.setState(coordinate.Coordinate(8, 2),
                       types.getPieceIntValueFromChar(cleanDescription[8][23]))
    gnObject1.setState(coordinate.Coordinate(10, 2),
                       types.getPieceIntValueFromChar(cleanDescription[8][29]))

    # Do item #9 of board_description. This corresponds to y=1 on board
    gnObject1.setState(coordinate.Coordinate(1, 1),
                       types.getPieceIntValueFromChar(cleanDescription[9][2]))
    gnObject1.setState(coordinate.Coordinate(3, 1),
                       types.getPieceIntValueFromChar(cleanDescription[9][8]))
    gnObject1.setState(coordinate.Coordinate(5, 1),
                       types.getPieceIntValueFromChar(cleanDescription[9][14]))
    gnObject1.setState(coordinate.Coordinate(7, 1),
                       types.getPieceIntValueFromChar(cleanDescription[9][20]))
    gnObject1.setState(coordinate.Coordinate(9, 1),
                       types.getPieceIntValueFromChar(cleanDescription[9][26]))

    return gnObject1
