import argparse
from src import ai
from src import gamenode
from src import interface
from src.types import PLAYER_A_NAME, PLAYER_B_NAME


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Command line interface for playing Claudius"
    )

    parser.add_argument(
        "--search_ply",
        choices=[0, 2, 4, 6],
        type=int,
        default=2,
        help="Controls AI strength. Set to 0 (weak), 2, 4 or 6 (very strong)",
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


def getMoveFromUserInput(legalMoves):
    while True:
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
        return result[0]

if __name__ == '__main__':
    """ Main game loop. Play alternates between user and computer. """
    args = get_arguments()

    game = gamenode.GameNode()
    game.createStartingPosition()

    firstTurn = True
    computersTurn = True

    computerPlays = PLAYER_A_NAME
    humanPlays = PLAYER_B_NAME
    if args.play_as == "a":
        computersTurn = False
        computerPlays = PLAYER_B_NAME
        humanPlays = PLAYER_A_NAME

    while(True):
        interface.displayBoardForUser(firstTurn, computerPlays, game)

        if interface.checkForEndState(game):
            break

        if computersTurn:
            game = ai.getPlayerMove(computerPlays,
                                    game,
                                    args.search_ply,
                                    ai.DEFAULT_AI_WEIGHTS)

            if args.display_score:
                print("Computer evaluation: {0}".format(game.score))

        game.print_board()

        if interface.checkForEndState(game):
            break

        legalMoves = ai.getAllMovesForPlayer(game, args.play_as == "a")
        game = getMoveFromUserInput(legalMoves)

        computersTurn = True
        firstTurn = False
