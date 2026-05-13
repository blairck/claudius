# Script to read in positions.jsonl file from gather.py. For each position, it adds a groundTruth position and writes to a new file evalCases.jsonl

ANALYSIS_SEARCH_PLY = 4 # How deep to analyze each position to determine ground truth
EVAL_CASE_SCHEMA = {"startGameNode": [[]], "groundTruthGameNode": [[]]} # eval case schema