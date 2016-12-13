######################

# Creates an "action value"
# Takes 1 action at a time, and calculates which hypotheses are consistent with
# the outcome of this action.

# E.g., if we think the hypothesis is A, we should expect "A", "AB", etc. should activate the machine
# But if the True Hypothesis is C, none of that is correct.
# The "Expected outcome" of A given a hypothesis of A should be ON
# The "Actual outcome" will be OFF (because the TRUE hypothesis is C)
# Thus, "A" should be discarded as a hypothesis that can explain the data (because it doesn't).

# FUNCTION 4 OF ___

######################

from action_space import *
from HypothesisGenerators import *
from GetOutcome import *


# for every action (takes 1 action at a time), calculates which hypotheses
# are consistent with the outcome of this action.

def ValueFunction(action, true_hypothesis, hypothesis_space, verbose, verbose2):
    current_length = len(hypothesis_space)
    updated_hypothesis_space = []
    if verbose2 == 1:
        true_hypothesis_list = ["True hypothesis is: "]
        current_hypothesis_list = ["Current hypothesis is: "]
        action_list = ["Current action is: "]
        expected_outcome_list = ["Given the current hypothesis and action, the expected outcome is: "]
        actual_outcome_list = ["Given the true hypothesis and action, the actual outcome is: "]

    
    for hypothesis in hypothesis_space:
        
        ExpectedOutcome = GetOutcome(hypothesis, action, 0)
        ActualOutcome = GetOutcome(true_hypothesis, action, 0)
        
        if verbose == 1:
            print("Current hypothesis is: ", "{}".format(hypothesis))
            print("Expected Outcome of", "{}".format(action), "on the machine is: ", "{}".format(ExpectedOutcome))
            print("Actual Outcome is: ", "{}".format(ActualOutcome))
            print("")

        if verbose2 == 1:
            true_hypothesis_list.append(true_hypothesis)
            current_hypothesis_list.append(hypothesis)
            action_list.append(action)
            expected_outcome_list.append(ExpectedOutcome)
            actual_outcome_list.append(ActualOutcome)
            
        
        if ExpectedOutcome == ActualOutcome:
            updated_hypothesis_space.append(hypothesis)
        
            if verbose == 1:
                print("Updated hypothesis space is: ", "{}".format(updated_hypothesis_space))
                print("")
    action_value = current_length - len(updated_hypothesis_space)

    if verbose2 == 1:
        return true_hypothesis_list, current_hypothesis_list, action_list, expected_outcome_list, actual_outcome_list
    else:
        return action_value, updated_hypothesis_space
        
