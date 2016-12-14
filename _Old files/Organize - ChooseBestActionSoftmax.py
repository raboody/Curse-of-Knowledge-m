######################

# takes in an action space, the "true hypothesis" (e.g., the rule that activates
# the machine), and one of our (currently 5) hypothesis spaces.

# Given this hypothesis space, returns:
# 1. The possible actions given the hypothesis space
# 2. The values of these actions given the actual True Hypothesis
# 3. Which of the blocks is most valuable to show (e.g., best teaching choice)

# FUNCTION 5 OF __

######################

import random
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from Softmax import *


def ChooseBestActionSoftmax(action_space, true_hypothesis, hypothesis_space, verbose, verbose2):
    ValueList = []
    if verbose == 1:
        print("Action space is: ", "{}".format(action_space))
        print("hypothesis space is: ", "{}".format(hypothesis_space))

    # Getting the value of each action
    for action in action_space:
        currentValue, newHypothesis = ValueFunction(action, true_hypothesis, hypothesis_space, verbose, 0)
        ValueList.append(currentValue)
        
        if verbose == 1:
            print("Current hypotheses are:", "{}".format(newHypothesis))
            print("Current value list: ", "{}".format(ValueList))


    # Now that we have the action values, we want to transform them with softmax:
    actions, values = action_space, Softmax(ValueList)
    
    

    


    # Now that we have the action values, we want to find the biggest value
    # (i.e., the best action)
    actions, values = action_space, ValueList
    index_counter, largest_value = -1, -1
    largest_value_index_list, largest_value_list, best_exemplar = [], [], []

    # Finds the largest action value (best action to perform for this hypothesis space)
    for value in values:
        if value >= largest_value:
            largest_value = value
    

    # Now checks to see how many actions produce that value
    for value in values:
        index_counter += 1
        if value == largest_value:
            largest_value_index_list.append(index_counter)
    if verbose2 == 1:
        print("largest action value:", largest_value)
        print("Index(es) of the largest value: ", largest_value_index_list)
            
    # If more than 1 action produces the same largest action value, chooses randomly which action to perform
    # Does this by taking a list of the indexes of the highest value actions, and chooses between them
    # (takes a random index of the list of highest action value indexes to choose randomly between them)
    if len(largest_value_index_list) > 1:
        index_of_largest_value_index_list = random.randint(0, len(largest_value_index_list) - 1)
        best_exemplar = actions[largest_value_index_list[index_of_largest_value_index_list]]
        for i in largest_value_index_list:
            largest_value_list.append(actions[i])
        if verbose2 == 1:
            print("list of the largest values at those indices: ", largest_value_list)

    # If there's only 1 action with the largest action value, just do that one
    else:
        best_exemplar = actions[largest_value_index_list[0]]
        print("largest value at that index is: ", best_exemplar)
    
    return actions, values, best_exemplar
    
 
