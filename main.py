from res import types
from src import ai
from src import boardParser
from src import coordinate
from src import gamenode
from src import interface
try:
    import debug
    print("Using custom starting position...")
except:
    pass

# Settings
COMP_IS_PLAYER_A = False # User is player A (false) or player B (true)
SEARCH_PLY = 2 # From 0 (weak random moves) to 5 (strong moves) for AI strength
DISPLAY_EVALUATION = False # Display computer evaluation of the position

def aPlayerHasWon(game):
    """ Check game state to see if a player has won """
    game.playerAMoveCount = len(ai.getAllMovesForPlayer(game, True))
    game.playerBMoveCount = len(ai.getAllMovesForPlayer(game, False))

    if game.playerAWins():
        print("Player A wins!")
        return True
    elif game.playerBWins():
        print("Player B wins!")
        return True
    return False

if __name__ == '__main__':
    """ Main game loop. Play alternates between user and computer. """
    try:
        game = boardParser.parseBoardInput(debug.customPosition)
    except NameError:
        game = gamenode.GameNode()
        game.createStartingPosition()

    firstTurn = True

    if COMP_IS_PLAYER_A:
        computersTurn = True
    else:
        computersTurn = False

    while(True):
        if not firstTurn:
            game.print_board()
            print("--------------------------------")
        elif firstTurn and COMP_IS_PLAYER_A:
            game.print_board()
            print("--------------------------------")

        if computersTurn:
            if SEARCH_PLY == 0:
                game = ai.randomSearch(game, COMP_IS_PLAYER_A)
            else:
                game = ai.iterativeDeepeningSearch(game,
                                                   COMP_IS_PLAYER_A,
                                                   SEARCH_PLY)
            if DISPLAY_EVALUATION:
                print("Computer evaluation: {0}".format(game.score))
            computersTurn = False

        game.print_board()

        legalMoves = ai.getAllMovesForPlayer(game, not COMP_IS_PLAYER_A)
        while(True):
            userInput = input('Enter a move: ')
            result = interface.getPositionFromListOfMoves(legalMoves,
                                                          str(userInput),
                                                          COMP_IS_PLAYER_A)
            if len(result) != 1:
                print("Unknown or invalid move, try again")
                continue
            else:
                game = result[0]
                computersTurn = True
                break

        firstTurn = False
