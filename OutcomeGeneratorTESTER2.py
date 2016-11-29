from OutcomeGenerator import *
from HypothesisGenerators import *
from ActionSpaceGenerator import *
#from OutcomeGeneratorTESTER1 import *

blocks = ['A', 'B', 'C', 'D']

def Tester(Hypotheses, Actions):
    for hypothesis in Hypotheses:
        for action in Actions:
            print(GetOutcome(hypothesis, action, 1))

print("action space is: ", "{}".format(action_space(blocks)))
print("hypothesis space is: ", "{}".format(ordered_AND_OR(blocks)))
Tester(ordered_AND_OR(blocks), action_space(blocks))
