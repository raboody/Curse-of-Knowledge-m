#####################

# Not sure we really need this function
# Restricts the action space to the hypothesis space
# That is, if the hypothesis space is ['B', 'ANDOR'], ['D', 'ANDOR'] will
# restrict the action space to ['B'] and ['D']

#####################


from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *

def action_space_updater(action_space, true_hypothesis, hypothesis_space, verbose):
    updated_action_space = []
    if verbose == 1:
        print('action_space', action_space)
        print('hypothesis_space', hypothesis_space)
    for action in action_space:
        for hypothesis in hypothesis_space:
            if len(action) == (len(hypothesis) - 1) and action == hypothesis[0:(len(hypothesis) - 1)]:
                updated_action_space.append(action)
            elif len(action) == 0 and action == hypothesis:
                updated_action_space.append(action)
    action_space = updated_action_space
    return action_space
                

