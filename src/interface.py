""" This module contains the interface for playing the game """

# pylint: disable=import-error
from res import types
from src import coordinate
from src import rules

def getPositionFromListOfMoves(theGame, theMoves, userInput, userIsPlayerB):
    """ Gets a position with userInput from a list of legal moves (theMoves).
    Returns empty list if none found or ambiguous"""
    userCoordinates = getCoordinatesFromUserInput(userInput)
    if (len(userCoordinates) > 1 and
          theGame.getState(userCoordinates[0]) != types.EMPTY):
        return matchMultipleCoordinatesToMoves(theMoves,
                                               userCoordinates,
                                               userIsPlayerB)
    else:
        return []

def matchMultipleCoordinatesToMoves(theMoves,
                                    userCoordinates,
                                    userIsPlayerB):
    """ Match user input when there are multiple legal moves. This function
    iterates over each coordinate that the user inputted. It filters theMoves
    list with the coordinates. If it is a Fox turn, then it will also filter
    based on captured spaces"""
    for i in range(len(userCoordinates) - 1):
        theMoves = list(filter(
            lambda x, inputCoordinate=i:
            x.getState(userCoordinates[inputCoordinate]) == types.EMPTY,
            theMoves))
    lastCoordinate = userCoordinates.pop()
    theMoves = matchSingleCoordinateToMoves(theMoves,
                                            lastCoordinate,
                                            userIsPlayerB)
    return theMoves

def matchSingleCoordinateToMoves(theMoves, userCoordinate, userIsPlayerB):
    """ Match user input when there's only one legal move """
    result = list(filter(lambda x: isCoordinateMatch(x,
                                                     userCoordinate,
                                                     userIsPlayerB),
                         theMoves))
    return result

def isCoordinateMatch(theMove, userCoordinate, userIsPlayerB):
    """ Returns true or false if the user coordinate matches theMove """
    destinationType = theMove.getState(userCoordinate)
    if userIsPlayerB and destinationType is types.PLAYER_B_REGULAR:
        return True
    elif not userIsPlayerB and destinationType is types.PLAYER_A_REGULAR:
        return True
    else:
        return False

def getCoordinatesFromUserInput(userInput):
    """ Parses string of user input to get coordinates """
    result = []
    userInput = ''.join(c for c in userInput if c.isdigit())
    inputLength = len(userInput)
    #print(userInput)
    if inputLength < 2 or inputLength % 2 == 1:
        return []
    try:
        result.append(coordinate.Coordinate(
                      userInputCharacterFor10thAxis(userInput[0]),
                      userInputCharacterFor10thAxis(userInput[1])))

        for i in range(2, inputLength, 2):
            result.append(coordinate.Coordinate(
                          userInputCharacterFor10thAxis(userInput[i]),
                          userInputCharacterFor10thAxis(userInput[i+1])))
    except ValueError:
        return []
    return result

def userInputCharacterFor10thAxis(userInputCharacter):
    """ Maps the chacter '0' to 10th axis for user's input """
    if userInputCharacter is "0":
        return 10
    else:
        return int(userInputCharacter)
