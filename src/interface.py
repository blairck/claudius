""" This module contains the interface for playing the game """

# pylint: disable=import-error
from res import types
from src import coordinate

def getPositionFromListOfMoves(theGame, theMoves, userInput, gooseP):
    """ Gets a position with userInput from a list of legal moves (theMoves).
    Returns empty list if none found or ambiguous"""
    userCoordinates = getCoordinatesFromUserInput(userInput)
    if (len(userCoordinates) > 1 and
          theGame.getState(userCoordinates[0]) != types.EMPTY):
        return matchMultipleCoordinatesToMoves(theMoves,
                                               userCoordinates,
                                               gooseP)
    else:
        return []

def matchMultipleCoordinatesToMoves(theMoves,
                                    userCoordinates,
                                    gooseP):
    """ Match user input when there are multiple legal moves. This function
    iterates over each coordinate that the user inputted. It filters theMoves
    list with the coordinates. If it is a Fox turn, then it will also filter
    based on captured spaces"""
    for i in range(len(userCoordinates) - 1):
        theMoves = list(filter(
            lambda x, inputCoordinate=i:
            x.getState(userCoordinates[inputCoordinate]) == types.EMPTY,
            theMoves))
        connected = rules.Rules().findConnectionP(userCoordinates[i],
                                                  userCoordinates[i+1])
        if not gooseP and not connected:
            startX = userCoordinates[i].get_x_board()
            startY = userCoordinates[i].get_y_board()
            endX = userCoordinates[i+1].get_x_board()
            endY = userCoordinates[i+1].get_y_board()
            captureStartX = int(startX + (endX - startX)/2)
            captureStartY = int(startY + (endY - startY)/2)
            captureCoordinate = coordinate.Coordinate(captureStartX,
                                                      captureStartY)
            theMoves = list(filter(
                lambda x, capture=captureCoordinate:
                x.getState(capture) == types.EMPTY,
                theMoves))
    lastCoordinate = userCoordinates.pop()
    theMoves = matchSingleCoordinateToMoves(theMoves, lastCoordinate, gooseP)
    return theMoves

def isCoordinateMatch(theMove, userCoordinate, gooseP):
    """ Returns true or false if the user coordinate matches theMove """
    destinationType = theMove.getState(userCoordinate)
    if gooseP and destinationType not in (types.OFF_BOARD, types.EMPTY):
        return True
    return False

def getCoordinatesFromUserInput(userInput):
    """ Parses string of user input to get coordinates """
    result = []
    userInput = ''.join(c for c in userInput if c.isdigit())
    inputLength = len(userInput)
    if inputLength < 2 or inputLength % 2 == 1:
        return []
    try:
        result.append(coordinate.Coordinate(int(userInput[0]),
                                            int(userInput[1])))
        for i in range(2, inputLength, 2):
            result.append(coordinate.Coordinate(int(userInput[i]),
                                                int(userInput[i+1])))
    except ValueError:
        return []
    return result
