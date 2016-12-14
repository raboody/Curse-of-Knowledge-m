######################

# tests our hypothesis space generators

######################

from HypothesisGenerators import *

TestA = ['X']
TestB = ['A', 'B']
HypothesisList = [ordered_AND, ordered_AND_OR, unordered_AND, unordered_OR, unordered_AND_OR]

for i in HypothesisList:
    print(i(['A', 'X', 'C']))
    print("")


