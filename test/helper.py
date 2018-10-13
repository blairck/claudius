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
    """ Takes a description of a board and returns the corresponding
    GameNode """
    gnObject1 = gamenode.GameNode()

    # Remove any lines that are not part of the board
    cleanDescription = []
    for line in description:
        if line[0] != ' ':
            cleanDescription.append(line)

    # Set board state where coordinate Y is even
    for i in range(5):
        for j in range(5):
            pieceChar = cleanDescription[2*i][6*j+5]
            gnObject1.setState(coordinate.Coordinate(2*j+2, 10-2*i),
                               types.getPieceIntValueFromChar(pieceChar))

    # Set board state where coordinate Y is odd
    for i in range(5):
        for j in range(5):
            pieceChar = cleanDescription[2*i+1][6*j+2]
            gnObject1.setState(coordinate.Coordinate(2*j+1, 9-2*i),
                               types.getPieceIntValueFromChar(pieceChar))

    return gnObject1
