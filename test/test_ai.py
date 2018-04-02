""" Tests for the AI module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
import main
from res import types
from src import ai
from src import coordinate
from src import gamenode
from test import helper

class TestAI(unittest.TestCase):
    """ Tests for the AI module """

    def test_getTupleOfAllCoordinates(self):
        actualResult = len(ai.getTupleOfAllCoordinates())
        expectedResult = 50
        self.assertEquals(actualResult, expectedResult)

    def test_getMovesForRegularPiece_2_moves(self):
        aiObject = ai.AI()
        gnObject = gamenode.GameNode()
        pieceLocation = coordinate.Coordinate(4, 4)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = aiObject.getMovesForRegularPiece(gnObject,
                                                        pieceLocation,
                                                        True)
        expectedResultLength = 2
        self.assertEquals(len(actualResult), expectedResultLength)

    def test_getMovesForRegularPiece_1_move(self):
        aiObject = ai.AI()
        gnObject = gamenode.GameNode()
        pieceLocation = coordinate.Coordinate(10, 4)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = aiObject.getMovesForRegularPiece(gnObject,
                                                        pieceLocation,
                                                        True)
        expectedResultLength = 1
        self.assertEquals(len(actualResult), expectedResultLength)

    def test_getMovesForRegularPiece_0_moves(self):
        aiObject = ai.AI()
        gnObject = main.createStartingPosition()
        pieceLocation = coordinate.Coordinate(1, 1)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = aiObject.getMovesForRegularPiece(gnObject,
                                                        pieceLocation,
                                                        True)
        expectedResultLength = 0
        self.assertEquals(len(actualResult), expectedResultLength)

    def test_destinationIsEmpty_true(self):
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(4, 6)
        actualResult = ai.destinationIsEmpty(gnObject, pieceDestination)
        expectedResult = True
        self.assertEquals(actualResult, expectedResult)

    def test_destinationIsEmpty_false(self):
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(9, 3)
        gnObject.setState(pieceDestination, types.PLAYER_A_REGULAR)
        actualResult = ai.destinationIsEmpty(gnObject, pieceDestination)
        expectedResult = False
        self.assertEquals(actualResult, expectedResult)

    def test_makePieceMove_good(self):
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
        self.assertEquals(actualResultLocationType, expectedResultLocationType)
        self.assertEquals(actualResultDestinationType,
                          expectedResultDestinationType)

    def test_getAllMovesForPlayer_isPlayerA(self):
        aiObject = ai.AI()
        gnObject = main.createStartingPosition()
        actualResult = aiObject.getAllMovesForPlayer(gnObject, True)
        expectedResultLength = 9
        self.assertEquals(len(actualResult), expectedResultLength)

    def test_getAllMovesForPlayer_isPlayerB(self):
        aiObject = ai.AI()
        gnObject = main.createStartingPosition()
        actualResult = aiObject.getAllMovesForPlayer(gnObject, False)
        expectedResultLength = 9
        self.assertEquals(len(actualResult), expectedResultLength)

    def test_getAllMovesForPlayer_1_move_2_players(self):
        # Given
        aiObject = ai.AI()
        gnObject = gamenode.GameNode()
        pieceLocationA = coordinate.Coordinate(6, 2)
        gnObject.setState(pieceLocationA, types.PLAYER_A_REGULAR)
        pieceLocationB = coordinate.Coordinate(5, 7)
        gnObject.setState(pieceLocationB, types.PLAYER_B_REGULAR)

        # When
        actualResult = aiObject.getAllMovesForPlayer(gnObject, False)
        for item in actualResult:
            item.print_board()

        # Then
        expectedResultLength = 2
        self.assertEquals(len(actualResult), expectedResultLength)
