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

    while(True):
        game.print_board()
        print("---------------------------------")

        while(True):
            userInput = input('Enter a move: ')
