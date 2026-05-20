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