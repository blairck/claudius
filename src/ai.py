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

def iterativeDeepeningSearch(theGame, playerAToPlay, searchPly):
    """ Searches at steadily increasing ply and breaks if a draw or end
    state is found, otherwise searches to searchPly (inclusive). """
    bestMove = None
    plyRange = range(1, searchPly + 1, 1)
    for ply in plyRange:
        bestMove = findBestMove(theGame, playerAToPlay, ply)
        if (bestMove is None
                or bestMove.score < -2999
                or bestMove.score > 2999):
            return bestMove
    return bestMove

def findBestMove(theGame,
                 playerAToPlay,
                 searchPly,
                 minimum=-10000,
                 maximum=10000,
                 firstCall=True):
    """ Main alpha-beta minimax algorithm to find best move """
    allMoves = getAllMovesForPlayer(theGame, playerAToPlay)
    if firstCall and len(allMoves) == 0:
        return None
    elif not firstCall and len(allMoves) == 0:
        return 0

    for move in allMoves:
        evaluationFunction(move)
        move.playerAMoveCount = len(getAllMovesForPlayer(move, True))
        move.playerBMoveCount = len(getAllMovesForPlayer(move, False))
        move.determineWinningState()

    shuffle(allMoves)
    searchPly -= 1
    if searchPly > 0 and not theGame.winningState:
        allMoves.sort(key=lambda x: x.score, reverse=playerAToPlay)
        if playerAToPlay:
            for move in allMoves:
                result = findBestMove(move,
                                      not playerAToPlay,
                                      searchPly,
                                      minimum,
                                      maximum,
                                      False)
                move.score = result
                if result > minimum:
                    minimum = result
                if result > maximum:
                    move.score = maximum
                    return move.score
        else:
            for move in allMoves:
                result = findBestMove(move,
                                      not playerAToPlay,
                                      searchPly,
                                      minimum,
                                      maximum,
                                      False)
                move.score = result
                if result < maximum:
                    maximum = result
                if result < minimum:
                    move.score = minimum
                    return move.score
    if firstCall:
        return getHighestOrLowestScoreMove(allMoves, playerAToPlay)
    else:
        return getHighestOrLowestScoreMove(allMoves, playerAToPlay).score

def getHighestOrLowestScoreMove(moves, playerAToPlay):
    """ Returns the highest/lowest scored move depending on the player """
    if playerAToPlay:
        return max(moves, key=lambda x: x.score)
    else:
        return min(moves, key=lambda x: x.score)

