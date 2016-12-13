##################

# Tester for the ActionSpaceUpdater function

##################

from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *
from ActionSpaceUpdater import *


machine_blocks = ['A', 'B', 'C']

Hypothesis1 = ['C', 'ANDOR']
Hypothesis2 = ['A', 'C', 'OR']
Hypothesis3 = ['A', 'C', 'AND']

Action1 = ['C']
Action2 = ['A', 'B']
Action3 = ['A']
Action4 = ['A', 'C']
Action5 = ['A', 'B', 'C']

print(action_space_updater(action_space(machine_blocks), # Action space
                           Hypothesis1, # True hypothesis
                           [['B', 'ANDOR'], ['A', 'ANDOR'], ['B', 'C', 'AND']], # updated hypothesis space
                           0
                           ))
