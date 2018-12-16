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

def makeCapture(theGame, startCoordinate, endCoordinate):
    """ Update the board for a capture between a start and end coordinate """
    startX = startCoordinate.get_x_board()
    startY = startCoordinate.get_y_board()
    endX = endCoordinate.get_x_board()
    endY = endCoordinate.get_y_board()

    startPieceType = theGame.getState(startCoordinate)

    if startPieceType in (types.EMPTY, types.OFF_BOARD):
        error_template = "Illegal start piece type: {0} at ({1}, {2})"
        raise TypeError(error_template.format(startPieceType, startX, startY))
    elif abs(startX - endX) not in (0, 2):
        error_template = "Illegal X capture: {0} -> {1}"
        raise ValueError(error_template.format(startX, endX))
    elif abs(startY - endY) not in (0, 2):
        error_template = "Illegal Y capture: {0} -> {1}"
        raise ValueError(error_template.format(startY, endY))
    elif startX == endX and startY == endY:
        error_template = ("Start and end capture coordinates are the "
                          "same: ({0}, {1})")
        raise ValueError(error_template.format(startX, startY))

    captureStartX = int(startX + (endX - startX)/2)
    captureStartY = int(startY + (endY - startY)/2)
    captureCoordinate = coordinate.Coordinate(captureStartX, captureStartY)

    theGame.setState(endCoordinate, theGame.getState(startCoordinate))
    theGame.setState(captureCoordinate, types.EMPTY)
    theGame.setState(startCoordinate, types.EMPTY)
