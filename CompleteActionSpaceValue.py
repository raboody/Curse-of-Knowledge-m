from ActionSpaceGenerator import *
from ActionValueGenerator import*
from HypothesisGenerators import *
from OutcomeGenerator import *


def GetActionSpaceValue(action_space, true_hypothesis, hypothesis_space, verbose):
    ValueList = []
    if verbose == 1:
        print("Action space is: ", "{}".format(action_space))
        print("hypothesis space is: ", "{}".format(hypothesis_space))
        
    for action in action_space:
        outcome = GetOutcome(true_hypothesis, action, 0)
        currentValue, newHypothesis = ValueFunction(action, outcome, true_hypothesis, hypothesis_space, 1)
        ValueList.append(currentValue)
        if verbose == 1:
            print("Current hypotheses are:", "{}".format(newHypothesis))
            print("Current value list: ", "{}".format(ValueList))
    return action_space, ValueList




    
