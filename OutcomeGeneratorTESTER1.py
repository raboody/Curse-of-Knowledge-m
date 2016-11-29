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
    Hypothesis1,    # here choose a hypothesis
    Action3,       # here choose an action
    0               # verbose, 0 = off, 1 = on
      ))       
