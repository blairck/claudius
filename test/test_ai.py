""" Tests for the AI module """

import unittest

# pylint: disable=import-error
import helper
from res import types
from src import ai
from src import coordinate
from src import gamenode
from src import boardParser

class TestAI(unittest.TestCase):
    """ Tests for the AI module """

    def test_getNoncaptureMovesForPiece_KingA(self):
        board = boardParser.parseBoardInput(helper.getNoncaptureMovesForPiece)
        pieceLocation = coordinate.Coordinate(2, 8)
        playerAToPlay = True

        actualResult = ai.getNoncaptureMovesForPiece(board,
                                                     pieceLocation,
                                                     playerAToPlay)

        expectedResultLength = 4

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getNoncaptureMovesForPiece_KingB(self):
        board = boardParser.parseBoardInput(helper.getNoncaptureMovesForPiece)
        pieceLocation = coordinate.Coordinate(7, 7)
        playerAToPlay = False

        actualResult = ai.getNoncaptureMovesForPiece(board,
                                                     pieceLocation,
                                                     playerAToPlay)

        expectedResultLength = 3

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getNoncaptureMovesForPiece_RegularA(self):
        board = boardParser.parseBoardInput(helper.getNoncaptureMovesForPiece)
        pieceLocation = coordinate.Coordinate(3, 5)
        playerAToPlay = True

        actualResult = ai.getNoncaptureMovesForPiece(board,
                                                     pieceLocation,
                                                     playerAToPlay)

        expectedResultLength = 2

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getNoncaptureMovesForPiece_RegularB(self):
        board = boardParser.parseBoardInput(helper.getNoncaptureMovesForPiece)
        pieceLocation = coordinate.Coordinate(7, 3)
        playerAToPlay = False

        actualResult = ai.getNoncaptureMovesForPiece(board,
                                                     pieceLocation,
                                                     playerAToPlay)

        expectedResultLength = 1

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getNoncaptureMovesForPiece_None(self):
        board = boardParser.parseBoardInput(helper.getNoncaptureMovesForPiece)
        pieceLocation = coordinate.Coordinate(3, 5)
        playerAToPlay = False

        actualResult = ai.getNoncaptureMovesForPiece(board,
                                                     pieceLocation,
                                                     playerAToPlay)

        expectedResultLength = 0

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getNoncaptureMovesForKingPiece_1MoveAvailable(self):
        board = boardParser.parseBoardInput(helper.multipleKings)
        pieceLocation = coordinate.Coordinate(7, 7)

        actualResult = ai.getNoncaptureMovesForKingPiece(board,
                                                         pieceLocation)

        expectedResultLength = 1

        self.assertEqual(expectedResultLength, len(actualResult))
        self.assertEqual(types.EMPTY, actualResult[0].getState(pieceLocation))
        self.assertEqual(types.PLAYER_B_KING,
                         actualResult[0].getState(coordinate.Coordinate(6, 8)))

    def test_getNoncaptureMovesForKingPiece_2MoveAvailable(self):
        board = boardParser.parseBoardInput(helper.multipleKings)
        pieceLocation = coordinate.Coordinate(7, 3)

        actualResult = ai.getNoncaptureMovesForKingPiece(board,
                                                         pieceLocation)

        expectedResultLength = 2

        self.assertEqual(expectedResultLength, len(actualResult))
        self.assertEqual(types.EMPTY, actualResult[0].getState(pieceLocation))
        self.assertEqual(types.PLAYER_A_KING,
                         actualResult[0].getState(coordinate.Coordinate(6, 2)))
        self.assertEqual(types.PLAYER_A_KING,
                         actualResult[1].getState(coordinate.Coordinate(8, 2)))

    def test_getNoncaptureMovesForKingPiece_4MoveAvailable(self):
        board = boardParser.parseBoardInput(helper.multipleKings)
        pieceLocation = coordinate.Coordinate(3, 3)

        actualResult = ai.getNoncaptureMovesForKingPiece(board,
                                                         pieceLocation)

        expectedResultLength = 4

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getNoncaptureMovesForKingPiece_0MoveAvailable(self):
        board = boardParser.parseBoardInput(helper.multipleKings)
        pieceLocation = coordinate.Coordinate(3, 7)

        actualResult = ai.getNoncaptureMovesForKingPiece(board,
                                                         pieceLocation)

        expectedResultLength = 0

        self.assertEqual(expectedResultLength, len(actualResult))

    def test_getTupleOfAllCoordinates(self):
        """ Check that all the legal coordinates are generated """
        actualResult = len(ai.getTupleOfAllCoordinates())
        expectedResult = 50
        self.assertEqual(actualResult, expectedResult)

    def test_getAllMovesForPlayer_good(self):
        """ Check that capture moves take precedence over non-captures """
        board_description = [
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     .     .     . 0",
            "9 .     .     .     .     .    9",
            "8    .     .     .     .     . 8",
            "7 .     .     .     .     .    7",
            "6    .     b     .     .     . 6",
            "5 .     .     a     a     .    5",
            "4    .     .     .     .     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",]
        board = boardParser.parseBoardInput(board_description)
        #capturingPiece = coordinate.Coordinate(3, 5)

        expectedLength = 1
        movesList = ai.getAllMovesForPlayer(board, True)

        actualMovesListLength = len(movesList)

        self.assertEqual(expectedLength, actualMovesListLength)

    def test_getNoncaptureMovesForRegularPiece_2_moves(self):
        """ Test that regular piece has to possible moves """
        gnObject = gamenode.GameNode()
        pieceLocation = coordinate.Coordinate(4, 4)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = ai.getNoncaptureMovesForRegularPiece(gnObject,
                                                            pieceLocation,
                                                            True)
        expectedResultLength = 2
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getNoncaptureMovesForRegularPiece_1_move(self):
        """ Test regular piece on the edge of the board, which has 1 move """
        gnObject = gamenode.GameNode()
        pieceLocation = coordinate.Coordinate(10, 4)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = ai.getNoncaptureMovesForRegularPiece(gnObject,
                                                            pieceLocation,
                                                            True)
        expectedResultLength = 1
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getNoncaptureMovesForRegularPiece_0_moves(self):
        """ Test regular piece that is completely blocked from moving """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        pieceLocation = coordinate.Coordinate(1, 1)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)
        actualResult = ai.getNoncaptureMovesForRegularPiece(gnObject,
                                                            pieceLocation,
                                                            True)
        expectedResultLength = 0
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_destinationIsEmpty_true(self):
        """ Test when destination is Empty """
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(4, 6)
        actualResult = ai.destinationIsEmpty(gnObject, pieceDestination)
        expectedResult = True
        self.assertEqual(actualResult, expectedResult)

    def test_destinationIsEmpty_false(self):
        """ Test when destination is not Empty """
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(9, 3)
        gnObject.setState(pieceDestination, types.PLAYER_A_REGULAR)
        actualResult = ai.destinationIsEmpty(gnObject, pieceDestination)
        expectedResult = False
        self.assertEqual(actualResult, expectedResult)

    def test_makePieceMove_good(self):
        """ Test executing a happy-path piece move """
        # Given
        gnObject = gamenode.GameNode()
        pieceDestination = coordinate.Coordinate(9, 3)
        pieceLocation = coordinate.Coordinate(8, 2)
        gnObject.setState(pieceLocation, types.PLAYER_A_REGULAR)

        # When
        actualResult = ai.makePieceMove(gnObject,
                                        pieceDestination,
                                        pieceLocation)

        # Then
        actualResultLocationType = actualResult.getState(pieceLocation)
        actualResultDestinationType = actualResult.getState(pieceDestination)
        expectedResultLocationType = types.EMPTY
        expectedResultDestinationType = types.PLAYER_A_REGULAR
        self.assertEqual(actualResultLocationType, expectedResultLocationType)
        self.assertEqual(actualResultDestinationType,
                         expectedResultDestinationType)

    def test_getAllMovesForPlayer_isPlayerA(self):
        """ Test getting all moves for player A """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        actualResult = ai.getAllMovesForPlayer(gnObject, True)
        expectedResultLength = 9
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getAllMovesForPlayer_isPlayerB(self):
        """ Test getting all moves for player B """
        gnObject = gamenode.GameNode()
        gnObject.createStartingPosition()
        actualResult = ai.getAllMovesForPlayer(gnObject, False)
        expectedResultLength = 9
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getAllMovesForPlayer_1_move_2_players(self):
        """ Test getting moves for a particular player when both players have
        legal moves """
        # Given
        gnObject = gamenode.GameNode()
        pieceLocationA = coordinate.Coordinate(6, 2)
        gnObject.setState(pieceLocationA, types.PLAYER_A_REGULAR)
        pieceLocationB = coordinate.Coordinate(5, 7)
        gnObject.setState(pieceLocationB, types.PLAYER_B_REGULAR)

        # When
        actualResult = ai.getAllMovesForPlayer(gnObject, False)

        # Then
        expectedResultLength = 2
        self.assertEqual(len(actualResult), expectedResultLength)

    def test_getCapturesForRegularPiece_good(self):
        """ Check valid captures are returned for a regular piece """
        board_description = [
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     .     .     . 0",
            "9 .     .     .     .     .    9",
            "8    .     .     B     b     . 8",
            "7 .     .     .     .     .    7",
            "6    A     b     b     b     . 6",
            "5 .     a     .     .     .    5",
            "4    a     B     .     b     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",]
        board = boardParser.parseBoardInput(board_description)
        capturingPiece = coordinate.Coordinate(3, 5)

        expectedLength = 2
        movesList = ai.getCapturesForRegularPiece(board,
                                                  capturingPiece,
                                                  True)
        actualMovesListLength = len(movesList)

        self.assertEqual(expectedLength, actualMovesListLength)
        # Since we don't want to assume an order of the moves being returned,
        # just assert here on the common features of both legal moves
        self.assertEqual(types.EMPTY,
                         movesList[0].getState(coordinate.Coordinate(4, 6)))
        self.assertEqual(types.EMPTY,
                         movesList[0].getState(coordinate.Coordinate(6, 8)))
        self.assertEqual(types.EMPTY,
                         movesList[0].getState(coordinate.Coordinate(8, 8)))
        self.assertEqual(types.EMPTY,
                         movesList[0].getState(coordinate.Coordinate(8, 6)))
        self.assertEqual(types.EMPTY,
                         movesList[1].getState(coordinate.Coordinate(4, 6)))
        self.assertEqual(types.EMPTY,
                         movesList[1].getState(coordinate.Coordinate(6, 8)))
        self.assertEqual(types.EMPTY,
                         movesList[1].getState(coordinate.Coordinate(8, 8)))
        self.assertEqual(types.EMPTY,
                         movesList[1].getState(coordinate.Coordinate(8, 6)))

    def test_removeBoardDuplicates(self):
        """ Dedupe list of 2 identical boards """
        board = boardParser.parseBoardInput([
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     .     .     . 0",
            "9 .     .     .     .     .    9",
            "8    .     .     .     .     . 8",
            "7 .     .     .     .     .    7",
            "6    .     .     .     .     . 6",
            "5 .     .     .     .     .    5",
            "4    .     .     .     .     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",])
        list_of_boards = [board, board,]

        expectedLength = 1
        resultList = ai.removeBoardDuplicates(list_of_boards)
        self.assertEqual(expectedLength, len(resultList))

    def test_filterForFewestOpposingPieces(self):
        """ Filter list of boards to one with fewest 'a' pieces, board2 """
        board1 = boardParser.parseBoardInput([
            "  1  2  3  4  5  6  7  8  9  0",
            "0    a     .     .     .     . 0",
            "9 .     b     .     .     .    9",
            "8    a     .     .     .     . 8",
            "7 .     b     .     .     .    7",
            "6    a     .     .     .     . 6",
            "5 .     b     .     .     .    5",
            "4    .     .     .     .     . 4",
            "3 .     b     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     b     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",])
        board2 = boardParser.parseBoardInput([
            "  1  2  3  4  5  6  7  8  9  0",
            "0    .     .     b     .     . 0",
            "9 .     .     a     .     .    9",
            "8    .     .     .     .     . 8",
            "7 .     .     a     .     .    7",
            "6    .     .     .     .     . 6",
            "5 .     .     .     .     .    5",
            "4    .     .     .     .     . 4",
            "3 .     .     .     .     .    3",
            "2    .     .     .     .     . 2",
            "1 .     .     .     .     .    1",
            "  1  2  3  4  5  6  7  8  9  0",])
        list_of_boards = [board1, board2,]

        expectedLength = 1
        resultList = ai.filterForFewestOpposingPieces(list_of_boards, True)
        resultingPiece = coordinate.Coordinate(5, 7)
        self.assertEqual(expectedLength, len(resultList))
        self.assertEqual(types.PLAYER_A_REGULAR,
                         resultList[0].getState(resultingPiece))
