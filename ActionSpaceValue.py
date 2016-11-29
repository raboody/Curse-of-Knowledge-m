from ActionSpaceGenerator import *
from ActionValueGenerator import*
from HypothesisGenerators import *
from OutcomeGenerator import *


Hypothesis0 = Action0 = []
Hypothesis1 = Action1 = ['A']
Hypothesis2 = Action2 = ['B']
Hypothesis3 = Action3 = ['C']
Hypothesis4 = Action4 = ['A', 'B']
Hypothesis5 = Action5 = ['A', 'C']
Hypothesis6 = Action6 = ['B', 'C']
Hypothesis7 = Action7 = ['A', 'B', 'C']


def GetActionSpaceValue(action_space, true_hypothesis, hypothesis_space):
    ValueList = []

    print("Action space is: ", "{}".format(action_space))
    print("hypothesis space is: ", "{}".format(hypothesis_space))
    
    for action in action_space:
        outcome = GetOutcome(true_hypothesis, action, 1)
        currentValue, newHypothesis = ValueFunction(action, outcome, true_hypothesis, hypothesis_space, 1)
        ValueList.append(currentValue)
        print("Current hypotheses are:", "{}".format(newHypothesis))
        print("Current value list: ", "{}".format(ValueList))
    return action_space, ValueList



print(GetActionSpaceValue(
    action_space(machine_blocks),   # all possible actions (action space)
    Hypothesis4,                    # true hypothesis (from ActionValueTESTER)
    ordered_AND_OR(machine_blocks), # hypothesis space (all possible hypotheses)
    ))
    
    
