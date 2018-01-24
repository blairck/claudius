""" Tests for the GameNode module """

import unittest

from src import gamenode
from test import helper

class TestGameNode(unittest.TestCase):
    """ Tests for the GameNode module """

    def test_default_instantiation(self):
        """ Test a known default instantiation """
        gn_obj = gamenode.GameNode()
        result = gn_obj.gameState[0][0]
        self.assertEqual(result, -1)
        self.assertFalse(gn_obj.leafP)
        self.assertFalse(gn_obj.rootP)
        self.assertFalse(gn_obj.score)

    def test_print_board(self):
        """Check that print_board works"""
        with helper.captured_output() as out:
            gn_obj = gamenode.GameNode()
            gn_obj.print_board()
            actual_print = out.getvalue().strip()
            expected_print = ("000   \n"
                              "   000   \n"
                              "0000000\n"
                              "0000000\n"
                              "0000000\n"
                              "   000   \n"
                              "   000")
            self.assertEqual(actual_print, expected_print)

    def test_print_middle_rows_without_seperator(self):
        """ Check that print_middle_rows() works without seperator """
        with helper.captured_output() as out:
            gn_obj = gamenode.GameNode()
            gn_obj.print_middle_rows()
            actual_print = out.getvalue().strip()
            expected_print = ("0000000\n"
                              "0000000\n"
                              "0000000")
            self.assertEqual(actual_print, expected_print)

    def test_print_middle_rows_with_seperator(self):
        """ Check that print_middle_rows() works with a seperator """
        with helper.captured_output() as out:
            gn_obj = gamenode.GameNode()
            gn_obj.print_middle_rows(1)
            actual_print = out.getvalue().strip()
            expected_print = ("0101010101010\n"
                              "0101010101010\n"
                              "0101010101010")
            self.assertEqual(actual_print, expected_print)
