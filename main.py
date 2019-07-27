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

def aPlayerHasWon(game):
    """ Check game state to see if a player has won """
    raise NotImplementedError

def determineDraw(game, ai):
    """ Check game state to see if it is drawn """
    raise NotImplementedError

if __name__ == '__main__':
    """ Main game loop. Play alternates between user and computer. """
    try:
        game = boardParser.parseBoardInput(debug.customPosition)
    except NameError:
        game = gamenode.GameNode()
        game.createStartingPosition()

    firstTurn = True
    COMP_IS_PLAYER_A = True

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
            game = ai.randomSearch(game, COMP_IS_PLAYER_A)
            computersTurn = False

        game.print_board()

        legalMoves = ai.getAllMovesForPlayer(game, not COMP_IS_PLAYER_A)
        while(True):
            userInput = input('Enter a move: ')
            result = interface.getPositionFromListOfMoves(game,
                                                          legalMoves,
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
