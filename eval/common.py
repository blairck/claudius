import json

from src import gamenode, helper


def readGatherDataFile(path):
    result = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            result.append(json.loads(line.rstrip("\n")))
    return result


def readFlatGameState(flatGameState):
    coordinates = helper.getTupleOfAllCoordinates()
    newGameNode = gamenode.GameNode()
    listGameState = list(flatGameState)

    for i in range(len(coordinates)):
        newGameNode.setState(coordinates[i], int(listGameState[i]))

    return newGameNode


def getFlatGameNode(gn, activePlayer=None):
    """ Returns flat game state like where every 5 characters is a board row starting
    at 1 and going up to 10: '11111111111111111114111151211144411111111141114411'
    """
    coordinateTuple = helper.getTupleOfAllCoordinates()
    listOfBoardStates = []
    for coordinate in coordinateTuple:
        listOfBoardStates.append(str(gn.getState(coordinate)))
    return ("".join(listOfBoardStates), activePlayer)
