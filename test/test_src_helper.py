""" Tests for the helper module """

import unittest

from src import helper

class TestHelper(unittest.TestCase):
    """ Tests for the helper module """
    def test_checkIfInt_good(self):
        """ Check that checkIfInt correctly assesses an input """
        self.assertFalse(helper.checkIfInt(123))

    def test_checkIfInt_bad(self):
        """ Check that checkIfInt raises an error with non-int input """
        self.assertRaises(TypeError, helper.checkIfInt, "abc")

    def test_checkIfCoordinateIsValid_good_x(self):
        """ Check that checkIfCoordinateIsValid is False """
        self.assertTrue(helper.checkIfCoordinateIsValid(1, 3))

    def test_checkIfCoordinateIsValid_good_y(self):
        """ Check that checkIfCoordinateIsValid is False """
        self.assertTrue(helper.checkIfCoordinateIsValid(6, 0))

    def test_checkIfCoordinateIsValid_bad_x(self):
        """ Check that checkIfCoordinateIsValid is False """
        self.assertFalse(helper.checkIfCoordinateIsValid(9, 6))

    def test_checkIfCoordinateIsValid_bad_y(self):
        """ Check that checkIfCoordinateIsValid is False """
        self.assertFalse(helper.checkIfCoordinateIsValid(4, 1))

    def test_checkIfCoordinateIsValid_bad_outside(self):
        """ Check that checkIfCoordinateIsValid is False """
        self.assertFalse(helper.checkIfCoordinateIsValid(40, 30))
