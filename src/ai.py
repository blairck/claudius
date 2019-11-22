""" This module contains the AI search algorithm """

from random import shuffle

# pylint: disable=import-error
from res import types
from src import coordinate
from src import gamenode
from src import rules

def randomSearch(theGame, playerAToPlay):
    """ Randomly pick a move from player's legal moves """
    moves = getAllMovesForPlayer(theGame, playerAToPlay)
    shuffle(moves)
    return moves[0]

def getAllMovesForPlayer(theGame, playerAToPlay):
    """playerAToPlay == True means it's the player A's turn. Otherwise B"""
    moves = []
    for location in getTupleOfAllCoordinates():
        moves.extend(getCapturesForPiece(theGame,
                                         location,
                                         playerAToPlay))

    # If any captures are possible, the player must choose from them
    if moves:
        return moves

    for location in getTupleOfAllCoordinates():
        moves.extend(getNoncaptureMovesForPiece(theGame,
                                                location,
                                                playerAToPlay))
    return moves

def getCapturesForPiece(theGame, pieceLocation, playerAToPlay):
    """ Gets capture list for regular or king pieces """
    moveList = []
    if (theGame.getState(pieceLocation) in (types.PLAYER_A_REGULAR,
                                            types.PLAYER_B_REGULAR)):
        moveList.extend(getCapturesForRegularPiece(theGame,
                                                   pieceLocation,
                                                   playerAToPlay))
    # find king captures. if there are none, then keep any noncaptures
    # that are found

    return moveList

def getLastMoveInEachDirection(theGame, pieceLocation):
    """ Checks 4 directions king could move; returns last move in each dir """
    # TODO - unit test
    deltaAndMoveList = []
    deltaPairs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for deltaPair in deltaPairs:
        pair = []
        pair.append(deltaPair)
        result = getAllNoncaptureMovesForKingPiece(theGame, pieceLocation, pair)
        lastResult = result[len(result)-1]
        pair.append(lastResult)
        deltaAndMoveList.append(pair)
    return deltaAndMoveList

def getDirectionFromDelta(delta):
    """ Gets a direction from x/y delta pair"""
    # TODO - unit test
    if delta == (1, 1):
        return 2
    elif delta == (1, -1):
        return 4
    elif delta == (-1, -1):
        return 6
    elif delta == (-1, 1):
        return 8
    else:
        error_template = "Unexpected delta value of: {0}"
        raise ValueError(error_template.format(delta))

def getNoncaptureMovesForPiece(theGame, pieceLocation, playerAToPlay):
    """Calls getNoncaptureMovesForPiece() or getNoncaptureMovesForRegularPiece()
    Depending on the piece type"""
    moveList = []
    if (theGame.getState(pieceLocation) is types.PLAYER_A_KING
            and playerAToPlay):
        moveList.extend(getAllNoncaptureMovesForKingPiece(theGame,
                                                          pieceLocation))
    elif (theGame.getState(pieceLocation) is types.PLAYER_B_KING
            and not playerAToPlay):
        moveList.extend(getAllNoncaptureMovesForKingPiece(theGame,
                                                          pieceLocation))
    elif (theGame.getState(pieceLocation) is types.PLAYER_A_REGULAR
            and playerAToPlay):
        moveList.extend(getNoncaptureMovesForRegularPiece(theGame,
                                                          pieceLocation))
    elif (theGame.getState(pieceLocation) is types.PLAYER_B_REGULAR
            and not playerAToPlay):
        moveList.extend(getNoncaptureMovesForRegularPiece(theGame,
                                                          pieceLocation))
    return moveList

def getAllNoncaptureMovesForKingPiece(theGame,
                                      pieceLocation,
                                      deltaPairs=((-1, -1),
                                                  (-1, 1),
                                                  (1, -1), 
                                                  (1, 1))):
    """Gets all the noncapture moves for a king piece or pass in deltaPairs
    to specify the direction"""
    moveList = []
    for deltaPair in deltaPairs:
        moveList.extend(getDiagonalNonCaptureMovesForKing(theGame,
                                                          pieceLocation,
                                                          deltaPair[0],
                                                          deltaPair[1]))
    return moveList

