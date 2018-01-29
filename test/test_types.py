""" Tests for the Types module """

import unittest

# pylint: disable=import-error
from res import types

class TestTypes(unittest.TestCase):
    """ Tests for the Types module """

    def test_getPieceAbbreviation_OFF_BOARD(self):
        "Correctly convert a type to a character for display"
        self.assertEqual("   ", types.getPieceAbbreviation(types.OFF_BOARD))

    def test_getPieceAbbreviation_EMPTY(self):
        "Correctly convert a type to a character for display"
        self.assertEqual("|||", types.getPieceAbbreviation(types.EMPTY))

    def test_getPieceAbbreviation_PLAYER_A_REGULAR(self):
        "Correctly convert a type to a character for display"
        self.assertEqual("|a|",
                         types.getPieceAbbreviation(types.PLAYER_A_REGULAR))

    def test_getPieceAbbreviation_PLAYER_A_KING(self):
        "Correctly convert a type to a character for display"
        self.assertEqual("|A|",
                         types.getPieceAbbreviation(types.PLAYER_A_KING))

    def test_getPieceAbbreviation_PLAYER_B_REGULAR(self):
        "Correctly convert a type to a character for display"
        self.assertEqual("|b|",
                         types.getPieceAbbreviation(types.PLAYER_B_REGULAR))

    def test_getPieceAbbreviation_PLAYER_B_KING(self):
        "Correctly convert a type to a character for display"
        self.assertEqual("|B|",
                         types.getPieceAbbreviation(types.PLAYER_B_KING))

    def test_getPieceAbbreviation_invalid(self):
        "Correctly convert a type to a character for display"
        self.assertRaises(ValueError,
                          types.getPieceAbbreviation,
                          'abcd')
