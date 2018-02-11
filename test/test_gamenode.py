""" Tests for the GameNode module """

import unittest

from test import helper
from src import coordinate
from src import gamenode

class TestGameNode(unittest.TestCase):
    """ Tests for the GameNode module """

    def test_default_instantiation(self):
        """ Test a known default instantiation """
        gn_obj = gamenode.GameNode()
        result = gn_obj.gameState[0][0]
        self.assertEqual(result, 0)
        self.assertFalse(gn_obj.leafP)
        self.assertFalse(gn_obj.rootP)
        self.assertFalse(gn_obj.score)

    def test_print_board(self):
        """Check that print_board works"""
        with helper.captured_output() as out:
            gn_obj = gamenode.GameNode()
            gn_obj.print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0\n"
                              "0  0  0  0  0  0  0  0  0  0")
            self.assertEqual(actual_print, expected_print)

    def test_getState(self):
        """ Check getting the board state at a Coordinate """
        gn_obj = gamenode.GameNode()
        self.assertEqual(gn_obj.getState(coordinate.Coordinate(3, 3)), 0)

    def test_setState(self):
        """ Test setting the board state at a Coordinate with a value """
        gn_obj = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(5, 1)
        testValue = 5
        gn_obj.setState(testCoordinate, testValue)
        self.assertEqual(gn_obj.getState(testCoordinate), testValue)

    def test_eq_same(self):
        """ Check equality function compares boards as equal """
        gn_obj_1 = gamenode.GameNode()
        gn_obj_2 = gamenode.GameNode()
        self.assertTrue(gn_obj_1 == gn_obj_2)

    def test_eq_not_same(self):
        """ Check equality function compares boards as not equal """
        gn_obj_1 = gamenode.GameNode()
        gn_obj_1.gameState[4][1] = 3
        gn_obj_2 = gamenode.GameNode()
        self.assertTrue(gn_obj_1 != gn_obj_2)
