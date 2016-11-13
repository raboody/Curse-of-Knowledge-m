###########################

# uses "itertools" to produce all the combinations of a list of arbitrary size (e.g., ordered combos)

###########################


import itertools

hypothesis_list = ['A', 'B', 'C', 'D', 'E']


def combo_function(hypothesis_space):
    hypothesis_space = []
    for i in range(0, len(hypothesis_list)+1):
        for j in itertools.combinations(hypothesis_list, i):
            print(list(j))
            hypothesis_space.append(list(j))
    print("hypothesis space = {}".format(hypothesis_space))



combo_function(hypothesis_list)
