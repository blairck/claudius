""" Tests for the GameNode module """

import unittest

from test import helper
from res import types
from src import coordinate
from src import gamenode

class TestGameNode(unittest.TestCase):
    """ Tests for the GameNode module """

    def test_default_instantiation(self):
        """ Test a known default instantiation """
        gnObject = gamenode.GameNode()
        result = gnObject.gameState[0][0]
        self.assertEqual(result, types.EMPTY)
        self.assertFalse(gnObject.score)

    def test_print_board(self):
        """Check that print_board works"""
        with helper.captured_output() as out:
            gnObject = gamenode.GameNode()
            gnObject.print_board()
            actual_print = out.getvalue()
            expected_print = ("  1  2  3  4  5  6  7  8  9  0\n"
                              "0    .     .     .     .     . 0\n"
                              "9 .     .     .     .     .    9\n"
                              "8    .     .     .     .     . 8\n"
                              "7 .     .     .     .     .    7\n"
                              "6    .     .     .     .     . 6\n"
                              "5 .     .     .     .     .    5\n"
                              "4    .     .     .     .     . 4\n"
                              "3 .     .     .     .     .    3\n"
                              "2    .     .     .     .     . 2\n"
                              "1 .     .     .     .     .    1\n"
                              "  1  2  3  4  5  6  7  8  9  0\n")
            self.assertEqual(actual_print, expected_print)

    def test_getState(self):
        """ Check getting the board state at a Coordinate """
        gnObject = gamenode.GameNode()
        self.assertEqual(gnObject.getState(coordinate.Coordinate(3, 3)),
                         types.EMPTY)

    def test_setState(self):
        """ Test setting the board state at a Coordinate with a value """
        gnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(5, 1)
        testValue = types.PLAYER_A_KING
        gnObject.setState(testCoordinate, testValue)
        self.assertEqual(gnObject.getState(testCoordinate),
                         types.PLAYER_A_KING)

    def test_eq_same(self):
        """ Check equality function compares boards as equal """
        gnObject1 = gamenode.GameNode()
        gnObject2 = gamenode.GameNode()
        self.assertTrue(gnObject1 == gnObject2)

    def test_eq_not_same(self):
        """ Check equality function compares boards as not equal """
        gnObject1 = gamenode.GameNode()
        gnObject1.setState(coordinate.Coordinate(5, 3), types.PLAYER_A_KING)
        gnObject2 = gamenode.GameNode()
        self.assertTrue(gnObject1 != gnObject2)

    def test_playerWins(self):
        """ Check if a player has won the game """
        gnObject = gamenode.GameNode()
        self.assertRaises(NotImplementedError, gnObject.playerWins)

    def test_createStartingPosition(self):
        """ Check that the starting position is set correctly """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        self.assertEqual(gnObject.getState(coordinate.Coordinate(2, 2)),
                         types.PLAYER_A_REGULAR)
        self.assertEqual(gnObject.getState(coordinate.Coordinate(6, 10)),
                         types.PLAYER_B_REGULAR)
        self.assertEqual(gnObject.getState(coordinate.Coordinate(9, 5)),
                         types.EMPTY)
