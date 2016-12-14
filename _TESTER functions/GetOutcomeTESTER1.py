######################

# Tests GetOutcome; input is 1 action & 1 true hypothesis

######################


from GetOutcome import *
from HypothesisGenerators import *
from action_space import *

Hypothesis1 = ['C', 'ANDOR']
Hypothesis2 = ['A', 'C', 'OR']
Hypothesis3 = ['A', 'C', 'AND']

Action1 = ['C']
Action2 = ['A', 'B']
Action3 = ['A']
Action4 = ['A', 'C']
Action5 = ['A', 'B', 'C']

machine_blocks = ['A', 'B', 'C']

def GetOutcomeTESTER1(TrueHypothesis, action):
    print("True Hypothesis is: ", TrueHypothesis)
    print("action is: ", action)
    print("outcome is: ", GetOutcome(TrueHypothesis, action, 0))

GetOutcomeTESTER1(Hypothesis3, Action1)
