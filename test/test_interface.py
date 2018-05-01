""" Tests for the AI module """

import unittest
from unittest.mock import patch

# pylint: disable=import-error
from res import types
from src import ai
from src import coordinate
from src import interface
from test import helper

class TestInterface(unittest.TestCase):
    """ Integration Tests for the Interface module """

    # pylint: disable=too-many-public-methods
    # Never too many tests

    @classmethod
    def setUpClass(cls):
        cls.shared_game = helper.nearlyWonGooseGame
        cls.looped_capture = helper.loopedFoxCapture

    @patch.object(interface, "matchSingleCoordinateToMoves")
    def test_getPositionFromListOfMoves_single(self,
                                               mock_matchSingleCoordinateTo):
        """ Get position from list of moves with a single coordinate string
        input """
        mock_matchSingleCoordinateTo.return_value = ["fake board1"]
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        result = interface.getPositionFromListOfMoves(self.shared_game,
                                                      listOfMoves,
                                                      '53',
                                                      gooseP)
        self.assertEqual(len(result), 1)

    @patch.object(interface, "matchMultipleCoordinatesToMoves")
    def test_getPositionFromListOfMoves_multi(self,
                                              mock_matchMultipleCoordinatesTo):
        """ Get position from list of moves with a multi coordinate string
        input """
        mock_matchMultipleCoordinatesTo.return_value = ["fake_board1",
                                                        "fake_board2"]
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        result = interface.getPositionFromListOfMoves(self.shared_game,
                                                      listOfMoves,
                                                      '5363',
                                                      gooseP)
        self.assertEqual(len(result), 2)

    def test_getPositionFromListOfMoves_none(self):
        """ Gets a simple position from a list of moves where none exist """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        result = interface.getPositionFromListOfMoves(self.shared_game,
                                                      listOfMoves,
                                                      'z1',
                                                      gooseP)
        self.assertEqual(len(result), 0)

    def test_getPositionFromListOfMoves_ambiguous(self):
        r""" Gets a move from an ambiguous board state
        7         G - . - .
                  | \ | / |
        6         . - G - G
                  | / | \ |
        5 G - G - G - . - . - G - G
          | \ | / | \ | / | \ | / |
        4 . - G - . - . - . - G - G
          | / | \ | / | \ | / | \ |
        3 G - . - . - . - . - G - G
                  | \ | / |
        2         F - . - F
                  | / | \ |
        1         S - S - S
          1   2   3   4   5   6   7
        """
        hnObject = gamenode.GameNode()
        hnObject.setState(coordinate.Coordinate(3, 2), types.FOX)
        hnObject.setState(coordinate.Coordinate(5, 2), types.FOX)
        hnObject.setState(coordinate.Coordinate(3, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(1, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(2, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(2, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(1, 3), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 7), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(4, 6), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(5, 6), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(6, 3), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(6, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(6, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(7, 3), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(7, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(7, 5), types.GOOSE)
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(hnObject, gooseP)
        result = interface.getPositionFromListOfMoves(hnObject,
                                                      listOfMoves,
                                                      "4544",
                                                      gooseP)
        self.assertEqual(len(result), 0)

    def test_getPositionFromListOfMoves_bugged(self):
        r""" Gets a move from an ambiguous board state
        7         . - . - .
                  | \ | / |
        6         . - . - .
                  | / | \ |
        5 . - . - . - . - . - . - G
          | \ | / | \ | / | \ | / |
        4 . - F - . - . - F - . - G
          | / | \ | / | \ | / | \ |
        3 G - . - . - . - S - . - G
                  | \ | / |
        2         S - S - S
                  | / | \ |
        1         . - . - S
          A   B   C   D   E   F   G
        Fox to play. Test based on a bug:
        'Enter a move: e4d4
        Unknown or invalid move, please try again'
        """
        hnObject = gamenode.GameNode()
        hnObject.setState(coordinate.Coordinate(7, 5), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(2, 4), types.FOX)
        hnObject.setState(coordinate.Coordinate(5, 4), types.FOX)
        hnObject.setState(coordinate.Coordinate(7, 4), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(1, 3), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(5, 3), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(7, 3), types.GOOSE)
        hnObject.setState(coordinate.Coordinate(3, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(4, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 2), types.SUPERGOOSE)
        hnObject.setState(coordinate.Coordinate(5, 1), types.SUPERGOOSE)
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(hnObject, gooseP)
        result = interface.getPositionFromListOfMoves(hnObject,
                                                      listOfMoves,
                                                      "e4d4",
                                                      gooseP)
        self.assertEqual(len(result), 1)
        start = coordinate.Coordinate(5, 4)
        end = coordinate.Coordinate(4, 4)
        self.assertEqual(result[0].getState(start), types.EMPTY)
        self.assertEqual(result[0].getState(end), types.FOX)

    def test_getPositionFromListOfMoves_loop(self):
        """ Test getting position from user input when fox captures loop """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.looped_capture,
                                                    gooseP)
        result = interface.getPositionFromListOfMoves(self.looped_capture,
                                                      listOfMoves,
                                                      '42',
                                                      gooseP)
        self.assertEqual(len(result), 1)

    def test_matchSingleCoordinateToMoves_fox_unambiguous(self):
        """ Match coordinate where there is exactly one match """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 5)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEqual(len(actualValue), 1)

    def test_matchSingleCoordinateToMoves_fox_ambiguous(self):
        """ Match coordinate to moves when there are 2 matches """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 4)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEqual(len(actualValue), 2)

    def test_matchSingleCoordinateToMoves_fox_none(self):
        """ Match coordinate to moves where there is no match """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        testCoordinate = coordinate.Coordinate(6, 3)
        actualValue = interface.matchSingleCoordinateToMoves(listOfMoves,
                                                             testCoordinate,
                                                             gooseP)
        self.assertEqual(len(actualValue), 0)

    def test_matchMultipleCoordinatesToMoves_goose_unambiguous(self):
        """ Match multi-coordinate goose input to move """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        coordinates = interface.getCoordinatesFromUserInput("25-35")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        self.assertEqual(len(actualValue), 1)

    def test_matchMultipleCoordinatesToMoves_goose_more_unambiguous(self):
        """ Match multi-coordinate goose input to move """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        coordinates = interface.getCoordinatesFromUserInput("4233")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        for item in listOfMoves:
            item.pretty_print_board()
        self.assertEqual(len(actualValue), 1)

    def test_matchMultipleCoordinatesToMoves_goose_nonexistant(self):
        """ Get coordinates from moves where there are none """
        aiObject = ai.AI()
        gooseP = True
        listOfMoves = aiObject.getAllMovesForPlayer(self.shared_game, gooseP)
        coordinates = interface.getCoordinatesFromUserInput("54-55")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        self.assertEqual(len(actualValue), 0)

    def test_matchMultipleCoordinatesToMoves_fox_ambiguous_short(self):
        """ Test for single result from multiple coordinates """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.looped_capture,
                                                    gooseP)
        coordinates = interface.getCoordinatesFromUserInput("42-64")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        for item in actualValue:
            item.pretty_print_board()
        self.assertEqual(len(actualValue), 1)

    def test_matchMultipleCoordinatesToMoves_fox_ambiguous_long(self):
        """ Test for single result from a long series of coordinates """
        aiObject = ai.AI()
        gooseP = False
        listOfMoves = aiObject.getAllMovesForPlayer(self.looped_capture,
                                                    gooseP)
        coordinates = interface.getCoordinatesFromUserInput("42-24-46-64")
        actualValue = interface.matchMultipleCoordinatesToMoves(listOfMoves,
                                                                coordinates,
                                                                gooseP)
        self.assertEqual(len(actualValue), 1)


    def test_getCoordinatesFromUserInput_good(self):
        """ Get coordinates from good input """
        actualValue = interface.getCoordinatesFromUserInput('34')[0]
        expectedValue = coordinate.Coordinate(3, 4)
        self.assertEqual(actualValue.get_x_board(),
                         expectedValue.get_x_board())
        self.assertEqual(actualValue.get_y_board(),
                         expectedValue.get_y_board())

    def test_getCoordinatesFromUserInput_good_with_comma(self):
        """ Get coordinates from good input with comma """
        actualValue = interface.getCoordinatesFromUserInput('3,4')[0]
        expectedValue = coordinate.Coordinate(3, 4)
        self.assertEqual(actualValue.get_x_board(),
                         expectedValue.get_x_board())
        self.assertEqual(actualValue.get_y_board(),
                         expectedValue.get_y_board())

    def test_getCoordinatesFromUserInput_long(self):
        """ Get coordinates from a long input """
        actualValue = interface.getCoordinatesFromUserInput('3,4-5,6')
        expectedValue0 = coordinate.Coordinate(3, 4)
        expectedValue1 = coordinate.Coordinate(5, 6)
        self.assertEqual(actualValue[0].get_x_board(),
                         expectedValue0.get_x_board())
        self.assertEqual(actualValue[1].get_y_board(),
                         expectedValue1.get_y_board())

    def test_getCoordinatesFromUserInput_long_simple(self):
        """ Get coordinates from a long input without extra notation """
        actualValue = interface.getCoordinatesFromUserInput('3456')
        expectedValue0 = coordinate.Coordinate(3, 4)
        expectedValue1 = coordinate.Coordinate(5, 6)
        self.assertEqual(actualValue[0].get_x_board(),
                         expectedValue0.get_x_board())
        self.assertEqual(actualValue[1].get_y_board(),
                         expectedValue1.get_y_board())

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

    def test_isCoordinateMatch_goose(self):
        """ Test coordinate match with goose """
        hnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = True
        hnObject.setState(testCoordinate, types.SUPERGOOSE)
        self.assertTrue(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))

    def test_isCoordinateMatch_fox(self):
        """ Test coordinate match with fox """
        hnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = False
        hnObject.setState(testCoordinate, types.FOX)
        self.assertTrue(interface.isCoordinateMatch(hnObject,
                                                    testCoordinate,
                                                    gooseP))

    def test_isCoordinateMatch_empty(self):
        """ Test coordinate match when it's empty """
        hnObject = gamenode.GameNode()
        testCoordinate = coordinate.Coordinate(3, 7)
        gooseP = False
        self.assertFalse(interface.isCoordinateMatch(hnObject,
                                                     testCoordinate,
                                                     gooseP))

    def test_parseAlphabetNotation_simple(self):
        """ Parse a simple valid alphabetnotation input """
        actualValue = interface.parseAlphabetNotation("a3b3")
        self.assertEqual(actualValue, "1323")

    def test_parseAlphabetNotation_mixed(self):
        """ Parse a simple valid alphabetnotation input """
        actualValue = interface.parseAlphabetNotation("a323")
        self.assertEqual(actualValue, "1323")
