""" Tests for the AI module """

import unittest

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import gamenode
from src import interface

class TestInterface(unittest.TestCase):
    """ Integration Tests for the Interface module """

    def test_getPositionFromListOfMoves_single(self):
        """ Test getting position from single possible user input """
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        listOfMoves = ai.getAllMovesForPlayer(gnObject, not userIsPlayerB)
        actualValue = interface.getPositionFromListOfMoves(gnObject,
                                                           listOfMoves,
                                                           "06",
                                                           userIsPlayerB)
        self.assertEqual(len(actualValue), 1)

    def test_getPositionFromListOfMoves_multiple(self):
        """ Test getting position from single possible user input """
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        listOfMoves = ai.getAllMovesForPlayer(gnObject, not userIsPlayerB)
        actualValue = interface.getPositionFromListOfMoves(gnObject,
                                                           listOfMoves,
                                                           "7786",
                                                           userIsPlayerB)
        self.assertEqual(len(actualValue), 1)

    def test_getPositionFromListOfMoves_none(self):
        """ Test getting position from single possible user input """
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        listOfMoves = ai.getAllMovesForPlayer(gnObject, not userIsPlayerB)
        actualValue = interface.getPositionFromListOfMoves(gnObject,
                                                           listOfMoves,
                                                           "7775",
                                                           userIsPlayerB)
        self.assertEqual(len(actualValue), 0)


    def test_matchSingleCoordinateToMoves_playerB(self):
        """ Match multi-coordinate playerB input to move """
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        listOfMoves = ai.getAllMovesForPlayer(gnObject, not userIsPlayerB)
        coordinates = interface.getCoordinatesFromUserInput("06")[0]
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             coordinates,
                                                             userIsPlayerB)
        self.assertEqual(len(actualValue), 1)

    def test_matchMultipleCoordinatesToMoves_playerB_unambiguous(self):
        """ Match multi-coordinate playerB input to move """
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        listOfMoves = ai.getAllMovesForPlayer(gnObject, not userIsPlayerB)
        coordinates = interface.getCoordinatesFromUserInput("3746")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                userIsPlayerB)
        self.assertEqual(len(actualValue), 1)

    def test_isCoordinateMatch_player_A_good(self):
        """ Test coordinate match with user as player A """
        userIsPlayerB = False
        gnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gnObject.setState(testCoordinate, types.PLAYER_A_REGULAR)
        self.assertTrue(interface.isCoordinateMatch(gnObject,
                                                    testCoordinate,
                                                    userIsPlayerB))

    def test_isCoordinateMatch_player_A_no_match(self):
        """ Test coordinate no match with user as player A """
        userIsPlayerB = False
        gnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        self.assertFalse(interface.isCoordinateMatch(gnObject,
                                                     testCoordinate,
                                                     userIsPlayerB))

    def test_isCoordinateMatch_player_B_good(self):
        """ Test coordinate match with user as player B """
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gnObject.setState(testCoordinate, types.PLAYER_B_REGULAR)
        self.assertTrue(interface.isCoordinateMatch(gnObject,
                                                    testCoordinate,
                                                    userIsPlayerB))

    def test_isCoordinateMatch_player_B_wrong_piece(self):
        """ Test coordinate match with user as player B but destination does
        not match"""
        userIsPlayerB = True
        gnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gnObject.setState(testCoordinate, types.PLAYER_A_REGULAR)
        self.assertFalse(interface.isCoordinateMatch(gnObject,
                                                     testCoordinate,
                                                     userIsPlayerB))

    def test_getCoordinatesFromUserInput_good(self):
        """ Get coordinates from good input """
        actualValue = interface.getCoordinatesFromUserInput('33')[0]
        expectedValue = coordinate.Coordinate(3, 3)
        self.assertCoordinatesMatch(actualValue, expectedValue)

    def test_getCoordinatesFromUserInput_good_with_comma(self):
        """ Get coordinates from good input with comma """
        actualValue = interface.getCoordinatesFromUserInput('8,6')[0]
        expectedValue = coordinate.Coordinate(8, 6)
        self.assertCoordinatesMatch(actualValue, expectedValue)

    def test_getCoordinatesFromUserInput_long(self):
        """ Get coordinates from a long input """
        actualValue = interface.getCoordinatesFromUserInput('9,7-0,8')
        expectedValue0 = coordinate.Coordinate(9, 7)
        expectedValue1 = coordinate.Coordinate(10, 8)
        self.assertCoordinatesMatch(actualValue[0], expectedValue0)
        self.assertCoordinatesMatch(actualValue[1], expectedValue1)

    def test_getCoordinatesFromUserInput_long_simple(self):
        """ Get coordinates from a long input without extra notation """
        actualValue = interface.getCoordinatesFromUserInput('4637')
        expectedValue0 = coordinate.Coordinate(4, 6)
        expectedValue1 = coordinate.Coordinate(3, 7)
        self.assertCoordinatesMatch(actualValue[0], expectedValue0)
        self.assertCoordinatesMatch(actualValue[1], expectedValue1)

    def test_getCoordinatesFromUserInput_very_long(self):
        """ Get coordinates from a long input without extra notation """
        actualValue = interface.getCoordinatesFromUserInput("42-24-46-64")
        self.assertEqual(len(actualValue), 4)

    def test_getCoordinatesFromUserInput_bad_short(self):
        """ Parse a short bad input string """
        actualValue = interface.getCoordinatesFromUserInput('3')
        self.assertEqual(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_bad_long(self):
        """ Parse a long bad input string """
        actualValue = interface.getCoordinatesFromUserInput('345t')
        self.assertEqual(len(actualValue), 0)

    def test_getCoordinatesFromUserInput_outside_long(self):
        """ Parse an input string outside the board """
        actualValue = interface.getCoordinatesFromUserInput('3459')
        self.assertEqual(len(actualValue), 0)

    def test_userInputCharacterFor10thAxis_10th_axis(self):
        """ Parse an input for 10th axis """
        actualValue = interface.userInputCharacterFor10thAxis("0")
        self.assertEqual(actualValue, 10)

    def test_userInputCharacterFor10thAxis_other_axis(self):
        """ Parse an input for 10th axis """
        actualValue = interface.userInputCharacterFor10thAxis("6")
        self.assertEqual(actualValue, 6)

    # Helper validation functions
    def assertCoordinatesMatch(self, actualCoordinate, expectedCoordinate):
        """ Verify that coordinate objects are the same """
        self.assertEqual(actualCoordinate.get_x_board(),
                         expectedCoordinate.get_x_board())
        self.assertEqual(actualCoordinate.get_y_board(),
                         expectedCoordinate.get_y_board())
