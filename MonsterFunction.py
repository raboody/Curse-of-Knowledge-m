import random 
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *
from ActionSpaceUpdater import *
from IsPermutation import *


def MonsterFunction(action_space, true_hypothesis, hypothesis_space, verbose):
    block_list = []
    block_value = []

    total_hypothesis_space_size = len(hypothesis_space)

    updated_hypothesis_space = hypothesis_space
    #print("starting action space:", action_space)
    #print("starting hypothesis space:", hypothesis_space)

    while len(updated_hypothesis_space) > 1 and IsPermutation(updated_hypothesis_space) != True:
        block_to_show = GetActionSpaceValue(action_space,
                                            true_hypothesis,
                                            updated_hypothesis_space,
                                            0
                                            )[2]
        if verbose == 1:
            print("block we showed:", block_to_show)
            print("action value of all blocks:", GetActionSpaceValue(
                                                            action_space,
                                                            true_hypothesis,
                                                            updated_hypothesis_space,
                                                            0
                                                            )[1])                      
        
        action_value, updated_hypothesis_space = ValueFunction(block_to_show,
                                             GetOutcome(true_hypothesis, block_to_show, 0),
                                             true_hypothesis,
                                             updated_hypothesis_space,
                                             0
                                             )

        action_space = action_space_updater(action_space, true_hypothesis, updated_hypothesis_space, 0)

        if verbose == 1:
            
            print("value of the one we showed:", action_value)                                                           
            print("updated hypothesis space:", updated_hypothesis_space)
            print("updated action space is", action_space)
            
    
        block_list.append(block_to_show)
        block_value.append(action_value)

        
        
    return block_list, block_value, total_hypothesis_space_size


