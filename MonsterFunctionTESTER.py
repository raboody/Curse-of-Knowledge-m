import random 
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *
from ActionSpaceUpdater import *
from MonsterFunction import * 


machine_blocks = ['A', 'B', 'C', 'D', 'E']



print(MonsterFunction(
    action_space(machine_blocks),       # action space
    ['B', 'E', 'AND'],                  # True hypothesis
    unordered_AND_OR(machine_blocks),        # hypothesis space
    1
    ))
    
