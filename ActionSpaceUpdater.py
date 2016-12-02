from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *
#from MonsterFunction import *




# Action space updater
# Takes in an action space and an "updated" hypothesis space
# (i.e., a hypothesis space smaller than the action space
# Reduces action space to only those actions also in the hypothesis space

def action_space_updater(action_space, true_hypothesis, hypothesis_space, verbose):
    updated_action_space = []
    if verbose == 1:
        print('action_space', action_space)
        print('hypothesis_space', hypothesis_space)
    for action in action_space:
        for hypothesis in hypothesis_space:
            if len(action) == (len(hypothesis) - 1) and action == hypothesis[0:(len(hypothesis) - 1)]:
                #print("actions to keep are:", action)
                updated_action_space.append(action)
            elif len(action) == 0 and action == hypothesis:
                #print("also keep this:", action)
                updated_action_space.append(action)
    action_space = updated_action_space
    return action_space
                

