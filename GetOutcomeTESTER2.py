######################

# Tests GetOutcome; input is a hypothesis space & action space of any size
# (more comprehensive tester)

######################

from GetOutcome import *
from HypothesisGenerators import *
from action_space import *


blocks = ['A', 'B', 'C']

def Tester(Hypotheses, Actions):
    for hypothesis in Hypotheses:
        for action in Actions:
            print(GetOutcome(hypothesis, action, 1))


print("action space is: ", "{}".format(action_space(blocks)))
print("hypothesis space is: ", "{}".format(ordered_AND_OR(blocks)))
Tester(ordered_AND_OR(blocks), action_space(blocks))
