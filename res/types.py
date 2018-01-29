OFF_BOARD = 0
EMPTY = 1
PLAYER_A_REGULAR = 2
PLAYER_A_KING = 3
PLAYER_B_REGULAR = 4
PLAYER_B_KING = 5

def getPieceAbbreviation(inputType):
    if int(inputType)==OFF_BOARD:
        return '   '
    elif int(inputType)==EMPTY:
        return '|||'
    if int(inputType)==PLAYER_A_REGULAR:
        return '|a|'
    if int(inputType)==PLAYER_A_KING:
        return '|A|'
    if int(inputType)==PLAYER_B_REGULAR:
        return '|b|'
    if int(inputType)==PLAYER_B_KING:
        return '|B|'
    else:
        return None