from CompleteActionSpaceValue import *


Hypothesis0 = Action0 = []
Hypothesis1 = Action1 = ['A']
Hypothesis2 = Action2 = ['B']
Hypothesis3 = Action3 = ['C']
Hypothesis4 = Action4 = ['A', 'B']
Hypothesis5 = Action5 = ['A', 'C']
Hypothesis6 = Action6 = ['B', 'C']
Hypothesis7 = Action7 = ['A', 'B', 'C']



print(GetActionSpaceValue(
    action_space(machine_blocks),   # all possible actions (action space)
    Hypothesis4,                    # true hypothesis (from ActionValueTESTER)
    ordered_AND_OR(machine_blocks), # hypothesis space (all possible hypotheses)
    0                               # verbose (0 = off, 1 = on)
    ))
    


