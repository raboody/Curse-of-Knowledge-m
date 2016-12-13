###########################

# uses "itertools" to produce all the combinations of a list of arbitrary size (e.g., ordered combos)
# identical to combo_function, but instead generates the action_space

# FUNCTION 1 of __

###########################


import itertools


def action_space(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.combinations(block_list, i):
            hypothesis_space.append(list(j))
    return hypothesis_space
