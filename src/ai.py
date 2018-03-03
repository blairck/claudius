""" This module contains the AI search algorithm """

from random import shuffle

# pylint: disable=import-error
from res import types
from src import coordinate
from src import gamenode

class AI(object):
    """ Class that stores the AI algorithm """
    def __init__(self):
        self.weightA = 1.0
        self.weightB = 1.0
        self.moveCount = 0

    def getAllMovesForPlayer(self, theGame, userIsPlayerA):
        """GooseP == True means it's the Goose player's turn. Otherwise fox"""
        moves = []
        for location in getTupleOfAllCoordinates():
            moves.extend(self.getMovesForRegularPiece(theGame,
                         location,
                         userIsPlayerA))
        if not gooseP:
            captureMoves = list(filter(lambda x: x.isCapture, moves))
            if len(captureMoves) > 0:
                return captureMoves
        return moves

    def getMovesForRegularPiece(self, theGame, pieceLocation, userIsPlayerA):
        """ This returns a GameNode for every legal move of a given piece """
        moveList = []
        xBoard = pieceLocation.get_x_board()
        yBoard = pieceLocation.get_y_board()

        if userIsPlayerA:
            if theGame.getState(pieceLocation) is types.PLAYER_A_REGULAR:
                pieceType = theGame.getState(pieceLocation)
                pieceDestinationLeft = getCoordinateHelper(xBoard - 1,
                                                           yBoard + 1)
                pieceDestinationRight = getCoordinateHelper(xBoard + 1,
                                                            yBoard + 1)

                if pieceDestinationLeft:
                    moveResult = transferNode(theGame)
                    moveResult.setState(pieceDestinationLeft, pieceType)
                    moveResult.setState(pieceLocation, types.EMPTY)
                    moveList.append(moveResult)
                if pieceDestinationRight:
                    moveResult = transferNode(theGame)
                    moveResult.setState(pieceDestinationRight, pieceType)
                    moveResult.setState(pieceLocation, types.EMPTY)
                    moveList.append(moveResult)

        return moveList

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
