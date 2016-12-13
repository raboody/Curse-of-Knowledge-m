######################

# Tests the ChooseBestAction function

######################

from ChooseBestAction import *

machine_blocks = ['A', 'B', 'C', 'D', 'E'] 

print(ChooseBestAction(
    action_space(machine_blocks),   # all possible actions (action space)
    ['B', 'E', 'AND'],                    # true hypothesis (from ActionValueTESTER)
    ordered_AND(machine_blocks), # hypothesis space (all possible hypotheses)
    0,  # verbose (0 = off, 1 = on)
    0   # verbose2 (0 = off, 1 = on)
    ))
