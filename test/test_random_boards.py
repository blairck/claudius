""" Tests for the AI module """

import unittest

# pylint: disable=import-error,too-many-public-methods
import random_board_generator
from src import ai

class TestAI(unittest.TestCase):
    """ Tests for the AI module """

    def test_random_boards_player_A(self):
        try:
            for i in range(10):
                board = random_board_generator.getRandomBoard()
                ai.getAllMovesForPlayer(board, True)
        except Exception as e:
            print("test_random_boards_player_A failure!")
            board.print_board()
            raise e

    def test_random_boards_player_B(self):
        try:
            for i in range(10):
                board = random_board_generator.getRandomBoard()
                ai.getAllMovesForPlayer(board, False)
        except Exception as e:
            print("test_random_boards_player_B failure!")
            board.print_board()
            raise e
