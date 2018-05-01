""" This module contains rules to the game."""

# pylint: disable=import-error
from res import types
from src import connection
from src import coordinate

# -*- coding: utf-8 -*-
class Rules(object):
    """Rules class"""
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        if not test_mode:
            path = "res/board_connections.txt"
            self.boardConnections = self.readConnectionFile(path)

    def readConnectionFile(self, file_path, test_data=None):
        """ Reads in the file of connections """
        result = []
        with open(file_path) as f:
            if test_data and self.test_mode:
                f = test_data
            for line in f:
                result.append(parseConnectionLine(line))
        return result

    def findConnectionP(self, startCoordinate, endCoordinate):
        """Finds connection between start coordinate and end coordinate.
        Returns True if connection exists, False otherwise"""
        startX = startCoordinate.get_x_board()
        startY = startCoordinate.get_y_board()
        endX = endCoordinate.get_x_board()
        endY = endCoordinate.get_y_board()
        for con in self.boardConnections:
            if (con.startX == startX and
                    con.startY == startY and
                    con.endX == endX and
                    con.endY == endY):
                return True
        return False

    def legalMoveP(self, theGame, startCoordinate, endCoordinate):
        """"Tests whether a start coordinate and end coordinate constitute a
        legal move"""
        if (theGame.getState(startCoordinate) == types.GOOSE and
                endCoordinate.get_y_board() > startCoordinate.get_y_board()):
            return False
        elif (theGame.getState(endCoordinate) == types.EMPTY and
              self.findConnectionP(startCoordinate, endCoordinate)):
            return True
        return False

    def captureHelper(self,
                      theGame,
                      foxCoordinate,
                      delta_mid,
                      delta_end):
        """ Determines if a particular set up board + fox + delta
        constitutes a legal capture """
        x = foxCoordinate.get_x_board()
        y = foxCoordinate.get_y_board()
        try:
            middle_coordinate = coordinate.Coordinate(x+delta_mid['x'],
                                                      y+delta_mid['y'])
            end_coordinate = coordinate.Coordinate(x+delta_end['x'],
                                                   y+delta_end['y'])
        except ValueError:
            # Sometimes delta coordinates will result in a position off the
            # board. In these cases, just return False since no capture is
            # possible here.
            return False
        middle_tile_state = theGame.getState(middle_coordinate)
        end_tile_state = theGame.getState(end_coordinate)
        return bool((middle_tile_state in (types.GOOSE, types.SUPERGOOSE)) and
                    end_tile_state == 0 and
                    self.findConnectionP(foxCoordinate, middle_coordinate) and
                    self.findConnectionP(middle_coordinate, end_coordinate))

    def isACaptureP(self, theGame, foxCoordinate, direction):
        """Returns true if there's a capture, given a fox coordinate and
        a direction. otherwise returns false"""
        delta_mid = None
        delta_end = None
        if direction == 1 and foxCoordinate.get_y_board() < 6:
            delta_mid = {'x':0, 'y':1}
            delta_end = {'x':0, 'y':2}
        elif (direction == 2 and
              foxCoordinate.get_x_board() < 6 and
              foxCoordinate.get_y_board() < 6):
            delta_mid = {'x':1, 'y':1}
            delta_end = {'x':2, 'y':2}
        elif direction == 3 and foxCoordinate.get_x_board() < 6:
            delta_mid = {'x':1, 'y':0}
            delta_end = {'x':2, 'y':0}
        elif (direction == 4 and
              foxCoordinate.get_x_board() < 6 and
              foxCoordinate.get_y_board() > 2):
            delta_mid = {'x':1, 'y':-1}
            delta_end = {'x':2, 'y':-2}
        elif direction == 5 and foxCoordinate.get_y_board() > 2:
            delta_mid = {'x':0, 'y':-1}
            delta_end = {'x':0, 'y':-2}
        elif (direction == 6 and
              foxCoordinate.get_x_board() > 2 and
              foxCoordinate.get_y_board() > 2):
            delta_mid = {'x':-1, 'y':-1}
            delta_end = {'x':-2, 'y':-2}
        elif (direction == 7 and
              foxCoordinate.get_x_board() > 2):
            delta_mid = {'x':-1, 'y':0}
            delta_end = {'x':-2, 'y':0}
        elif (direction == 8 and
              foxCoordinate.get_x_board() > 2 and
              foxCoordinate.get_y_board() < 6):
            delta_mid = {'x':-1, 'y':1}
            delta_end = {'x':-2, 'y':2}

        if delta_mid and delta_end:
            return self.captureHelper(theGame,
                                      foxCoordinate,
                                      delta_mid,
                                      delta_end)
        else:
            # Fox is near the edge of the board and won't be able to capture
            # in this direction.
            return False

def findXCoordinateFromDirection(direction):
    """ Returns delta X, when given a direction value """
    if direction in (1, 5):
        return 0
    elif direction in (2, 3, 4):
        return 2
    elif direction in (6, 7, 8):
        return -2
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template)

def findYCoordinateFromDirection(direction):
    """ Returns delta Y, when given a direction value """
    if direction in (3, 7):
        return 0
    elif direction in (8, 1, 2):
        return 2
    elif direction in (4, 5, 6):
        return -2
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template)
