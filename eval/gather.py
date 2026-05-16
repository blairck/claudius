# Script to gather evaluation dataset from playing AI games against itself
import os
import sys

sys.path.append(os.getcwd())

from src.types import PLAYER_A_NAME, PLAYER_B_NAME # noqa: E402
from src import ai, gamenode, helper, interface # noqa: E402

MAX_POSITIONS = 10 # Number of gameplay positions to collect
MAX_MOVES_PER_GAME = 100 # Number of moves to make an individual game until ending it as a draw. Games may finish sooner
OUTPUT_PATH = "./positions.jsonl" # Writes positions to jsonl file according to schema
POSITION_SCHEMA = {"startGameNode": "", "matchUp": []} # position schema for 1 row of jsonl file
SEARCH_PLY_PAIRS = [[0,2], [2,2], [0,0]] # Plys to pair when generating AI match data

def getFlatGameNode(gn):
    """ Returns flat game state like where every 5 characters is a board row starting
    at 1 and going up to 10: '11111111111111111114111151211144411111111141114411'
    """
    coordinateTuple = helper.getTupleOfAllCoordinates()
    listOfBoardStates = []
    for coordinate in coordinateTuple:
        listOfBoardStates.append(str(gn.getState(coordinate)))
    return "".join(listOfBoardStates)

def getEvaluationDataRow(flattenedGameState):
    return {"startGameNode": flattenedGameState} 

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
        flatGameStatesResult.append(getFlatGameNode(game))

        # Player B starts their turn
        # game.print_board()

        if interface.checkForEndState(game):
            break

        game = ai.getPlayerMove(PLAYER_B_NAME,
                                game,
                                playerBPly,
                                ai.DEFAULT_AI_WEIGHTS)
        flatGameStatesResult.append(getFlatGameNode(game))
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
    result = [getEvaluationDataRow(i) for i in uniqueGameStates]
    
    with open("evaluationData.jsonl", "w", encoding="utf-8") as f:
        f.writelines(f"{row}\n" for row in result)
