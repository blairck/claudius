OFF_BOARD = 0
EMPTY = 1
PLAYER_A_REGULAR = 2
PLAYER_A_KING = 3
PLAYER_B_REGULAR = 4
PLAYER_B_KING = 5

def getPieceAbbreviation(intValueAsString):
    if int(intValueAsString)==OFF_BOARD:
        return "   "
    elif int(intValueAsString)==EMPTY:
        return " . "
    elif int(intValueAsString)==PLAYER_A_REGULAR:
        return " a "
    elif int(intValueAsString)==PLAYER_A_KING:
        return " A "
    elif int(intValueAsString)==PLAYER_B_REGULAR:
        return " b "
    elif int(intValueAsString)==PLAYER_B_KING:
        return " B "
    else:
        raise TypeError(("Invalid piece int = {0}").format(intValueAsString))

def getPieceIntValueFromChar(charValue):
    if charValue==' ':
        return OFF_BOARD
    elif charValue=='.':
        return EMPTY
    elif charValue=='a':
        return PLAYER_A_REGULAR
    elif charValue=='A':
        return PLAYER_A_KING
    elif charValue=='b':
        return PLAYER_B_REGULAR
    elif charValue=='B':
        return PLAYER_B_KING
    else:
        raise TypeError(("Invalid piece char = {0}").format(charValue))

def getPromotedPiece(intValue):
    if intValue == PLAYER_A_REGULAR:
        return PLAYER_A_KING
    elif intValue == PLAYER_B_REGULAR:
        return PLAYER_B_KING
    else:
        return intValue