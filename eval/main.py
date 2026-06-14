# Main script which optimizes ai weights performance against evaluation data set.
import os
import sys
import random


sys.path.append(os.getcwd())
from eval import common
from src import ai, types


def createListCombination(element_size, length):
    if element_size < 0 or length < 0:
        raise ValueError("element_size and length must be non-negative")

    if length == 0:
        return [[]]

    result = []
    child_combinations = createListCombination(element_size, length-1)

    for value in range(element_size):
        for combination in child_combinations:
            result.append([value] + combination)

    return result

# createListCombination

    


def getHillClimbingWeightDeltas(weights, increment=1):
    weightDeltas = []

    # regularPieces
    weightDeltas.append(ai.Weights(weights.regularPieces+increment,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces))
    weightDeltas.append(ai.Weights(weights.regularPieces-increment,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces))
    
    # kingPieces
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces+increment,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces))
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces-increment,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces))

    # centerPieces
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces+increment,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces))
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces-increment,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces))

    # flankPieces
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces+increment,
                                   weights.edgePieces,
                                   weights.midPieces))
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces-increment,
                                   weights.edgePieces,
                                   weights.midPieces))

    # edgePieces
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces+increment,
                                   weights.midPieces))
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces-increment,
                                   weights.midPieces))

    # midPieces
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces+increment))
    weightDeltas.append(ai.Weights(weights.regularPieces,
                                   weights.kingPieces,
                                   weights.centerPieces,
                                   weights.flankPieces,
                                   weights.edgePieces,
                                   weights.midPieces-increment))
    
    return weightDeltas


def _getAllMovesForPlayer(game, activePlayer):
    activePlayerBool = False
    if activePlayer == types.PLAYER_A_NAME:
        activePlayerBool = True
    
    return ai.getAllMovesForPlayer(game, activePlayerBool)


def getScoredGameMoves(game, activePlayer, weights):
    moves = _getAllMovesForPlayer(game, activePlayer)
    for move in moves:
        move.score = ai._evaluationFunction(move, weights)
    return moves


def getMaxScoreMoves(moves):
    maxMoves = []
    maxScore = None

    for move in moves:
        if maxScore is None:
            maxMoves.append(move)
            maxScore = move.score
        elif move.score > maxScore:
            maxMoves = [move]
            maxScore = move.score
        elif move.score == maxScore:
            maxMoves.append(move)
    
    return maxMoves


def evaluatePosition(startGameNode, groundTruthGameNode, activePlayer, weights):
    # This needs to take the start gn, create a list of all scored moves that are next,
    # identify the top 1 (ties not allowed) determine if the groundTruthGameNode is ==.
    moves = getScoredGameMoves(startGameNode, activePlayer, weights)
    maxScoreMoves = getMaxScoreMoves(moves)

    if len(maxScoreMoves) != 1:
        return False
    elif groundTruthGameNode in maxScoreMoves:
        return True

    return False

def evaluateWeights(positions, weights):
    score = 0
    for _, position in enumerate(positions):
        startGameNode = common.readFlatGameState(position["startGameNode"])
        groundTruthGameNode = common.readFlatGameState(position["groundTruthGameNode"])

        if evaluatePosition(startGameNode,
                            groundTruthGameNode,
                            position["activePlayer"],
                            weights):
            score += 1

    percentCorrect = 100*(score/len(positions))
    return percentCorrect


if __name__ == "__main__":
    import random
    positions = common.readGatherDataFile("eval/data/evaluationData.jsonl")

    globalBestScore = 0
    globalBestWeights = None
    restart = 0

    while True:
        restart += 1
        currentWeights = ai.Weights(
            random.randint(0, 50),
            random.randint(0, 50),
            random.randint(0, 50),
            random.randint(0, 50),
            random.randint(0, 50),
            random.randint(0, 50),
        )
        currentScore = evaluateWeights(positions, currentWeights)
        # print(f"[restart {restart}] start: {currentScore:.1f}% for {currentWeights}")
        step = 0

        while True:
            step += 1
            candidates = getHillClimbingWeightDeltas(currentWeights, 2)

            bestResult = currentScore
            bestWeights = None

            for weight in candidates:
                result = evaluateWeights(positions, weight)
                if result > bestResult:
                    bestResult = result
                    bestWeights = weight

            if bestWeights is None:
                # print(f"[restart {restart}] step {step}: local max at {currentScore:.1f}%")
                break

            currentScore = bestResult
            currentWeights = bestWeights

            improved_global = currentScore > globalBestScore
            if improved_global:
                globalBestScore = currentScore
                globalBestWeights = currentWeights

            # tag = " *** NEW BEST ***" if improved_global else ""
            # print(f"[restart {restart}] step {step}: {currentScore:.1f}% for {currentWeights}{tag}")

        if currentScore > globalBestScore:
            globalBestScore = currentScore
            globalBestWeights = currentWeights
            print(f"[restart {restart}] *** NEW BEST: {globalBestScore:.1f}% for {globalBestWeights} ***")

        # print(f"[restart {restart}] global best so far: {globalBestScore:.1f}% for {globalBestWeights}")


