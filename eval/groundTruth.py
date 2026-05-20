# Script to read in positions.jsonl file from gather.py. For each position, it adds a groundTruth position and writes to a new file evalCases.jsonl
import json
import os
import sys


sys.path.append(os.getcwd())

from eval import gather, common
from src import ai


ANALYSIS_SEARCH_PLY = 6 # How deep to analyze each position to determine ground truth
EVAL_CASE_SCHEMA = {"startGameNode": "", "groundTruthGameNode": ""} # eval case schema


def getGroundTruthDataRow(flattenedGameState, groundTruthGameState):
    return {"startGameNode": flattenedGameState,
            "groundTruthGameNode": groundTruthGameState}


if __name__ == "__main__":
    positions = common.readGatherDataFile("eval/startPositionData.jsonl")
    result = []

    for i, position in enumerate(positions):
        print(f"Working on: {i}")
        currentGameNode = common.readFlatGameState(position["startGameNode"])
        game = ai.getPlayerMove(position["activePlayer"],
                                currentGameNode,
                                ANALYSIS_SEARCH_PLY,
                                ai.DEFAULT_AI_WEIGHTS)
        if game is not None:
            flatGame = gather.getFlatGameNode(game)[0]
            result.append(getGroundTruthDataRow(position["startGameNode"], flatGame))

    with open("eval/data/evaluationData.jsonl", "w", encoding="utf-8") as f:
        f.writelines(f"{json.dumps(row)}\n" for row in result)
