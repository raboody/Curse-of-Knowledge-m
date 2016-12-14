import random 
from BestTeachSequence import *



machine_blocks = ['A', 'B', 'C', 'D', 'E']



print(BestTeachSequence(
    action_space(machine_blocks),       # action space
    ['B', 'E', 'AND'],                  # True hypothesis
    unordered_AND(machine_blocks),        # hypothesis space
    0
    ))
    
