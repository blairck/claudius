# Script to read in positions.jsonl file from gather.py. For each position, it adds a groundTruth position and writes to a new file evalCases.jsonl
import json
import os
import sys

sys.path.append(os.getcwd())

from eval import gather
from src import ai, gamenode, helper


ANALYSIS_SEARCH_PLY = 6 # How deep to analyze each position to determine ground truth
EVAL_CASE_SCHEMA = {"startGameNode": "", "groundTruthGameNode": ""} # eval case schema

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

def getGroundTruthDataRow(flattenedGameState, groundTruthGameState):
    return {"startGameNode": flattenedGameState,
            "groundTruthGameNode": groundTruthGameState}

def _getPlayerMove(activePlayer, currentGameNode):
    return ai.getPlayerMove(activePlayer,
                            currentGameNode,
                            ANALYSIS_SEARCH_PLY,
                            ai.DEFAULT_AI_WEIGHTS)


if __name__ == "__main__":
    positions = readGatherDataFile("eval/startPositionData.jsonl")
    result = []

    for i, position in enumerate(positions):
        print(f"Working on: {i}")
        currentGameNode = readFlatGameState(position["startGameNode"])
        game = _getPlayerMove(position["activePlayer"], currentGameNode)
        if game is not None:
            flatGame = gather.getFlatGameNode(game)[0]
            result.append(getGroundTruthDataRow(position["startGameNode"], flatGame))

    with open("eval/evaluationData.jsonl", "w", encoding="utf-8") as f:
        f.writelines(f"{json.dumps(row)}\n" for row in result)
