import argparse
from src import ai
from src import gamenode
from src import interface


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Command line interface for playing Claudius"
    )

    parser.add_argument(
        "--search_ply",
        type=int,
        default=2,
        help="Controls AI strength. From 0 (weak) to 5 (strong)",
    )

    parser.add_argument(
        "--play_as",
        choices=["a", "b"],
        default="a",
    )

    parser.add_argument(
        "--display_score",
        type=bool,
        default=False,
        help="Display AI's score for each position, can be +/-"
    )

    return parser.parse_args()

def checkIfAnyPlayerWon(game):
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
    args = get_arguments()
    game = gamenode.GameNode()
    game.createStartingPosition()

    firstTurn = True
    computersTurn = True

    if args.play_as == "a":
        computersTurn = False

    while(True):
        interface.displayBoardForUser(firstTurn, args.play_as, game)

        if checkIfAnyPlayerWon(game):
            break

        if computersTurn:
            if args.search_ply == 0:
                game = ai.randomSearch(game, args.play_as == "b")
            else:
                game = ai.iterativeDeepeningSearch(game,
                                                   args.play_as == "b",
                                                   args.search_ply)
            if args.display_score:
                print("Computer evaluation: {0}".format(game.score))
            computersTurn = False

        game.print_board()

        if checkIfAnyPlayerWon(game):
            break

        legalMoves = ai.getAllMovesForPlayer(game, args.play_as == "a")
        while(True):
            userInput = input('Enter a move: ')
            if userInput == 'm' or userInput == 'moves':
                print("These are your legal moves:")
                for move in legalMoves:
                    move.print_board()
                print("--------------------------------")
                continue
            result = interface.getPositionFromListOfMoves(legalMoves,
                                                          str(userInput),
                                                          args.play_as == "b")
            if len(result) != 1:
                print("Unknown or invalid move, try again")
                continue
            else:
                game = result[0]
                computersTurn = True
                break

        firstTurn = False
