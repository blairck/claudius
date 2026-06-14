# Script to gather evaluation dataset from playing AI games against itself
import json
import os
import sys

sys.path.append(os.getcwd())

from eval import common
from src.types import PLAYER_A_NAME, PLAYER_B_NAME # noqa: E402
from src import ai, gamenode, interface # noqa: E402

MAX_POSITIONS = 10 # Number of gameplay positions to collect
MAX_MOVES_PER_GAME = 100 # Number of moves to make an individual game until ending it as a draw. Games may finish sooner
OUTPUT_PATH = "./positions.jsonl" # Writes positions to jsonl file according to schema
POSITION_SCHEMA = {"startGameNode": "", "matchUp": []} # position schema for 1 row of jsonl file
SEARCH_PLY_PAIRS = [[0,2], [2,2], [0,0]] # Plys to pair when generating AI match data


def getEvaluationDataRow(flattenedGameState, activePlayer):
    return {"startGameNode": flattenedGameState, "activePlayer": activePlayer} 

def playAIvsAI(playerAPly, playerBPly, maxMoves):
    game = gamenode.GameNode()
    game.createStartingPosition()
    turns = 0
    flatGameStatesResult = []

    while(True):
        # Once per turn checks
        # print("Score: {0}".format(game.score))
        turns += 1
        if turns > maxMoves:
            print("Maximum turns count exceeded")
            break

        # Player A starts their turn
        # game.print_board()
        if interface.checkForEndState(game):
            break

        game = ai.getPlayerMove(PLAYER_A_NAME,
                                game,
                                playerAPly,
                                ai.DEFAULT_AI_WEIGHTS)
        flatGameStatesResult.append(common.getFlatGameNode(game, PLAYER_B_NAME))

        # Player B starts their turn
        # game.print_board()
        if interface.checkForEndState(game):
            break

        game = ai.getPlayerMove(PLAYER_B_NAME,
                                game,
                                playerBPly,
                                ai.DEFAULT_AI_WEIGHTS)
        flatGameStatesResult.append(common.getFlatGameNode(game, PLAYER_A_NAME))

    return tuple(flatGameStatesResult)
    # print("Final turn count: {0}".format(turns))

def appendPosition():
    pass

if __name__ == "__main__":
    gameStates = []
    for matchUp in SEARCH_PLY_PAIRS:
        print(f"Running match up: {matchUp}")
        gameStates.extend(playAIvsAI(matchUp[0], matchUp[1], MAX_MOVES_PER_GAME))
    uniqueGameStates = set(gameStates)
    result = [getEvaluationDataRow(i[0], i[1]) for i in uniqueGameStates]
    
    with open("eval/data/startPositions.jsonl", "w", encoding="utf-8") as f:
        f.writelines(f"{json.dumps(row)}\n" for row in result)
