""" Tests for the AI module """

import unittest

# pylint: disable=import-error
import helper
from res import types
from src import ai
from src import coordinate
from src import gamenode

class TestAI(unittest.TestCase):
    """ Tests for the AI module """

    def test_getTupleOfAllCoordinates(self):
        """ Check that all the legal coordinates are generated """
        actualResult = len(ai.getTupleOfAllCoordinates())
        expectedResult = 50
        self.assertEqual(actualResult, expectedResult)

    def test_getAllMovesForPlayer_good(self):
        board_description = [
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     .     .     . 0",
            "9 .     .     .     .     .    9",
            "8    .     .     .     .     . 8",
            "7 .     .     .     .     .    7",
            "6    .     b     .     .     . 6",
            "5 .     .     a     a     .    5",
            "4    .     .     .     .     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",]
        board = helper.parse_board_input(board_description)
        #capturingPiece = coordinate.Coordinate(3, 5)

        expectedLength = 1
        movesList = ai.getAllMovesForPlayer(board, True)

        actualMovesListLength = len(movesList)

        self.assertEqual(expectedLength, actualMovesListLength)

    def test_getNoncaptureMovesForRegularPiece_2_moves(self):
        """ Test that regular piece has to possible moves """
        gnObject = gamenode.GameNode()
        pieceLocation = coordinate.Coordinate(4, 4)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = ai.getNoncaptureMovesForRegularPiece(gnObject,
                                                            pieceLocation,
                                                            True)
        expectedResultLength = 2
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getNoncaptureMovesForRegularPiece_1_move(self):
        """ Test regular piece on the edge of the board, which has 1 move """
        gnObject = gamenode.GameNode()
        pieceLocation = coordinate.Coordinate(10, 4)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = ai.getNoncaptureMovesForRegularPiece(gnObject,
                                                            pieceLocation,
                                                            True)
        expectedResultLength = 1
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getNoncaptureMovesForRegularPiece_0_moves(self):
        """ Test regular piece that is completely blocked from moving """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        pieceLocation = coordinate.Coordinate(1, 1)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = ai.getNoncaptureMovesForRegularPiece(gnObject,
                                                            pieceLocation,
                                                            True)
        expectedResultLength = 0
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_destinationIsEmpty_true(self):
        """ Test when destination is Empty """
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(4, 6)
        actualResult = ai.destinationIsEmpty(gnObject, pieceDestination)
        expectedResult = True
        self.assertEqual(actualResult, expectedResult)

    def test_destinationIsEmpty_false(self):
        """ Test when destination is not Empty """
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(9, 3)
        gnObject.setState(pieceDestination, types.PLAYER_A_REGULAR)
        actualResult = ai.destinationIsEmpty(gnObject, pieceDestination)
        expectedResult = False
        self.assertEqual(actualResult, expectedResult)

    def test_makePieceMove_good(self):
        """ Test executing a happy-path piece move """
        # Given
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(9, 3)
        pieceLocation = coordinate.Coordinate(8, 2)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)

        # When
        actualResult = ai.makePieceMove(gnObject,
                                        pieceDestination,
                                        pieceLocation)

        # Then
        actualResultLocationType = actualResult.getState(pieceLocation)
        actualResultDestinationType = actualResult.getState(pieceDestination)
        expectedResultLocationType = types.EMPTY
        expectedResultDestinationType = types.PLAYER_A_REGULAR
        self.assertEqual(actualResultLocationType, expectedResultLocationType)
        self.assertEqual(actualResultDestinationType,
                         expectedResultDestinationType)

    def test_getAllMovesForPlayer_isPlayerA(self):
        """ Test getting all moves for player A """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        actualResult = ai.getAllMovesForPlayer(gnObject, True)
        expectedResultLength = 9
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getAllMovesForPlayer_isPlayerB(self):
        """ Test getting all moves for player B """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        actualResult = ai.getAllMovesForPlayer(gnObject, False)
        expectedResultLength = 9
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getAllMovesForPlayer_1_move_2_players(self):
        """ Test getting moves for a particular player when both players have
        legal moves """
        # Given
        gnObject = gamenode.GameNode()
        pieceLocationA = coordinate.Coordinate(6, 2)
        gnObject.setState(pieceLocationA, types.PLAYER_A_REGULAR)
        pieceLocationB = coordinate.Coordinate(5, 7)
        gnObject.setState(pieceLocationB, types.PLAYER_B_REGULAR)

        # When
        actualResult = ai.getAllMovesForPlayer(gnObject, False)

        # Then
        expectedResultLength = 2
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getCapturesForRegularPiece_good(self):
        board_description = [
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     .     .     . 0",
            "9 .     .     .     .     .    9",
            "8    .     .     B     b     . 8",
            "7 .     .     .     .     .    7",
            "6    A     b     b     b     . 6",
            "5 .     a     .     .     .    5",
            "4    a     B     .     b     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",]
        board = helper.parse_board_input(board_description)
        capturingPiece = coordinate.Coordinate(3, 5)

        expectedLength = 2
        movesList = ai.getCapturesForRegularPiece(board,
                                                  capturingPiece,
                                                  True)
        for item in movesList:
            item.print_board()
        actualMovesListLength = len(movesList)

        self.assertEqual(expectedLength, actualMovesListLength)

        # for move in actualMovesList:
        #     move.print_board()

        # TODO Finish these tests
        # assert starting position is empty
        # assert (4,6), (6,8), (8,8), (8,6) are empty
        # case 1: pieceA ends in (9,3). (8,4) empty. pieceB is present in (6,6).
        # case 2: pieceA ends in (5,7). (6,6) empty. pieceB is present in (8,4).
        # assert length of results is 2
