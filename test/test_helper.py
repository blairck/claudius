""" Tests for the helper module """

import unittest

# pylint: disable=import-error
import helper
from res import types
from src import coordinate
from src import boardParser

class TestHelper(unittest.TestCase):
    """ Tests for the helper module """

    def test_parseBoardInput_good(self):
        """ Verify a board description is parsed correctly """
        board_description = [
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     b     .     b     b 0",
            "9 b     b     .     b     b    9",
            "8    b     .     b     .     b 8",
            "7 b     b     b     b     b    7",
            "6    .     .     .     B     . 6",
            "5 .     a     .     .     .    5",
            "4    A     .     a     .     a 4",
            "3 a     .     a     a     a    3",
            "2    .     a     .     .     a 2",
            "1 a     a     a     a     a    1",
            "  1  2  3  4  5  6  7  8  9  0",]

        actualResult = boardParser.parseBoardInput(board_description)
        self.assertEqual(actualResult.getState(coordinate.Coordinate(10, 6)),
                         types.EMPTY)
        self.assertEqual(actualResult.getState(coordinate.Coordinate(3, 5)),
                         types.PLAYER_A_REGULAR)
        self.assertEqual(actualResult.getState(coordinate.Coordinate(2, 4)),
                         types.PLAYER_A_KING)
        self.assertEqual(actualResult.getState(coordinate.Coordinate(4, 10)),
                         types.PLAYER_B_REGULAR)
        self.assertEqual(actualResult.getState(coordinate.Coordinate(8, 6)),
                         types.PLAYER_B_KING)
