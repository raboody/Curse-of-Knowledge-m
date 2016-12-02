from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *


Hypothesis0 = Action0 = []
Hypothesis1 = Action1 = ['A', 'ANDOR']
Hypothesis2 = Action2 = ['B', 'ANDOR']
Hypothesis3 = Action3 = ['C', 'ANDOR']
Hypothesis4 = Action4 = ['A', 'B', 'AND']
Hypothesis4_1 = Action4_1 = ['A', 'B', 'OR']

                               
Hypothesis5 = Action5 = ['A', 'C']
Hypothesis6 = Action6 = ['B', 'C']
Hypothesis7 = Action7 = ['A', 'B', 'C']


hypothesis_space = [[], ['B', 'ANDOR'], ['A', 'B', 'AND'], ['B', 'C', 'AND'], ['A', 'B', 'C', 'AND']]

machine_blocks = ['A', 'B', 'C', 'D', 'E']


print(ValueFunction(
    ['B', 'E'],           # action
    GetOutcome(['B', 'E', 'AND'], ['B', 'E'] ,0),    # outcome
    ['B', 'E', 'AND'],                      # true hypothesis
    unordered_AND_OR(machine_blocks),       # hypothesis space
    0                                       # verbose (0 = off, 1 = on)
    ))

