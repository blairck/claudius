""" Tests for the rules module """

import unittest

# pylint: disable=import-error
import helper
from res import types
from src import coordinate
from src import gamenode
from src import rules

# pylint: disable=too-many-public-methods
class TestRules(unittest.TestCase):
    """ Tests for the rules module """

    def test_findConnectionP_nonexistant(self):
        """ FindConnectionP isn't able to find a connection """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules.findConnectionP(startCoordinate, endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_up_right(self):
        """ FindConnectionP is able to find a connection """
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(4, 4)
        actual_result = rules.findConnectionP(startCoordinate, endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_down_right(self):
        """ FindConnectionP is able to find a connection """
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(4, 2)
        actual_result = rules.findConnectionP(startCoordinate, endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_down_left(self):
        """ FindConnectionP is able to find a connection """
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(2, 2)
        actual_result = rules.findConnectionP(startCoordinate, endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_up_left(self):
        """ FindConnectionP is able to find a connection """
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(2, 4)
        actual_result = rules.findConnectionP(startCoordinate, endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_backwards_PLAYER_A_REGULAR(self):
        """ PLAYER_A_REGULAR moving backwards returns false """
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(3, 3)
        board.setState(startCoordinate, types.PLAYER_A_REGULAR)
        actual_result = rules.legalMoveP(board, startCoordinate, endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_forwards_PLAYER_A_REGULAR(self):
        """ PLAYER_A_REGULAR moving forwards returns true """
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(3, 5)
        board.setState(startCoordinate, types.PLAYER_A_REGULAR)
        actual_result = rules.legalMoveP(board, startCoordinate, endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_forwards_disconnected_PLAYER_A_REGULAR(self):
        """ PLAYER_A_REGULAR moving forwards but not connected """
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(3, 7)
        board.setState(startCoordinate, types.PLAYER_A_REGULAR)
        actual_result = rules.legalMoveP(board, startCoordinate, endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_backwards_PLAYER_B_REGULAR(self):
        """ PLAYER_B_REGULAR moving backwards returns false """
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(5, 5)
        board.setState(startCoordinate, types.PLAYER_B_REGULAR)
        actual_result = rules.legalMoveP(board, startCoordinate, endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_forwards_PLAYER_B_REGULAR(self):
        """ PLAYER_B_REGULAR moving fowards returns true """
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(5, 3)
        board.setState(startCoordinate, types.PLAYER_B_REGULAR)
        actual_result = rules.legalMoveP(board, startCoordinate, endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findXDeltaFromDirection_left(self):
        """ Get the delta X from a left direction """
        actual_result = rules.findXDeltaFromDirection(8)
        expected_result = -2
        self.assertEqual(actual_result, expected_result)

    def test_findXDeltaFromDirection_bad(self):
        """ Handle a bad direction """
        self.assertRaises(ValueError,
                          rules.findXDeltaFromDirection,
                          80)

    def test_findYDeltaFromDirection_down(self):
        """ Get the delta Y from a left direction """
        actual_result = rules.findYDeltaFromDirection(4)
        expected_result = -2
        self.assertEqual(actual_result, expected_result)

    def test_findYDeltaFromDirection_bad(self):
        """ Handle a bad direction """
        self.assertRaises(ValueError,
                          rules.findYDeltaFromDirection,
                          80)

    def test_isACaptureP_good(self):
        board_description = [
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     .     .     . 0",
            "9 .     .     .     .     .    9",
            "8    .     .     .     .     . 8",
            "7 .     .     .     .     .    7",
            "6    .     A     b     .     . 6",
            "5 .     .     a     .     .    5",
            "4    .     a     B     .     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",]
        board = helper.parse_board_input(board_description)
        self.assertTrue(rules.isACaptureP(board,
                                          coordinate.Coordinate(5, 5),
                                          2,
                                          True))
        self.assertTrue(rules.isACaptureP(board,
                                          coordinate.Coordinate(5, 5),
                                          4,
                                          True))
        self.assertFalse(rules.isACaptureP(board,
                                          coordinate.Coordinate(5, 5),
                                          6,
                                          True))
        self.assertFalse(rules.isACaptureP(board,
                                          coordinate.Coordinate(5, 5),
                                          8,
                                          True))


