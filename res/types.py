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
        return '| |'
    elif int(value)==PLAYER_A_REGULAR:
        return '|a|'
    elif int(value)==PLAYER_A_KING:
        return '|A|'
    elif int(value)==PLAYER_B_REGULAR:
        return '|b|'
    elif int(value)==PLAYER_B_KING:
        return '|B|'
    else:
        raise TypeError(("Invalid piece int = {0}").format(value))

def getPieceIntValueFromChar(value):
    if value==' ':
        # A space is actually ambiguous between OFF_BOARD and EMPTY. This 
        # method is used in board_setter so in that case, just returning EMPTY
        # makes the most sense
        return EMPTY
    elif value=='a':
        return PLAYER_A_REGULAR
    elif value=='A':
        return PLAYER_A_KING
    elif value=='b':
        return PLAYER_B_REGULAR
    elif value=='B':
        return PLAYER_B_KING
    else:
        raise TypeError(("Invalid piece char = {0}").format(value))