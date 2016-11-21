###########################

# function generates all list combinations with AND or OR appended

import itertools

hypothesis_list = ['A', 'B', 'C']


def combo_AND_OR_function(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.combinations(hypothesis_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j))
            elif len(j) > 1: 
                x = [list(j) + ['AND']]
                y = [list(j) + ['OR']]
                hypothesis_space.append(x)
                hypothesis_space.append(y)
    print(len(hypothesis_space))
    return hypothesis_space


print(combo_AND_OR_function(hypothesis_list))



#############################################

# generates the "action space" (all possible actions)


hypothesis_list = ['A', 'B', 'C']


def action_space(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.combinations(hypothesis_list, i):
            hypothesis_space.append(list(j))
    print(len(hypothesis_space))
    return hypothesis_space


print(action_space(hypothesis_list))


#############################################

# rates the value of the action (e.g., the number of hypotheses it deletes)


outcomes = ['OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF',
            'OFF', 'OFF', 'OFF', 'OFF']


def simple_value_function(action_list, outcome_list, hypothesis_space):
    current_length = len(hypothesis_space)
    for x, y in zip(action_list, outcome_list):
        print(x,y)
        if y == 'OFF':
            print(list(x))
            hypothesis_space.remove(list(x))
    action_value = current_length - len(hypothesis_space)
    return action_value, hypothesis_space
    
# current problem: the action space doesn't have the AND/OR values in it
# therefore the function does not find a direct match to delete.
# need to figure out how to make it delete the list element that contains these
# letters without getting hung up on the "And" && "Or" suffixes. 


print(simple_value_function(action_space(hypothesis_list), outcomes, combo_AND_OR_function(hypothesis_list)))
