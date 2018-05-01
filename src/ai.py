""" This module contains the AI search algorithm """

# pylint: disable=import-error
from res import types
from src import coordinate
from src import gamenode

from random import shuffle

def randomSearch(theGame, userIsPlayerA):
    moves = getAllMovesForPlayer(theGame, userIsPlayerA)
    shuffle(moves)
    return moves[0]

def getAllMovesForPlayer(theGame, userIsPlayerA):
    """userIsPlayerA == True means it's the player A's turn. Otherwise B"""
    moves = []
    for location in getTupleOfAllCoordinates():
        moves.extend(getMovesForRegularPiece(theGame,
                                             location,
                                             userIsPlayerA))
    return moves

def getMovesForRegularPiece(theGame, pieceLocation, userIsPlayerA):
    """ This returns a GameNode for every legal move of a given piece """
    moveList = []
    xBoard = pieceLocation.get_x_board()
    yBoard = pieceLocation.get_y_board()
    pieceDestinationLeft = None
    pieceDestinationRight = None

    if (userIsPlayerA and
            theGame.getState(pieceLocation) is types.PLAYER_A_REGULAR):
        # Player A moves in positive Y increments
        moveDirection = 1
        pieceDestinationLeft = getCoordinateHelper(xBoard - 1,
                                                   yBoard + moveDirection)
        pieceDestinationRight = getCoordinateHelper(xBoard + 1,
                                                    yBoard + moveDirection)
    elif (not userIsPlayerA and
          theGame.getState(pieceLocation) is types.PLAYER_B_REGULAR):
        # Player B moves in negative Y increments
        moveDirection = -1
        pieceDestinationLeft = getCoordinateHelper(xBoard - 1,
                                                   yBoard + moveDirection)
        pieceDestinationRight = getCoordinateHelper(xBoard + 1,
                                                    yBoard + moveDirection)

    if (pieceDestinationLeft and
            destinationIsEmpty(theGame, pieceDestinationLeft)):
        moveList.append(makePieceMove(theGame,
                                      pieceDestinationLeft,
                                      pieceLocation))
    if (pieceDestinationRight and
            destinationIsEmpty(theGame, pieceDestinationRight)):
        moveList.append(makePieceMove(theGame,
                                      pieceDestinationRight,
                                      pieceLocation))
    return moveList

def destinationIsEmpty(theGame, pieceDestination):
    """ Returns True or False depending on whether destination is empty """
    return bool(theGame.getState(pieceDestination) is types.EMPTY)

def makePieceMove(theGame, pieceDestination, pieceLocation):
    """ Takes a piece location and destination and updates game state to move
    piece from pieceLocation to pieceDestination """
    pieceType = theGame.getState(pieceLocation)
    moveResult = transferNode(theGame)
    moveResult.setState(pieceDestination, pieceType)
    moveResult.setState(pieceLocation, types.EMPTY)
    return moveResult

def getTupleOfAllCoordinates():
    """ Gets a tuple of all legal Coordinates on the board """
    return (coordinate.Coordinate(1, 1),
            coordinate.Coordinate(3, 1),
            coordinate.Coordinate(5, 1),
            coordinate.Coordinate(7, 1),
            coordinate.Coordinate(9, 1),
            coordinate.Coordinate(2, 2),
            coordinate.Coordinate(4, 2),
            coordinate.Coordinate(6, 2),
            coordinate.Coordinate(8, 2),
            coordinate.Coordinate(10, 2),
            coordinate.Coordinate(1, 3),
            coordinate.Coordinate(3, 3),
            coordinate.Coordinate(5, 3),
            coordinate.Coordinate(7, 3),
            coordinate.Coordinate(9, 3),
            coordinate.Coordinate(2, 4),
            coordinate.Coordinate(4, 4),
            coordinate.Coordinate(6, 4),
            coordinate.Coordinate(8, 4),
            coordinate.Coordinate(10, 4),
            coordinate.Coordinate(1, 5),
            coordinate.Coordinate(3, 5),
            coordinate.Coordinate(5, 5),
            coordinate.Coordinate(7, 5),
            coordinate.Coordinate(9, 5),
            coordinate.Coordinate(2, 6),
            coordinate.Coordinate(4, 6),
            coordinate.Coordinate(6, 6),
            coordinate.Coordinate(8, 6),
            coordinate.Coordinate(10, 6),
            coordinate.Coordinate(1, 7),
            coordinate.Coordinate(3, 7),
            coordinate.Coordinate(5, 7),
            coordinate.Coordinate(7, 7),
            coordinate.Coordinate(9, 7),
            coordinate.Coordinate(2, 8),
            coordinate.Coordinate(4, 8),
            coordinate.Coordinate(6, 8),
            coordinate.Coordinate(8, 8),
            coordinate.Coordinate(10, 8),
            coordinate.Coordinate(1, 9),
            coordinate.Coordinate(3, 9),
            coordinate.Coordinate(5, 9),
            coordinate.Coordinate(7, 9),
            coordinate.Coordinate(9, 9),
            coordinate.Coordinate(2, 10),
            coordinate.Coordinate(4, 10),
            coordinate.Coordinate(6, 10),
            coordinate.Coordinate(8, 10),
            coordinate.Coordinate(10, 10),)

def getCoordinateHelper(xBoard, yBoard):
    """ Wrap the error handling """
    try:
        return coordinate.Coordinate(xBoard, yBoard)
    except ValueError:
        return None

def transferNode(startNode):
    """ Copies input gamenode to a new one and returns it. """
    resultNode = gamenode.GameNode()
    for x in range(0, 10):
        for y in range(0, 10):
            resultNode.gameState[x][y] = startNode.gameState[x][y]
    return resultNode
