## Claudius ##
### Description ###
Jaeger is a console-based implementation of checkers.

Project Status: This project is in development.

### Requirements ###
To use:
* Python 3.6 or later required
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

### Status ###
Functions to be ported and tested, organized by component
* AI                            0/6
* Connection                    0/5
* GameNode                      0/7
* HistoryNode                   0/11
* Rules                         0/14
* TOTAL                         0/43