def evaluationFunction(theGame):
    # This evaluation uses attributes that are applicable to both players. Then
    # it adds up the occurrences for A, subtracts the occurrences for B, and
    # multiplies by weight. All attribute/weight products are then added up and
    # saved to theGame.score.
    # Definitions:
    # - Attribute: A specific feature of a player's position
    # - Weight: Values which give attributes relative importance
    # - List of attributes:
    # 1. Regular pieces
    # 2. King pieces
    # 3. Pieces in columns 5/6 (center)
    # 4. Pieces in columns 3/4 & 7/8 (flank)
    # 5. Pieces in columns 1/2 & 9/10 (edge)
    # 6. Pieces in rows 4/5/6/7 (mid)

    if theGame.score:
        return

    attributeCount = {"regularPieces":0,
                      "kingPieces":0,
                      "centerPieces":0,
                      "flankPieces":0,
                      "edgePieces":0,
                      "midPieces":0}

    weightValues = {"regularPieces":10,
                    "kingPieces":50,
                    "centerPieces":5,
                    "flankPieces":3,
                    "edgePieces":2,
                    "midPieces":4}

    for x in range(0, 10):
        for y in range(0, 10):
            if theGame.gameState[x][y] in (types.EMPTY, types.OFF_BOARD):
                continue

            # attribute "regularPieces"
            if theGame.gameState[x][y] == types.PLAYER_A_REGULAR:
                attributeCount["regularPieces"] += 1
            elif theGame.gameState[x][y] == types.PLAYER_B_REGULAR:
                attributeCount["regularPieces"] -= 1

            # attribute "kingPieces"
            if theGame.gameState[x][y] == types.PLAYER_A_KING:
                attributeCount["kingPieces"] += 1
            elif theGame.gameState[x][y] == types.PLAYER_B_KING:
                attributeCount["kingPieces"] -= 1

            # attribute "centerPieces"
            if (theGame.gameState[x][y] in (types.PLAYER_A_REGULAR,
                                            types.PLAYER_A_KING) and
                4<=x<=5):
                attributeCount["centerPieces"] += 1
            elif (theGame.gameState[x][y] in (types.PLAYER_B_REGULAR,
                                              types.PLAYER_B_KING) and
                4<=x<=5):
                attributeCount["centerPieces"] -= 1

            # attribute "flankPieces"
            if (theGame.gameState[x][y] in (types.PLAYER_A_REGULAR,
                                            types.PLAYER_A_KING) and
                (2<=x<=3 or 6<=x<=7)):
                attributeCount["flankPieces"] += 1
            elif (theGame.gameState[x][y] in (types.PLAYER_B_REGULAR,
                                              types.PLAYER_B_KING) and
                (2<=x<=3 or 6<=x<=7)):
                attributeCount["flankPieces"] -= 1

            # attribute "edgePieces"
            if (theGame.gameState[x][y] in (types.PLAYER_A_REGULAR,
                                            types.PLAYER_A_KING) and
                (0<=x<=1 or 8<=x<=9)):
                attributeCount["edgePieces"] += 1
            elif (theGame.gameState[x][y] in (types.PLAYER_B_REGULAR,
                                              types.PLAYER_B_KING) and
                (0<=x<=1 or 8<=x<=9)):
                attributeCount["edgePieces"] -= 1

            # attribute "midPieces"
            if (theGame.gameState[x][y] in (types.PLAYER_A_REGULAR,
                                            types.PLAYER_A_KING) and
                3<=y<=6):
                attributeCount["midPieces"] += 1
            elif (theGame.gameState[x][y] in (types.PLAYER_B_REGULAR,
                                              types.PLAYER_B_KING) and
                3<=y<=6):
                attributeCount["midPieces"] -= 1

    theGame.score = (
           weightValues["regularPieces"] * attributeCount["regularPieces"] +
           weightValues["kingPieces"] * attributeCount["kingPieces"] +
           weightValues["centerPieces"] * attributeCount["centerPieces"] +
           weightValues["flankPieces"] * attributeCount["flankPieces"] +
           weightValues["edgePieces"] * attributeCount["edgePieces"] +
           weightValues["midPieces"] * attributeCount["midPieces"])



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
    if (theGame.getState(pieceLocation) in (types.PLAYER_A_KING,
                                            types.PLAYER_B_KING)):
        # find king captures. if there are none, then keep any noncaptures
        # that are found
        moveList.extend(getCapturesForKingPiece(theGame,
                                                pieceLocation,
                                                playerAToPlay))
    elif (theGame.getState(pieceLocation) in (types.PLAYER_A_REGULAR,
                                              types.PLAYER_B_REGULAR)):
        moveList.extend(getCapturesForRegularPiece(theGame,
                                                   pieceLocation,
                                                   playerAToPlay))
    return moveList

