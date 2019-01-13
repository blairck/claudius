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

    def test_countPlayerPieces_player_A(self):
        """ Count player A pieces """
        board = helper.parse_board_input(helper.simpleCaptureBoardDescription)

        playerPieces = (types.PLAYER_A_REGULAR, types.PLAYER_A_KING)
        expectedResult = 2

        actualResult = board.countPlayerPieces(playerPieces)
        self.assertEqual(actualResult, expectedResult)

    def test_countPlayerPieces_player_B(self):
        """ Count player B pieces """
        board = helper.parse_board_input(helper.simpleCaptureBoardDescription)

        playerPieces = (types.PLAYER_B_REGULAR, types.PLAYER_B_KING)
        expectedResult = 1

        actualResult = board.countPlayerPieces(playerPieces)
        self.assertEqual(actualResult, expectedResult)

    def test_countPlayerPieces_nonexistant(self):
        """ Count pieces that don't exist """
        board = helper.parse_board_input(helper.simpleCaptureBoardDescription)
        nonexistantPieceType = 99

        playerPieces = (nonexistantPieceType,)
        expectedResult = 0

        actualResult = board.countPlayerPieces(playerPieces)
        self.assertEqual(actualResult, expectedResult)

    def test_getPieceCount_bad_unassigned(self):
        """ Handle unknown player type """
        gnObject = gamenode.GameNode()
        self.assertRaises(ValueError, gnObject.getPieceCount, None)

    def test_getPieceCount_good_playerA(self):
        """ Count player A pieces, cached and uncached """
        board = helper.parse_board_input(helper.simpleCaptureBoardDescription)

        playerAToPlay = True
        expectedResult = 2

        # Assert uncached value and result
        self.assertFalse(board.numberOfPiecesForA)
        actualResult = board.getPieceCount(playerAToPlay)
        self.assertEqual(actualResult, expectedResult)

        # Assert cached value
        self.assertEqual(board.numberOfPiecesForA, expectedResult)
        actualResult = board.getPieceCount(playerAToPlay)
        self.assertEqual(actualResult, expectedResult)

    def test_getPieceCount_good_playerB(self):
        """ Count player B pieces, cached and uncached """
        board = helper.parse_board_input(helper.simpleCaptureBoardDescription)

        playerAToPlay = False
        expectedResult = 1

        # Assert uncached value and result
        self.assertFalse(board.numberOfPiecesForB)
        actualResult = board.getPieceCount(playerAToPlay)
        self.assertEqual(actualResult, expectedResult)

        # Assert cached value
        self.assertEqual(board.numberOfPiecesForB, expectedResult)
        actualResult = board.getPieceCount(playerAToPlay)
        self.assertEqual(actualResult, expectedResult)
