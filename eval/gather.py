# Script to gather evaluation dataset from playing AI games against itself
import os
import sys

sys.path.append(os.getcwd())

from main import checkIfAnyPlayerWon, DEFAULT_AI_WEIGHTS # noqa: E402
from src import ai, gamenode # noqa: E402

MAX_POSITIONS = 10 # Number of gameplay positions to collect
MAX_MOVES_PER_GAME = 50 # Number of moves to make an individual game until ending it as a draw. Games may finish sooner
OUTPUT_PATH = "./positions.jsonl" # Writes positions to jsonl file according to schema
POSITION_SCHEMA = {"startGameNode": [[]]} # position schema
SEARCH_PLY_PAIRS = [[0,2], [2,2], [0,0]] # Plys to pair when generating AI match data

def playAIvsAI(playerAPly, playerBPly, maxMoves):
    game = gamenode.GameNode()
    game.createStartingPosition()
    turns = 0

    while(True):
        # Once per turn checks
        print("Score: {0}".format(game.score))
        turns += 1
        if turns > MAX_MOVES_PER_GAME:
            print("Maximum turns count exceeded")
            break

        # Player A starts their turn
        game.print_board()

        if checkIfAnyPlayerWon(game):
            break

        game = ai.getPlayerMove("a",
                                game,
                                playerAPly,
                                DEFAULT_AI_WEIGHTS)

        # Player B starts their turn
        game.print_board()

        if checkIfAnyPlayerWon(game):
            break

        game = ai.getPlayerMove("b",
                                game,
                                playerBPly,
                                DEFAULT_AI_WEIGHTS)

    print("Final turn count: {0}".format(turns))

def appendPosition():
    pass

if __name__ == "__main__":
    playAIvsAI(2, 4, MAX_MOVES_PER_GAME)