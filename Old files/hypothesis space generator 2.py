###########################

# uses "itertools" to produce all the permutations of a list of arbitrary size (e.g., unordered combos)

###########################

import itertools

hypothesis_list = ['A', 'B', 'C']

def perm_function(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.permutations(hypothesis_list, i):
            hypothesis_space.append(list(j))
    return hypothesis_space


print(perm_function(hypothesis_list))
