###########################

# uses itertools to produce all the combinations of a list of arbitrary size (e.g., ordered combos).
# Each hypothesis is also assigned an 'AND' or 'OR' element.

###########################


import itertools

hypothesis_list = ['A', 'B', 'C']


def combo_AND_OR_function(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.combinations(hypothesis_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j))
            elif len(j) > 1: # and counter == 1:
                x = [list(j) + ['AND']]
                y = [list(j) + ['OR']]
                hypothesis_space.append(x)
                hypothesis_space.append(y)
    return hypothesis_space

