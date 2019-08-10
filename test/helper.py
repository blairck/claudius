""" Helper functions for unit tests """

from contextlib import contextmanager
from io import StringIO
import sys

@contextmanager
def captured_output():
    """ Redirects stdout to StringIO so we can inspect Print statements """
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

simpleCountPiecesDescription = [
    "  1  2  3  4  5  6  7  8  9  0",
    "0    .     .     .     .     . 0",
    "9 a     a     .     .     .    9",
    "8    b     .     .     .     . 8",
    "7 .     .     .     .     .    7",
    "6    .     .     .     .     . 6",
    "5 .     .     .     .     .    5",
    "4    .     .     .     .     . 4",
    "3 .     .     .     .     .    3",
    "2    .     .     .     .     . 2",
    "1 .     .     .     .     .    1",
    "  1  2  3  4  5  6  7  8  9  0",]

simpleCaptureBoardDescription = [
    "  1  2  3  4  5  6  7  8  9  0",
    "0    .     .     .     .     . 0",
    "9 a     a     .     b     .    9",
    "8    b     .     .     a     . 8",
    "7 .     .     .     .     .    7",
    "6    .     .     .     .     . 6",
    "5 .     .     .     .     .    5",
    "4    .     .     .     .     . 4",
    "3 .     .     .     .     .    3",
    "2    .     .     .     .     . 2",
    "1 .     .     .     .     .    1",
    "  1  2  3  4  5  6  7  8  9  0",]

piecePromotions = [
    "  1  2  3  4  5  6  7  8  9  0",
    "0    .     .     .     .     . 0",
    "9 .     a     .     B     A    9",
    "8    a     .     .     .     . 8",
    "7 .     .     .     .     .    7",
    "6    .     .     .     .     . 6",
    "5 .     .     .     b     .    5",
    "4    .     .     .     .     . 4",
    "3 .     .     .     .     .    3",
    "2    b     A     .     B     . 2",
    "1 .     .     .     .     .    1",
    "  1  2  3  4  5  6  7  8  9  0",]

multipleKings = [
    "  1  2  3  4  5  6  7  8  9  0",
    "0    .     .     .     .     . 0",
    "9 .     .     .     .     .    9",
    "8    B     A     .     B     . 8",
    "7 .     A     .     B     .    7",
    "6    B     A     B     B     . 6",
    "5 .     .     .     .     .    5",
    "4    .     .     A     A     . 4",
    "3 .     B     .     A     .    3",
    "2    .     .     .     .     . 2",
    "1 .     .     .     .     .    1",
    "  1  2  3  4  5  6  7  8  9  0",]