def getCapturesForKingPiece(theGame,
                            pieceLocation,
                            playerAToPlay,
                            enableBackwardsCapture=True):
    if not enableBackwardsCapture:
        backwardsDelta = (-1*theGame.deltaLastMoved[0],
                          -1*theGame.deltaLastMoved[1])
    else:
        backwardsDelta = None

    # step #1: get a list of all the regular moves
    # step #2: find moves that have captures in the SAME DIRECTION
    # step #3: save moves to filteredList. will only ever be 0<=x<=4 results
    # TODO: Move to seperate method and add unit tests
    captureList = []
    if (theGame.getState(pieceLocation) is types.PLAYER_A_KING
            and playerAToPlay):
        captureList.extend(getLastMoveInEachDirection(theGame,
                                                      pieceLocation,
                                                      backwardsDelta))
    elif (theGame.getState(pieceLocation) is types.PLAYER_B_KING
            and not playerAToPlay):
        captureList.extend(getLastMoveInEachDirection(theGame,
                                                      pieceLocation,
                                                      backwardsDelta))
    else:
        return captureList

    # step #4: for each move get list of landing squares in direction of cap
    # step #4a: collect these moves into a finalResult
    # TODO: Move to seperate method and add unit tests
    deltaAndCaptureList = []
    for board in captureList:
        delta = board.deltaLastMoved
        direction = getDirectionFromDelta(delta)

        #uses pieceLastMoved (where piece stopped) and direction, to check cap
        if rules.isACaptureP(board,
                             board.pieceLastMoved,
                             direction,
                             playerAToPlay):
            endCoordinate = rules.getCaptureCoordinateFromDirection(
                board.pieceLastMoved,
                direction)
            rules.makeCapture(board, board.pieceLastMoved, endCoordinate)
            deltaAndCaptureList.append(board)

    # this gets non capture moves in a direction. reconcile with steps?
    # TODO: Move to seperate method and add unit tests
    moveList = []
    for maxMove in deltaAndCaptureList:
        moveList.append(transferNode(maxMove))

        result = getAllNoncaptureMovesForKingPiece(maxMove,
            maxMove.pieceLastMoved,
            [maxMove.deltaLastMoved,])

        moveList.extend(result)

    if len(moveList) is 0:
        return moveList

    # step #5: for each landing square, go to step #1
    # TODO: Move to seperate method and add unit tests
    allMoves = []
    for move in moveList:
        allMoves.append(transferNode(move))

        allMoves.extend(getCapturesForKingPiece(move,
            move.pieceLastMoved,
            playerAToPlay,
            False))

    # step #6: once all captures have been collected, filter by most caps
    # TODO: Move to seperate method and add unit tests
    mostCaptureMoves = []
    opposingPlayer = not playerAToPlay
    keyFunction = lambda x: x.getPieceCount(opposingPlayer)
    minimum = min(allMoves, key=keyFunction).getPieceCount(opposingPlayer)
    minimumIndices = [i for i, v in enumerate(allMoves)
        if v.getPieceCount(opposingPlayer) == minimum]
    for index in minimumIndices:
        mostCaptureMoves.append(allMoves[index])

    # step #7: remove duplicates
    # Non-optimal linear search for uniqueness
    finalMoves = []
    for board in mostCaptureMoves:
        if board not in finalMoves:
            finalMoves.append(board)
    return finalMoves

def getLastMoveInEachDirection(theGame,
                               pieceLocation,
                               skipDelta=None):
    """ Checks 4 directions king could move; returns last move in each dir """
    moveList = []
    deltaPairs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for deltaPair in deltaPairs:
        if deltaPair == skipDelta:
            continue
        deltaAsList = []
        deltaAsList.append(deltaPair)
        result = getAllNoncaptureMovesForKingPiece(theGame,
                                                   pieceLocation,
                                                   deltaAsList)
        if len(result) > 0:
            lastBoard = result[len(result)-1]
            lastBoard.deltaLastMoved = deltaPair
            moveList.append(lastBoard)
        else:
            lastBoard = transferNode(theGame)
            lastBoard.pieceLastMoved = pieceLocation
            lastBoard.deltaLastMoved = deltaPair
            moveList.append(lastBoard)
    return moveList

def getDirectionFromDelta(delta):
    """ Gets a direction from x/y delta pair """
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
        try:
            moveList.extend(getDiagonalNonCaptureMovesForKing(theGame,
                                                              pieceLocation,
                                                              deltaPair[0],
                                                              deltaPair[1]))
        except ValueError:
            continue
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
        newMove = makePieceMove(theGame, newPiece, startingLocation)
        newMove.pieceLastMoved = newPiece
        resultingMoves.append(newMove)
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
    resultNode.pieceLastMoved = startNode.pieceLastMoved
    resultNode.deltaLastMoved = startNode.deltaLastMoved
    for x in range(0, 10):
        for y in range(0, 10):
            resultNode.gameState[x][y] = startNode.gameState[x][y]
    return resultNode
