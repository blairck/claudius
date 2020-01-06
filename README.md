## Claudius ##
### Description ###
Claudius is a console-based implementation of checkers.

Project Status: Version 1.0.0 is released. This project is now in maintenance.

### Requirements ###
To use:
* Python 3.7 or later required
* Python 2 is not supported

### Setting Up For Players ###
Setting up:
* Install Python 3
* Download this repo (Green download button, upper right corner)
* Setup instructions for development are at the end of this document

## Setting Up For Development ##
Install extra requirements:
* Install Git
* Clone this repo
* Install Make to run the makefile commands
* Make a virtualenv for dependencies:
```
virtualenv env --python=python3
```
* Activate the virtualenv
* Install development requirements:
```
pip install -r requirements.txt
```
* Run the unit tests to make sure everything is set up:
```
make tests
```

### Quick start ###
Here is how to quickly get into a game:
* Follow the 'Setting Up For Players' instructions
* In the Claudius directory, run the command "python3 main.py"
* This what you'll see:
```
  1  2  3  4  5  6  7  8  9  0
0    b     b     b     b     b 0
9 b     b     b     b     b    9
8    b     b     b     b     b 8
7 b     b     b     b     b    7
6    .     .     .     .     . 6
5 .     .     .     .     .    5
4    a     a     a     a     a 4
3 a     a     a     a     a    3
2    a     a     a     a     a 2
1 a     a     a     a     a    1
  1  2  3  4  5  6  7  8  9  0
Enter a move:
```
* By default, you'll be playing as player A, which moves first. To make a move
* you'll need to provide the starting location and the ending location. For
* example, the move "84-95" (alternatively "8495") would result in this
* board position:
```
  1  2  3  4  5  6  7  8  9  0
0    b     b     b     b     b 0
9 b     b     b     b     b    9
8    b     b     b     b     b 8
7 b     b     b     b     b    7
6    .     .     .     .     . 6
5 .     .     .     .     a    5
4    a     a     a     .     a 4
3 a     a     a     a     a    3
2    a     a     a     a     a 2
1 a     a     a     a     a    1
  1  2  3  4  5  6  7  8  9  0
```
* Tip: If there is only 1 possible move with the ending location, you can just
type that. For example, you could type "15" which would make this move:
```
  1  2  3  4  5  6  7  8  9  0
0    b     b     b     b     b 0
9 b     b     b     b     b    9
8    b     b     b     b     b 8
7 b     b     b     b     b    7
6    .     .     .     .     . 6
5 a     .     .     .     .    5
4    .     a     a     a     a 4
3 a     a     a     a     a    3
2    a     a     a     a     a 2
1 a     a     a     a     a    1
  1  2  3  4  5  6  7  8  9  0
```
* To quit, type "quit()" or Ctrl-D.
* Feel free to change game settings (such as difficulty) in the main.py file
* and play again.
