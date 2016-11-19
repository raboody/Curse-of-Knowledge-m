import itertools

hypothesis_list = ['A', 'B']


def combo_function(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.combinations(hypothesis_list, i):
            hypothesis_space.append(list(j))
    return hypothesis_space


print(combo_function(hypothesis_list))


#########################################################


actions = ['AB', 'A', 'B']
outcomes = ['ON', 'OFF', 'OFF']


def simple_value_function(action_list, outcome_list, hypothesis_space):
    current_length = len(hypothesis_space)
    for x, y in zip(action_list, outcome_list):
        if y == 'OFF':
            hypothesis_space.remove(list(x))
    action_value = current_length - len(hypothesis_space)
    return action_value, hypothesis_space
    #return hypothesis_space

    

print(simple_value_function(actions, outcomes, combo_function(hypothesis_list)))

