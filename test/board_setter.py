from res import types
from src import coordinate
from src import gamenode

starting_position = [
"  1  2  3  4  5  6  7  8  9  0",
"0    b     b     b     b     b 0",
"9 b     b     b     b     b    9",
"8    b     b     b     b     b 8",
"7 b     b     b     b     b    7",
"6    .     .     .     .     . 6",
"5 .     a     .     .     .    5",
"4    a     .     a     a     a 4",
"3 a     a     a     a     a    3",
"2    a     a     a     a     a 2",
"1 a     a     a     a     a    1",
"  1  2  3  4  5  6  7  8  9  0",
]

def parse_board_input(description):
    gnObject1 = gamenode.GameNode()

    # Do item #0 of board_description. This corresponds to y=10 on board
    # Even:
    # coordinate x = 2 * j
    # coordinate y = 10 - i
    # description x = i
    # description y = 6 * j - 1
    # Odd:
    # coordinate x = 2 * j - 1
    # coordinate y = 10 - i
    # description x = i
    # description y = 6 * j - 4
    gnObject1.setState(coordinate.Coordinate(2, 10),
                       types.getPieceIntValueFromChar(description[0][5]))
    gnObject1.setState(coordinate.Coordinate(4, 10),
                       types.getPieceIntValueFromChar(description[0][11]))
    gnObject1.setState(coordinate.Coordinate(6, 10),
                       types.getPieceIntValueFromChar(description[0][17]))
    gnObject1.setState(coordinate.Coordinate(8, 10),
                       types.getPieceIntValueFromChar(description[0][23]))
    gnObject1.setState(coordinate.Coordinate(10, 10),
                       types.getPieceIntValueFromChar(description[0][29]))

    # Do item #1 of board_description. This corresponds to y=9 on board
    gnObject1.setState(coordinate.Coordinate(1, 9),
                       types.getPieceIntValueFromChar(description[1][2]))
    gnObject1.setState(coordinate.Coordinate(3, 9),
                       types.getPieceIntValueFromChar(description[1][8]))
    gnObject1.setState(coordinate.Coordinate(5, 9),
                       types.getPieceIntValueFromChar(description[1][14]))
    gnObject1.setState(coordinate.Coordinate(7, 9),
                       types.getPieceIntValueFromChar(description[1][20]))
    gnObject1.setState(coordinate.Coordinate(9, 9),
                       types.getPieceIntValueFromChar(description[1][26]))

    # Do item #2 of board_description. This corresponds to y=8 on board
    gnObject1.setState(coordinate.Coordinate(2, 8),
                       types.getPieceIntValueFromChar(description[2][5]))
    gnObject1.setState(coordinate.Coordinate(4, 8),
                       types.getPieceIntValueFromChar(description[2][11]))
    gnObject1.setState(coordinate.Coordinate(6, 8),
                       types.getPieceIntValueFromChar(description[2][17]))
    gnObject1.setState(coordinate.Coordinate(8, 8),
                       types.getPieceIntValueFromChar(description[2][23]))
    gnObject1.setState(coordinate.Coordinate(10, 8),
                       types.getPieceIntValueFromChar(description[2][29]))

    # Do item #3 of board_description. This corresponds to y=7 on board
    gnObject1.setState(coordinate.Coordinate(1, 7),
                       types.getPieceIntValueFromChar(description[3][2]))
    gnObject1.setState(coordinate.Coordinate(3, 7),
                       types.getPieceIntValueFromChar(description[3][8]))
    gnObject1.setState(coordinate.Coordinate(5, 7),
                       types.getPieceIntValueFromChar(description[3][14]))
    gnObject1.setState(coordinate.Coordinate(7, 7),
                       types.getPieceIntValueFromChar(description[3][20]))
    gnObject1.setState(coordinate.Coordinate(9, 7),
                       types.getPieceIntValueFromChar(description[3][26]))

    # Do item #4 of board_description. This corresponds to y=6 on board
    gnObject1.setState(coordinate.Coordinate(2, 6),
                       types.getPieceIntValueFromChar(description[4][5]))
    gnObject1.setState(coordinate.Coordinate(4, 6),
                       types.getPieceIntValueFromChar(description[4][11]))
    gnObject1.setState(coordinate.Coordinate(6, 6),
                       types.getPieceIntValueFromChar(description[4][17]))
    gnObject1.setState(coordinate.Coordinate(8, 6),
                       types.getPieceIntValueFromChar(description[4][23]))
    gnObject1.setState(coordinate.Coordinate(10, 6),
                       types.getPieceIntValueFromChar(description[4][29]))

    # Do item #5 of board_description. This corresponds to y=5 on board
    gnObject1.setState(coordinate.Coordinate(1, 5),
                       types.getPieceIntValueFromChar(description[5][2]))
    gnObject1.setState(coordinate.Coordinate(3, 5),
                       types.getPieceIntValueFromChar(description[5][8]))
    gnObject1.setState(coordinate.Coordinate(5, 5),
                       types.getPieceIntValueFromChar(description[5][14]))
    gnObject1.setState(coordinate.Coordinate(7, 5),
                       types.getPieceIntValueFromChar(description[5][20]))
    gnObject1.setState(coordinate.Coordinate(9, 5),
                       types.getPieceIntValueFromChar(description[5][26]))

    # Do item #6 of board_description. This corresponds to y=4 on board
    gnObject1.setState(coordinate.Coordinate(2, 4),
                       types.getPieceIntValueFromChar(description[6][5]))
    gnObject1.setState(coordinate.Coordinate(4, 4),
                       types.getPieceIntValueFromChar(description[6][11]))
    gnObject1.setState(coordinate.Coordinate(6, 4),
                       types.getPieceIntValueFromChar(description[6][17]))
    gnObject1.setState(coordinate.Coordinate(8, 4),
                       types.getPieceIntValueFromChar(description[6][23]))
    gnObject1.setState(coordinate.Coordinate(10, 4),
                       types.getPieceIntValueFromChar(description[6][29]))

    # Do item #7 of board_description. This corresponds to y=3 on board
    gnObject1.setState(coordinate.Coordinate(1, 3),
                       types.getPieceIntValueFromChar(description[7][2]))
    gnObject1.setState(coordinate.Coordinate(3, 3),
                       types.getPieceIntValueFromChar(description[7][8]))
    gnObject1.setState(coordinate.Coordinate(5, 3),
                       types.getPieceIntValueFromChar(description[7][14]))
    gnObject1.setState(coordinate.Coordinate(7, 3),
                       types.getPieceIntValueFromChar(description[7][20]))
    gnObject1.setState(coordinate.Coordinate(9, 3),
                       types.getPieceIntValueFromChar(description[7][26]))

    # Do item #8 of board_description. This corresponds to y=2 on board
    gnObject1.setState(coordinate.Coordinate(2, 2),
                       types.getPieceIntValueFromChar(description[8][5]))
    gnObject1.setState(coordinate.Coordinate(4, 2),
                       types.getPieceIntValueFromChar(description[8][11]))
    gnObject1.setState(coordinate.Coordinate(6, 2),
                       types.getPieceIntValueFromChar(description[8][17]))
    gnObject1.setState(coordinate.Coordinate(8, 2),
                       types.getPieceIntValueFromChar(description[8][23]))
    gnObject1.setState(coordinate.Coordinate(10, 2),
                       types.getPieceIntValueFromChar(description[8][29]))

    # Do item #9 of board_description. This corresponds to y=1 on board
    gnObject1.setState(coordinate.Coordinate(1, 1),
                       types.getPieceIntValueFromChar(description[9][2]))
    gnObject1.setState(coordinate.Coordinate(3, 1),
                       types.getPieceIntValueFromChar(description[9][8]))
    gnObject1.setState(coordinate.Coordinate(5, 1),
                       types.getPieceIntValueFromChar(description[9][14]))
    gnObject1.setState(coordinate.Coordinate(7, 1),
                       types.getPieceIntValueFromChar(description[9][20]))
    gnObject1.setState(coordinate.Coordinate(9, 1),
                       types.getPieceIntValueFromChar(description[9][26]))
