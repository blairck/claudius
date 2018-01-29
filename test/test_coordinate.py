""" Unit tests for Coordinate class """

import unittest
from src import coordinate

class TestRules(unittest.TestCase):
    """ Tests for the coordinate module """

    def test_get_x_board(self):
        """ Get an X location in board notation """
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 4
        actual_result = board_location.get_x_board()
        self.assertEqual(actual_result, expected_result)

    def test_get_y_board(self):
        """ Get a Y location in board notation """
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 6
        actual_result = board_location.get_y_board()
        self.assertEqual(actual_result, expected_result)

    def test_get_x_array(self):
        """ Get an X location in array notation """
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 3
        actual_result = board_location.get_x_array()
        self.assertEqual(actual_result, expected_result)

    def test_get_y_array(self):
        """ Get a Y location in array notation """
        board_location = coordinate.Coordinate(4, 6)
        expected_result = 5
        actual_result = board_location.get_y_array()
        self.assertEqual(actual_result, expected_result)

    def test_coordinate_bad_x(self):
        """ Instantiate a coordinate with non-int X """
        self.assertRaises(TypeError, coordinate.Coordinate, "4", 6)

    def test_coordinate_bad_y(self):
        """ Instantiate a coordinate with non-int Y """
        self.assertRaises(TypeError, coordinate.Coordinate, 4, "6")

    def test_coordinate_bad_location(self):
        """ Instantiate a coordinate that is off the board """
        self.assertRaises(ValueError, coordinate.Coordinate, 50, 100)
