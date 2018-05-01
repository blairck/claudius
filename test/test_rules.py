""" Tests for the rules module """

import unittest
from unittest.mock import mock_open, patch
import unittest.mock as mock

# pylint: disable=import-error
from res import types
from src import coordinate
from src import gamenode
from src import rules

# pylint: disable=too-many-public-methods
class TestRules(unittest.TestCase):
    """ Tests for the rules module """

    def test_makeCapture_horizontal(self):
        """ Correctly update board with horizontal capture """
        # Given
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(3, 4)
        captureCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(5, 4)
        board.setState(startCoordinate, types.FOX)
        board.setState(captureCoordinate, types.GOOSE)

        # When
        rules.makeCapture(board, startCoordinate, endCoordinate)

        # Assert
        actualValue = board.getState(startCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(captureCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(endCoordinate)
        self.assertEqual(actualValue, 2)

    def test_makeCapture_vertical(self):
        """ Correctly update board with vertical capture """
        # Given
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(4, 4)
        captureCoordinate = coordinate.Coordinate(4, 5)
        endCoordinate = coordinate.Coordinate(4, 6)
        board.setState(startCoordinate, types.FOX)
        board.setState(captureCoordinate, types.GOOSE)

        # When
        rules.makeCapture(board, startCoordinate, endCoordinate)

        # Assert
        actualValue = board.getState(startCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(captureCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(endCoordinate)
        self.assertEqual(actualValue, 2)

    def test_makeCapture_diagonal(self):
        """ Correctly update board with diagonal capture """
        # Given
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(3, 4)
        captureCoordinate = coordinate.Coordinate(4, 5)
        endCoordinate = coordinate.Coordinate(5, 6)
        board.setState(startCoordinate, types.FOX)
        board.setState(captureCoordinate, types.GOOSE)

        # When
        rules.makeCapture(board, startCoordinate, endCoordinate)

        # Assert
        actualValue = board.getState(startCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(captureCoordinate)
        self.assertEqual(actualValue, 0)
        actualValue = board.getState(endCoordinate)
        self.assertEqual(actualValue, 2)

    def test_makeCapture_horizontal_bad_x(self):
        """ Correctly handle a bad X ending coordinate """
        # Given
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(3, 4)
        captureCoordinate = coordinate.Coordinate(4, 4)
        endCoordinate = coordinate.Coordinate(6, 4)
        board.setState(startCoordinate, types.FOX)
        board.setState(captureCoordinate, types.GOOSE)

        # When/Assert
        self.assertRaises(ValueError,
                          rules.makeCapture,
                          board,
                          startCoordinate,
                          endCoordinate)

    def test_makeCapture_horizontal_bad_y(self):
        """ Correctly handle a bad Y ending coordinate """
        # Given
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(3, 3)
        captureCoordinate = coordinate.Coordinate(3, 5)
        endCoordinate = coordinate.Coordinate(3, 6)
        board.setState(startCoordinate, types.FOX)
        board.setState(captureCoordinate, types.GOOSE)

        # When/Assert
        self.assertRaises(ValueError,
                          rules.makeCapture,
                          board,
                          startCoordinate,
                          endCoordinate)

    def test_makeCapture_horizontal_same_coordinates(self):
        """ Correctly handle capture over the same coordinate """
        # Given
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(3, 3)
        captureCoordinate = coordinate.Coordinate(3, 5)
        board.setState(startCoordinate, types.FOX)
        board.setState(captureCoordinate, types.GOOSE)

        # When/Assert
        self.assertRaises(ValueError,
                          rules.makeCapture,
                          board,
                          startCoordinate,
                          startCoordinate)

    def test_findDirection_1(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(5, 7)
        expected_result = 1
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_2(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(3, 3)
        endCoordinate = coordinate.Coordinate(5, 5)
        expected_result = 2
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_3(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(7, 5)
        expected_result = 3
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_4(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(7, 3)
        expected_result = 4
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_5(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(5, 3)
        expected_result = 5
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_6(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 3)
        expected_result = 6
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_7(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 5)
        expected_result = 7
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_8(self):
        """ Find direction between two adjacent coordinates """
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 7)
        expected_result = 8
        actual_result = rules.findDirection(startCoordinate, endCoordinate)
        self.assertEqual(actual_result, expected_result)

    def test_findDirection_bad(self):
        """ Coordinates are not adjacent, so don't have an associated
         direction """
        startCoordinate = coordinate.Coordinate(4, 4)
        self.assertRaises(ValueError,
                          rules.findDirection,
                          startCoordinate,
                          startCoordinate)

    def test_convertCharToInt_good_value_1(self):
        """ Test a known good value"""
        result = rules.convertCharToInt('1')
        self.assertEqual(result, 1)

    def test_convertCharToInt_good_value_3(self):
        """ Test a known good value"""
        result = rules.convertCharToInt('3')
        self.assertEqual(result, 3)

    def test_convertCharToInt_upper_value_10(self):
        """ Test a value that should be too high"""
        self.assertRaises(ValueError, rules.convertCharToInt, '10')

    def test_convertCharToInt_lower_value_5(self):
        """ Test a value that should be too low"""
        self.assertRaises(ValueError, rules.convertCharToInt, '-5')

    def test_convertCharToInt_bad_value(self):
        """ Test a value that isn't an int"""
        self.assertRaises(ValueError, rules.convertCharToInt, 'qq')

    # pylint: disable=no-self-use
    def test_readConnectionFile_good(self):
        """ ReadConnectionFile is called """
        with patch("builtins.open",
                   mock_open(read_data="data")) as mock_file:
            rules_obj = rules.Rules(test_mode=True)
            rules_obj.readConnectionFile("nonexistant_file")
            mock_file.assert_called_with("nonexistant_file")

    def test_readConnectionFile_parsing(self):
        """ ReadConnectionFile parses file content """
        fake_data = ("3,1 1 3,2", "5,3 2 4,3")
        with patch("builtins.open", mock_open(read_data="data")):
            rules_obj = rules.Rules(test_mode=True)
            actual_result = rules_obj.readConnectionFile("nonexistant_file",
                                                         test_data=fake_data)
            self.assertEqual(len(actual_result), 2)

    def test_saveGame(self):
        """ Test that game history is convered to a string correctly for
        writing to a save file """
        gameHistory = []
        board_1 = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(5, 3)
        gooseCoordinate = coordinate.Coordinate(4, 3)
        board_1.setState(foxCoordinate, types.FOX)
        board_1.setState(gooseCoordinate, types.GOOSE)
        gameHistory.append(board_1)
        board_2 = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        board_2.setState(foxCoordinate, types.FOX)
        gameHistory.append(board_2)
        metadata = {'p1':1, 'p2':2, 're':3, 'gt':4, 'gs':5, 'fs':6}
        actual_result = rules.saveGame(gameHistory, metadata)
        expected_result = ("p1: 1\n"
                           "p2: 2\n"
                           "re: 3\n"
                           "gt: 4\n"
                           "gs: 5\n"
                           "fs: 6\n"
                           "hm: 1\n"
                           "    0 0 0    \n"
                           "    0 0 0    \n"
                           "0 0 0 0 0 0 0\n"
                           "0 0 0 0 0 0 0\n"
                           "0 0 0 1 2 0 0\n"
                           "    0 0 0    \n"
                           "    0 0 0    \n"
                           "hm: 2\n"
                           "    0 0 0    \n"
                           "    0 0 0    \n"
                           "0 0 0 0 0 0 0\n"
                           "0 0 0 0 0 0 0\n"
                           "0 0 2 0 0 0 0\n"
                           "    0 0 0    \n"
                           "    0 0 0    \n")
        self.assertEqual(actual_result, expected_result)

    def test_makeMetadata(self):
        """ Test meta data input gets correct output """
        test_input = ["p1: Chris\n",
                      "p2: AI\n",
                      "re: 0-2\n",
                      "gt: 1\n",
                      "gs: 2\n",
                      "fs: 3\n",
                      "ga: 4\n"]
        expected_result = {"p1": "Chris",
                           "p2": "AI",
                           "re": "0-2",
                           "gt": "1",
                           "gs": "2",
                           "fs": "3",
                           "ga": "4"}
        actual_result = rules.makeMetadata(test_input)
        self.assertEqual(actual_result['p1'], expected_result['p1'])
        self.assertEqual(actual_result['p2'], expected_result['p2'])
        self.assertEqual(actual_result['re'], expected_result['re'])
        self.assertEqual(actual_result['gt'], expected_result['gt'])
        self.assertEqual(actual_result['gs'], expected_result['gs'])
        self.assertEqual(actual_result['fs'], expected_result['fs'])
        self.assertEqual(actual_result['ga'], expected_result['ga'])

    def test_parseConnectionLine(self):
        """ Connection line is properly parsed """
        fake_connection = "5,3 2 4,3"
        actual_result = rules.parseConnectionLine(fake_connection)
        self.assertEqual(actual_result.startX, 5)
        self.assertEqual(actual_result.startY, 3)
        self.assertEqual(actual_result.direction, 2)
        self.assertEqual(actual_result.endX, 4)
        self.assertEqual(actual_result.endY, 3)

    def test_findConnectionP_nonexistant(self):
        """ FindConnectionP isn't able to find a connection """
        fake_data = ("3,1 1 3,2", "5,3 2 4,3")
        rules_obj = rules.Rules(test_mode=True)
        with patch("builtins.open", mock_open(read_data="data")):
            fake_file = "nonexistant_file"
            rules_obj.boardConnections = \
                rules_obj.readConnectionFile(fake_file, test_data=fake_data)
        startCoordinate = coordinate.Coordinate(5, 5)
        endCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_findConnectionP_exists(self):
        """ FindConnectionP is able to find a connection """
        fake_data = ("3,1 1 3,2", "5,3 2 4,3")
        rules_obj = rules.Rules(test_mode=True)
        with patch("builtins.open", mock_open(read_data="data")):
            fake_file = "nonexistant_file"
            rules_obj.boardConnections = \
                rules_obj.readConnectionFile(fake_file, test_data=fake_data)
        startCoordinate = coordinate.Coordinate(3, 1)
        endCoordinate = coordinate.Coordinate(3, 2)
        actual_result = rules_obj.findConnectionP(startCoordinate,
                                                  endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_legalMoveP_backwards_goose(self):
        """ Goose moving backwards returns false """
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(3, 1)
        endCoordinate = coordinate.Coordinate(3, 2)
        board.setState(startCoordinate, types.GOOSE)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    @patch.object(rules.Rules, "findConnectionP")
    def test_legalMoveP_good(self, mock_findConnectionP):
        """ Legal move returns true """
        mock_findConnectionP.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(5, 3)
        endCoordinate = coordinate.Coordinate(4, 3)
        board.setState(startCoordinate, types.FOX)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    @patch.object(rules.Rules, "findConnectionP")
    def test_legalMoveP_bad(self, mock_findConnectionP):
        """ Not legal move returns False """
        mock_findConnectionP.return_value = False
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        startCoordinate = coordinate.Coordinate(5, 3)
        endCoordinate = coordinate.Coordinate(3, 3)
        board.setState(startCoordinate, types.FOX)
        actual_result = rules_obj.legalMoveP(board,
                                             startCoordinate,
                                             endCoordinate)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    @patch.object(rules.Rules, "findConnectionP")
    def test_captureHelper_true(self, mock_findConnectionP):
        """ When a capture looks good, return True """
        mock_findConnectionP.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        delta_mid = {'x':0, 'y':1}
        delta_end = {'x':0, 'y':2}
        x = foxCoordinate.get_x_board()
        y = foxCoordinate.get_y_board()
        middle_coordinate = coordinate.Coordinate(x+delta_mid['x'],
                                                  y+delta_mid['y'])
        board.setState(middle_coordinate, types.GOOSE)
        actual_result = rules_obj.captureHelper(board,
                                                foxCoordinate,
                                                delta_mid,
                                                delta_end)
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    @patch.object(rules.Rules, "findConnectionP")
    def test_captureHelper_false(self, mock_findConnectionP):
        """ When a capture does not exist, return False """
        mock_findConnectionP.return_value = False
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        delta_mid = {'x':0, 'y':1}
        delta_end = {'x':0, 'y':2}
        x = foxCoordinate.get_x_board()
        y = foxCoordinate.get_y_board()
        middle_coordinate = coordinate.Coordinate(x+delta_mid['x'],
                                                  y+delta_mid['y'])
        board.setState(middle_coordinate, types.GOOSE)
        actual_result = rules_obj.captureHelper(board,
                                                foxCoordinate,
                                                delta_mid,
                                                delta_end)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_1(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 1
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':0, 'y':1},
                                              {'x':0, 'y':2})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_2(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 2
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':1, 'y':1},
                                              {'x':2, 'y':2})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_3(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 3
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':1, 'y':0},
                                              {'x':2, 'y':0})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_4(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 4
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':1, 'y':-1},
                                              {'x':2, 'y':-2})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_5(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 5
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':0, 'y':-1},
                                              {'x':0, 'y':-2})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_6(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 6
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':-1, 'y':-1},
                                              {'x':-2, 'y':-2})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_7(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 7
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':-1, 'y':0},
                                              {'x':-2, 'y':0})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_direction_8(self, mock_captureHelper):
        """ IsACaptureP calls direction with correct args """
        direction = 8
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = True
        self.assertEqual(actual_result, expected_result)
        mock_captureHelper.assert_called_with(board,
                                              foxCoordinate,
                                              {'x':-1, 'y':1},
                                              {'x':-2, 'y':2})

    @patch.object(rules.Rules, "captureHelper")
    def test_isACaptureP_bad_direction(self, mock_captureHelper):
        """ IsACaptureP return False with a bad direction """
        mock_captureHelper.return_value = True
        rules_obj = rules.Rules(test_mode=True)
        board = gamenode.GameNode()
        foxCoordinate = coordinate.Coordinate(3, 3)
        direction = 20
        actual_result = rules_obj.isACaptureP(board, foxCoordinate, direction)
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_findXCoordinateFromDirection_up(self):
        """ Get the delta X from an up direction """
        actual_result = rules.findXCoordinateFromDirection(1)
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_findXCoordinateFromDirection_right(self):
        """ Get the delta X from a right direction """
        actual_result = rules.findXCoordinateFromDirection(3)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def test_findXCoordinateFromDirection_left(self):
        """ Get the delta X from a left direction """
        actual_result = rules.findXCoordinateFromDirection(8)
        expected_result = -2
        self.assertEqual(actual_result, expected_result)

    def test_findXCoordinateFromDirection_bad(self):
        """ Handle a bad direction """
        self.assertRaises(ValueError,
                          rules.findXCoordinateFromDirection,
                          80)

    def test_findYCoordinateFromDirection_left(self):
        """ Get the delta Y from a left direction """
        actual_result = rules.findYCoordinateFromDirection(7)
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_findYCoordinateFromDirection_up(self):
        """ Get the delta Y from a right direction """
        actual_result = rules.findYCoordinateFromDirection(1)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def test_findYCoordinateFromDirection_down(self):
        """ Get the delta Y from a left direction """
        actual_result = rules.findYCoordinateFromDirection(4)
        expected_result = -2
        self.assertEqual(actual_result, expected_result)

    def test_findYCoordinateFromDirection_bad(self):
        """ Handle a bad direction """
        self.assertRaises(ValueError,
                          rules.findYCoordinateFromDirection,
                          80)
