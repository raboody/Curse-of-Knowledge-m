import random
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *


# takes in an action space, the "true hypothesis" (e.g., the rule that activates
# the machine), and one of our (currently 5) hypothesis spaces.

# Given this hypothesis space, returns:
# 1. The possible actions given the hypothesis space
# 2. The values of these actions given the actual True Hypothesis
# 3. Which of the blocks is most valuable to show (e.g., best teaching choice)


def GetActionSpaceValue(action_space, true_hypothesis, hypothesis_space, verbose):
    ValueList = []
    if verbose == 1:
        print("Action space is: ", "{}".format(action_space))
        print("hypothesis space is: ", "{}".format(hypothesis_space))


    # Getting the value of each action
    # (e.g., how many  hypotheses each action deletes, given the machine's actual activation rule)
    for action in action_space:
        outcome = GetOutcome(true_hypothesis, action, 0)
        currentValue, newHypothesis = ValueFunction(action, outcome, true_hypothesis, hypothesis_space, verbose)
        ValueList.append(currentValue)
        if verbose == 1:
            print("Current hypotheses are:", "{}".format(newHypothesis))
            print("Current value list: ", "{}".format(ValueList))

    # Now that we have the action values, we want to find the biggest value
    # (i.e., the best action)
    actions = action_space
    values = ValueList
    index_counter1 = -1
    index_counter2 = -1
    largest_value = -1
    largest_value_index_list = []
    best_exemplar = []

    # Finds the largest action value (best action to perform for this hypothesis space)
    for value in values:
        if largest_value < value:
            largest_value = value
            index_counter1 += 1

    # Now checks to see how many actions produce that value
    for value in values:
        index_counter2 += 1
        if value == largest_value:
            largest_value_index_list.append(index_counter2)
            
    # If more than 1 action produces the same largest action value:
    # Create a list with the indexes of these actions
    # Randomly chooses between these actions to choose 1 to perform
    # (takes the index of the list of highest action value indexes to choose randomly between them)
    # (So thus we get an index of a list of indexes)
    # (looks confusing but basically we use this to get back to the index of the actual block we want to choose)
    if len(largest_value_index_list) > 1:
        index_of_largest_value_index_list = random.randint(0, len(largest_value_index_list) - 1)
        best_exemplar = actions[largest_value_index_list[index_of_largest_value_index_list]]

    # If there's only 1 action with the largest action value, just do that one
    else:
        best_exemplar = actions[index_counter1]
    
    print(actions[0])
    return actions, values, best_exemplar
    
    # return function for debugging: return actions, values, index_counter1, largest_value, largest_value_index_list, best_exemplar




    