def getDiagonalNonCaptureMovesForKing(theGame,
                                      startingLocation,
                                      directionX,
                                      directionY):
    """ This takes the board state, a starting coordinate of a king, and a
    direction. Then it iteratively returns a list of diaganal moves available
    in that direction. """
    resultingMoves = []
    newXBoard = startingLocation.get_x_board()
    newYBoard = startingLocation.get_y_board()
    newPiece = coordinate.Coordinate(newXBoard + directionX,
                                     newYBoard + directionY)
    while(True):
        if (newPiece is None or 
            theGame.getState(newPiece) is not types.EMPTY):
            break
        resultingMoves.append(makePieceMove(theGame,
                                            newPiece,
                                            startingLocation))
        newPiece = getCoordinateHelper(newPiece.get_x_board() + directionX,
                                       newPiece.get_y_board() + directionY)
    return resultingMoves

def getNoncaptureMovesForRegularPiece(theGame, pieceLocation):
    """ This returns a GameNode for every legal move of a regular piece """
    moveList = []
    xBoard = pieceLocation.get_x_board()
    yBoard = pieceLocation.get_y_board()
    pieceDestinationLeft = None
    pieceDestinationRight = None

    if theGame.getState(pieceLocation) is types.PLAYER_A_REGULAR:
        # Player A moves in positive Y increments
        moveDelta = 1
    elif theGame.getState(pieceLocation) is types.PLAYER_B_REGULAR:
        # Player B moves in negative Y increments
        moveDelta = -1
        
    pieceDestinationLeft = getCoordinateHelper(xBoard - 1, yBoard + moveDelta)
    pieceDestinationRight = getCoordinateHelper(xBoard + 1, yBoard + moveDelta)

    if (pieceDestinationLeft and
            destinationIsEmpty(theGame, pieceDestinationLeft)):
        moveList.append(makePieceMove(theGame,
                                      pieceDestinationLeft,
                                      pieceLocation))
    if (pieceDestinationRight and
            destinationIsEmpty(theGame, pieceDestinationRight)):
        moveList.append(makePieceMove(theGame,
                                      pieceDestinationRight,
                                      pieceLocation))
    return moveList

def getCapturesForRegularPiece(theGame, pieceLocation, playerAToPlay):
    """ This recursively finds all available captures for a single piece and
    returns the list of captures. Checks for duplicates from loops"""
    if theGame.getState(pieceLocation) is types.EMPTY:
        return []

    tempCaptureList = []
    x_board = pieceLocation.get_x_board()
    y_board = pieceLocation.get_y_board()
    # 2, 4, 6, 8 are the four directions a piece might capture
    for direction in (2, 4, 6, 8):
        if rules.isACaptureP(theGame,
                             pieceLocation,
                             direction,
                             playerAToPlay):
            deltaX = rules.findXDeltaFromDirection(direction)
            deltaY = rules.findYDeltaFromDirection(direction)
            newMoveNode = transferNode(theGame)
            destination = coordinate.Coordinate(x_board + deltaX,
                                                y_board + deltaY)
            rules.makeCapture(newMoveNode, pieceLocation, destination)
            newMoveNode.isCapture = True
            tempCaptureList.append(newMoveNode)
            nextCapture = getCapturesForRegularPiece(newMoveNode,
                                                     destination,
                                                     playerAToPlay)
            if nextCapture:
                tempCaptureList.extend(nextCapture)

    captureList = removeBoardDuplicates(tempCaptureList)

    captureList = filterForFewestOpposingPieces(captureList, playerAToPlay)

    return captureList

def filterForFewestOpposingPieces(boards, playerAToPlay):
    """ Filters boards to only the moves with fewest opposing pieces, because
    a player must capture as many pieces as possible """
    if boards and len(boards) > 1:
        fewestPiecesMove = min(boards,
                               key=lambda x: x.getPieceCount(not playerAToPlay))
        numOfPieces = fewestPiecesMove.getPieceCount(not playerAToPlay)
        def pieceCountComparison(x):
            """ Returns T/F when board pieceCount == numOfPieces"""
            return x.getPieceCount(not playerAToPlay) == numOfPieces
        boards = list(filter(pieceCountComparison, boards))
    return boards

