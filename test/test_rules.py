""" Tests for the rules module """

import unittest
from unittest.mock import mock_open, patch
import unittest.mock as mock

# pylint: disable=import-error
from res import types
from src import coordinate
from src import gamenode
from src import rules

# pylint: disable=too-many-public-methods
class TestRules(unittest.TestCase):
    """ Tests for the rules module """

    def test_findConnectionP_nonexistant(self):
        """ FindConnectionP isn't able to find a connection """
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_up_right(self):
        """ FindConnectionP is able to find a connection """
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(4, 4)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_down_right(self):
        """ FindConnectionP is able to find a connection """
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(4, 2)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_down_left(self):
        """ FindConnectionP is able to find a connection """
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(2, 2)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists_up_left(self):
        """ FindConnectionP is able to find a connection """
        rules_obj = rules.Rules()
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(2, 4)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_backwards_PLAYER_A_REGULAR(self):
        """ PLAYER_A_REGULAR moving backwards returns false """
        rules_obj = rules.Rules()
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(3, 3)
        board.setState(startCoordinate, types.PLAYER_A_REGULAR)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_forwards_PLAYER_A_REGULAR(self):
        """ PLAYER_A_REGULAR moving forwards returns true """
        rules_obj = rules.Rules()
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(3, 5)
        board.setState(startCoordinate, types.PLAYER_A_REGULAR)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_forwards_disconnected_PLAYER_A_REGULAR(self):
        """ PLAYER_A_REGULAR moving forwards but not connected """
        rules_obj = rules.Rules()
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(3, 7)
        board.setState(startCoordinate, types.PLAYER_A_REGULAR)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_backwards_PLAYER_B_REGULAR(self):
        """ PLAYER_B_REGULAR moving backwards returns false """
        rules_obj = rules.Rules()
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(5, 5)
        board.setState(startCoordinate, types.PLAYER_B_REGULAR)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_forwards_PLAYER_B_REGULAR(self):
        """ PLAYER_B_REGULAR moving fowards returns true """
        rules_obj = rules.Rules()
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(5, 3)
        board.setState(startCoordinate, types.PLAYER_B_REGULAR)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
