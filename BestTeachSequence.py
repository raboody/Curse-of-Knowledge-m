#####################

# Outputs the sequence of actions with highest value given a true hypothesis and a hypothesis space
# after deciding on an action of highest value, updates the hypothesis space, and repeats the process

# FUNCTION 7 OF __

#####################

import random
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from ChooseBestAction import *
from IsPermutation import *


def BestTeachSequence(action_space, true_hypothesis, hypothesis_space, verbose):
    block_list = []
    block_value = []
    total_hypothesis_space_size = len(hypothesis_space)
    updated_hypothesis_space = hypothesis_space
    while len(updated_hypothesis_space) > 1 and IsPermutation(updated_hypothesis_space) != True:
        block_to_show = ChooseBestAction(action_space,
                                            true_hypothesis,
                                            updated_hypothesis_space,
                                            0,
                                            0
                                            )[2]
        action_value, updated_hypothesis_space = ValueFunction(block_to_show, # action
                                             true_hypothesis,   # true hypothesis
                                             updated_hypothesis_space, # hypothesis space
                                             0,
                                             0
                                             )
        block_list.append(block_to_show)
        block_value.append(action_value)

        if verbose == 1:
            print("block we showed:", block_to_show)
            print("value of the one we showed:", action_value)
            print("action value of all blocks:", ChooseBestAction(action_space,
                                                            true_hypothesis,
                                                            updated_hypothesis_space,
                                                            0,
                                                            0
                                                            )[1]) 
    
    return block_list, block_value, total_hypothesis_space_size