def removeBoardDuplicates(boards):
    """ Removes duplicates from list of boards """
    uniqueList = []
    for board in boards:
        if board not in uniqueList:
            uniqueList.append(board)
    return uniqueList

def destinationIsEmpty(theGame, pieceDestination):
    """ Returns True or False depending on whether destination is empty """
    return bool(theGame.getState(pieceDestination) is types.EMPTY)

def makePieceMove(theGame, pieceDestination, pieceLocation):
    """ Takes a piece location and destination and updates game state to move
    piece from pieceLocation to pieceDestination """
    pieceType = rules.getPossiblePromotedPiece(theGame,
                                               pieceDestination,
                                               pieceLocation)
    moveResult = transferNode(theGame)
    moveResult.setState(pieceDestination, pieceType)
    moveResult.setState(pieceLocation, types.EMPTY)
    return moveResult

def getTupleOfAllCoordinates():
    """ Gets a tuple of all legal Coordinates on the board """
    return (coordinate.Coordinate(1, 1),
            coordinate.Coordinate(3, 1),
            coordinate.Coordinate(5, 1),
            coordinate.Coordinate(7, 1),
            coordinate.Coordinate(9, 1),
            coordinate.Coordinate(2, 2),
            coordinate.Coordinate(4, 2),
            coordinate.Coordinate(6, 2),
            coordinate.Coordinate(8, 2),
            coordinate.Coordinate(10, 2),
            coordinate.Coordinate(1, 3),
            coordinate.Coordinate(3, 3),
            coordinate.Coordinate(5, 3),
            coordinate.Coordinate(7, 3),
            coordinate.Coordinate(9, 3),
            coordinate.Coordinate(2, 4),
            coordinate.Coordinate(4, 4),
            coordinate.Coordinate(6, 4),
            coordinate.Coordinate(8, 4),
            coordinate.Coordinate(10, 4),
            coordinate.Coordinate(1, 5),
            coordinate.Coordinate(3, 5),
            coordinate.Coordinate(5, 5),
            coordinate.Coordinate(7, 5),
            coordinate.Coordinate(9, 5),
            coordinate.Coordinate(2, 6),
            coordinate.Coordinate(4, 6),
            coordinate.Coordinate(6, 6),
            coordinate.Coordinate(8, 6),
            coordinate.Coordinate(10, 6),
            coordinate.Coordinate(1, 7),
            coordinate.Coordinate(3, 7),
            coordinate.Coordinate(5, 7),
            coordinate.Coordinate(7, 7),
            coordinate.Coordinate(9, 7),
            coordinate.Coordinate(2, 8),
            coordinate.Coordinate(4, 8),
            coordinate.Coordinate(6, 8),
            coordinate.Coordinate(8, 8),
            coordinate.Coordinate(10, 8),
            coordinate.Coordinate(1, 9),
            coordinate.Coordinate(3, 9),
            coordinate.Coordinate(5, 9),
            coordinate.Coordinate(7, 9),
            coordinate.Coordinate(9, 9),
            coordinate.Coordinate(2, 10),
            coordinate.Coordinate(4, 10),
            coordinate.Coordinate(6, 10),
            coordinate.Coordinate(8, 10),
            coordinate.Coordinate(10, 10),)

def getCoordinateHelper(xBoard, yBoard):
    """ Wrap the error handling """
    try:
        return coordinate.Coordinate(xBoard, yBoard)
    except ValueError:
        return None

def transferNode(startNode):
    """ Copies input gamenode to a new one and returns it. """
    resultNode = gamenode.GameNode()
    for x in range(0, 10):
        for y in range(0, 10):
            resultNode.gameState[x][y] = startNode.gameState[x][y]
    return resultNode
