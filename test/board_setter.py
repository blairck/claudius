starting_position = [
"0     |b|   |b|   |b|   |b|   |b|"
"9  |b|   |b|   |b|   |b|   |b|   "
"8     |b|   |b|   |b|   |b|   |b|"
"7  |b|   |b|   |b|   |b|   |b|   "
"6     |||   |||   |||   |||   |||"
"5  |||   |||   |||   |||   |||   "
"4     |a|   |a|   |a|   |a|   |a|"
"3  |a|   |a|   |a|   |a|   |a|   "
"2     |a|   |a|   |a|   |a|   |a|"
"1  |a|   |a|   |a|   |a|   |a|   "
""
"    1  2  3  4  5  6  7  8  9  0"
]

#validate_board(starting_position) = True

def validate_board(board_description):
    if 9 < len(board_description) < 13:
        return True
    else:
        return False