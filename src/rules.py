""" This module contains rules to the game."""

# pylint: disable=import-error
from res import types
from src import coordinate

# -*- coding: utf-8 -*-
class Rules(object):
    """Rules class"""

    def findConnectionP(self, startCoordinate, endCoordinate):
        """Finds connection between start coordinate and end coordinate.
        Returns True if connection exists, False otherwise"""
        startX = startCoordinate.get_x_board()
        startY = startCoordinate.get_y_board()
        endX = endCoordinate.get_x_board()
        endY = endCoordinate.get_y_board()

        if endX - startX == 1 and endY - startY == 1:
            return True
        elif endX - startX == 1 and endY - startY == -1:
            return True
        elif endX - startX == -1 and endY - startY == -1:
            return True
        elif endX - startX == -1 and endY - startY == 1:
            return True
        else:
            return False

    def legalMoveP(self, theGame, startCoordinate, endCoordinate):
        """"Tests whether a start coordinate and end coordinate constitute a
        legal move"""
        if (theGame.getState(startCoordinate) == types.PLAYER_A_REGULAR and
                endCoordinate.get_y_board() < startCoordinate.get_y_board()):
            return False
        elif (theGame.getState(startCoordinate) == types.PLAYER_B_REGULAR and
                endCoordinate.get_y_board() > startCoordinate.get_y_board()):
            return False
        elif (theGame.getState(endCoordinate) == types.EMPTY and
              self.findConnectionP(startCoordinate, endCoordinate)):
            return True
        else:
            return False
