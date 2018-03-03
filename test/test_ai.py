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
