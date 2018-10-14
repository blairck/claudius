""" This module contains rules to the game."""

# pylint: disable=import-error
from res import types
from src import coordinate

def legalMoveP(theGame, startCoordinate, endCoordinate):
    """"Tests whether a start coordinate and end coordinate constitute a
    legal move"""
    if (theGame.getState(startCoordinate) == types.PLAYER_A_REGULAR and
            endCoordinate.get_y_board() < startCoordinate.get_y_board()):
        return False
    elif (theGame.getState(startCoordinate) == types.PLAYER_B_REGULAR and
          endCoordinate.get_y_board() > startCoordinate.get_y_board()):
        return False
    elif (theGame.getState(endCoordinate) == types.EMPTY and
          findConnectionP(startCoordinate, endCoordinate)):
        return True
    return False

def findConnectionP(startCoordinate, endCoordinate):
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
    return False

def findXDeltaFromDirection(direction):
    """ Returns delta X for jumping, when given a direction value """
    if direction in (2, 4):
        return 2
    elif direction in (6, 8):
        return -2
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template.format(direction))

def findYDeltaFromDirection(direction):
    """ Returns delta Y for jumping, when given a direction value """
    if direction in (8, 2):
        return 2
    elif direction in (4, 6):
        return -2
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template.format(direction))

def isACaptureP(theGame,
                startCoordinate,
                direction,
                playerAToPlay):
    """Returns True if there's a capture, given a start coordinate and
    a direction, otherwise returns False"""
    startX = startCoordinate.get_x_board()
    startY = startCoordinate.get_y_board()

    deltaX = findXDeltaFromDirection(direction)
    deltaY = findYDeltaFromDirection(direction)

    middleCoordinate = None
    endCoordinate = None

    try:
        middleCoordinate = coordinate.Coordinate(int(startX + deltaX/2),
                                                 int(startY + deltaY/2))
        endCoordinate = coordinate.Coordinate(int(startX + deltaX),
                                              int(startY + deltaY))
    except ValueError:
        return False

    startTileState = theGame.getState(startCoordinate)
    middleTileState = theGame.getState(middleCoordinate)
    endTileState = theGame.getState(endCoordinate)

    # Player A to play
    if playerAToPlay:
        return bool((startTileState in (types.PLAYER_A_REGULAR,
                                        types.PLAYER_A_KING)) and
                    (middleTileState in (types.PLAYER_B_REGULAR,
                                         types.PLAYER_B_KING)) and
                    endTileState == types.EMPTY)
    # Player B to play
    else:
        return bool((startTileState in (types.PLAYER_B_REGULAR,
                                        types.PLAYER_B_KING)) and
                    (middleTileState in (types.PLAYER_A_REGULAR,
                                         types.PLAYER_A_KING)) and
                    endTileState == types.EMPTY)
