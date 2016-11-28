from OutcomeGenerator import *
from HypothesisGenerators import *
from ActionSpaceGenerator import *

Hypothesis1 = ['C', 'ANDOR']
Hypothesis2 = ['A', 'C', 'OR']
Hypothesis3 = ['A', 'C', 'AND']

Action1 = ['C']
Action2 = ['A', 'B']
Action3 = ['A']
Action4 = ['A', 'C']
Action5 = ['A', 'B', 'C']



print("action space is: ", "{}".format(action_space(machine_blocks)))
print("hypothesis space is: ", "{}".format(ordered_AND_OR(machine_blocks)))
print(GetOutcome(
    Hypothesis3,    # here choose a hypothesis
    Action5))       # here choose an action
