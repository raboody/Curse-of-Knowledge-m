from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *


Hypothesis0 = Action0 = []
Hypothesis1 = Action1 = ['A']
Hypothesis2 = Action2 = ['B']
Hypothesis3 = Action3 = ['C']
Hypothesis4 = Action4 = ['A', 'B']
Hypothesis5 = Action5 = ['A', 'C']
Hypothesis6 = Action6 = ['B', 'C']
Hypothesis7 = Action7 = ['A', 'B', 'C']




print(GetOutcome(Hypothesis1, Action2, 1))
print("Our hypothesis space is: ", "{}".format(ordered_AND_OR(machine_blocks)))
print("###############")



print(ValueFunction(
    Action2,                                # action
    GetOutcome(Hypothesis1, Action2, 0),    # outcome
    Hypothesis1,                            # true hypothesis
    ordered_AND_OR(machine_blocks),         # hypothesis space
    0                                       # verbose (0 = off, 1 = on)
    ))

