import random

# pylint: disable=import-error
from src import ai
from src import coordinate
from src import gamenode
from res import types

def getRandomBoard():
	# Max and min number of pieces that could be on the board for each side
	# Max is <20 (default starting number) to reduce pieces clumping together
	maxPieces = 18
	minPieces = 1

	# Number of pieces for player A
	# random int in range 1<=x<=20
	piecesA = getRandomInt(1, 20)
	# Number of pieces for player B
	# random int in range 1<=x<=20
	piecesB = getRandomInt(1, 20)
	# Whether player A has king or not
	# True or False
	kingForPlayerA = getKingOrNot()
	if kingForPlayerA:
		piecesA -= 1
	# Whether player B has king or not
	# True or False
	kingForPlayerB = getKingOrNot()
	if kingForPlayerB:
		piecesB -= 1

	board = gamenode.GameNode()
	possibleCoordinates = list(ai.getTupleOfAllCoordinates())
	random.shuffle(possibleCoordinates)

	if kingForPlayerA:
		board.setState(possibleCoordinates.pop(), types.PLAYER_A_KING)
	if kingForPlayerB:
		board.setState(possibleCoordinates.pop(), types.PLAYER_B_KING)

	for i in range(piecesA):
		board.setState(possibleCoordinates.pop(), types.PLAYER_A_REGULAR)
	for i in range(piecesB):
		board.setState(possibleCoordinates.pop(), types.PLAYER_B_REGULAR)

	return board

def getRandomInt(start, end):
	return random.randint(start, end)


def getKingOrNot():
	result = getRandomInt(0, 1)
	if result is 1:
		return True
	else:
		return False
