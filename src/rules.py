""" This module contains rules to the game."""

# pylint: disable=import-error
from res import types
from src import coordinate

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

def isACaptureP(theGame, startCoordinate, direction, playerAToPlay):
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

    theGame.setState(endCoordinate, getPossiblePromotedPiece(theGame,
                                                             endCoordinate,
                                                             startCoordinate))
    theGame.setState(captureCoordinate, types.EMPTY)
    theGame.setState(startCoordinate, types.EMPTY)
    theGame.pieceLastMoved = endCoordinate

def getCaptureCoordinateFromDirection(startCoordinate, direction):
    """ Takes a coordinate and a direction, and returns the landing point of
    a possible capture """
    if direction == 2:
        delta = {'x':2, 'y':2}
    elif direction == 4:
        delta = {'x':2, 'y':-2}
    elif direction == 6:
        delta = {'x':-2, 'y':-2}
    elif direction == 8:
        delta = {'x':-2, 'y':2}
    else:
        error_template = "Unexpected direction value of: {0}"
        raise ValueError(error_template.format(direction))

    startX = startCoordinate.get_x_board()
    startY = startCoordinate.get_y_board()
    endX = startX + delta.get('x')
    endY = startY + delta.get('y')

    # can raise ValueError if off-board
    return coordinate.Coordinate(endX, endY)


def getPossiblePromotedPiece(theGame, pieceDestination, pieceLocation):
    """ Takes a piece location and its destination. If it is a regular piece
    moving to the final row, then returns a King type. Otherwise returns
    the original piece type. """
    pieceType = theGame.getState(pieceLocation)
    if (pieceDestination.get_y_board() == 10 and
            pieceType == types.PLAYER_A_REGULAR):
        pieceType = types.PLAYER_A_KING
    elif (pieceDestination.get_y_board() == 1 and
          pieceType == types.PLAYER_B_REGULAR):
        pieceType = types.PLAYER_B_KING
    return pieceType
