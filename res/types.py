OFF_BOARD = 0
EMPTY = 1
PLAYER_A_REGULAR = 2
PLAYER_A_KING = 3
PLAYER_B_REGULAR = 4
PLAYER_B_KING = 5

def getPieceAbbreviation(value):
    if int(value)==OFF_BOARD:
        return '   '
    elif int(value)==EMPTY:
        return '|||'
    if int(value)==PLAYER_A_REGULAR:
        return '|a|'
    if int(value)==PLAYER_A_KING:
        return '|A|'
    if int(value)==PLAYER_B_REGULAR:
        return '|b|'
    if int(value)==PLAYER_B_KING:
        return '|B|'
    else:
        raise TypeError(("Invalid piece value = {0}").format(value))