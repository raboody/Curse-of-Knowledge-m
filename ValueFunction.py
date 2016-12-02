from action_space import *
from HypothesisGenerators import *
from GetOutcome import *


# for every action I see (takes 1 action at a time): which hypotheses are consistent with
# the outcome of this action?

def ValueFunction(action, outcome, true_hypothesis, hypothesis_space, verbose):
    current_length = len(hypothesis_space)
    updated_hypothesis_space = []
    #print("True Hypothesis is: ", true_hypothesis)
    #print("Our hypothesis space is: ", hypothesis_space)
    
    for hypothesis in hypothesis_space:
        
        ExpectedOutcome = GetOutcome(hypothesis, action, 0)
        ActualOutcome = GetOutcome(true_hypothesis, action, 0)
        
        if verbose == 1:
            print("Current hypothesis is: ", "{}".format(hypothesis))
            print("Expected Outcome of", "{}".format(action), "on the machine is: ", "{}".format(ExpectedOutcome))
            print("Actual Outcome is: ", "{}".format(ActualOutcome))
            print("")
        
        if ExpectedOutcome == ActualOutcome:
            updated_hypothesis_space.append(hypothesis)
        
            if verbose == 1:
                print("Updated hypothesis space is: ", "{}".format(updated_hypothesis_space))
                print("")
    action_value = current_length - len(updated_hypothesis_space)
    return action_value, updated_hypothesis_space
        
# Add "outcome" as something INSIDE the function, instead of as an arugment
# arugments should only be info that the function can't compute by itself (even
# by calling other functions on it)
