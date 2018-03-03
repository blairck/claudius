from res import types
from src import coordinate
from src import gamenode

def aPlayerHasWon(game):
    """ Check game state to see if a player has won """
    raise NotImplementedError

def determineDraw(game, ai):
    """ Check game state to see if it is drawn """
    raise NotImplementedError

def createStartingPosition():
    game = gamenode.GameNode()
    odd_piece_rows = (1, 3, 5, 7, 9)
    even_piece_rows = (2, 4, 6, 8, 10)

    for y in (1, 3):
        for x in odd_piece_rows:
            game.setState(coordinate.Coordinate(x, y), types.PLAYER_A_REGULAR)

    for y in (7, 9):
        for x in odd_piece_rows:
            game.setState(coordinate.Coordinate(x, y), types.PLAYER_B_REGULAR)

    for y in (2, 4):
        for x in even_piece_rows:
            game.setState(coordinate.Coordinate(x, y), types.PLAYER_A_REGULAR)

    for y in (8, 10):
        for x in even_piece_rows:
            game.setState(coordinate.Coordinate(x, y), types.PLAYER_B_REGULAR)

    return game

if __name__ == '__main__':
    """ Main game loop. Play alternates between user and computer. """
    game = createStartingPosition()
    firstTurn = True
    USER_IS_PLAYER_A = True

    #aiObject = ai.AI()
    if USER_IS_PLAYER_A:
        computersTurn = True
    else:
        computersTurn = False

    while(True):
        if not firstTurn:
            game.print_board()
            print("---------------------------------")
        elif firstTurn and USER_IS_PLAYER_A:
            game.print_board()
            print("---------------------------------")

        # if aPlayerHasWon(game):
        #     break
        # elif determineDraw(game, aiObject):
        #     break

        if computersTurn:
            # game = aiObject.iterativeDeepeningSearch(game,
            #                                          USER_IS_PLAYER_A,
            #                                          SEARCHPLY)
            computersTurn = False

        game.print_board()

        #legalMoves = aiObject.getAllMovesForPlayer(game, not USER_IS_PLAYER_A)
        while(True):
            userInput = input('Enter a move: ')
