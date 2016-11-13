###########################

# uses "itertools" to produce all the permutations of a list of arbitrary size (e.g., unordered combos)

###########################

import itertools

hypothesis_list = ['A', 'B', 'C', 'D', 'E']

def perm_function(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.permutations(hypothesis_list, i):
            print(list(j))
            hypothesis_space.append(list(j))
    print("hypothesis space = {}".format(hypothesis_space))


perm_function(hypothesis_list)