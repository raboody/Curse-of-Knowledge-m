# 2 types of hypothesis space generators
# ordered (combinations) & unordered (permutations)
# use "itertools" to produce combinations & permutations of lists

import itertools


# 1. Ordered hypothesis list generators (combination):
# 1A: Ordered list + AND

def ordered_AND(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.combinations(block_list, i):
            if len(j) == 1:
                hypothesis_space.append(list(j) + ['ANDOR'])
            elif len(j) > 1:
                hypothesis_space.append(list(j) + ['AND'])
            else:
                hypothesis_space.append(list(j))
    return hypothesis_space



# 1B: Ordered list + AND && OR

def ordered_AND_OR(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.combinations(block_list, i):

            # for single blocks (e.g., A, B, C, etc.)
            if len(j) == 1:
                hypothesis_space.append(list(j) + ['ANDOR'])

            # for more than 1 block (e.g., ['A', 'B'] etc.)
            elif len(j) > 1:
                x = list(j) + ['AND']
                y = list(j) + ['OR']
                hypothesis_space.append(x)
                hypothesis_space.append(y)

            # for empty hypothesis spaces (e.g., [])
            else:
                hypothesis_space.append(list(j))
    return hypothesis_space
    


# 2. Unordered hypothesis list generators (permutations)
# 2A. Unordered list + AND

def unordered_AND(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.permutations(block_list, i):
            if len(j) == 1:
                hypothesis_space.append(list(j) + ['ANDOR'])
            elif len(j) > 1:
                hypothesis_space.append(list(j) + ['AND'])
            else:
                hypothesis_space.append(list(j))
    return hypothesis_space




# 2B. Unordered list + OR

def unordered_OR(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.permutations(block_list, i):
            if len(j) == 1:
                hypothesis_space.append(list(j) + ['ANDOR'])
            elif len(j) > 1:
                hypothesis_space.append(list(j) + ['OR'])
            else:
                hypothesis_space.append(list(j))
    return hypothesis_space


# 2C. Unordered list + AND && OR

def unordered_AND_OR(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.permutations(block_list, i):
            if len(j) == 1:
                hypothesis_space.append(list(j) + ['ANDOR'])
            elif len(j) > 1:
                x = list(j) + ['AND']
                y = list(j) + ['OR']
                hypothesis_space.append(x)
                hypothesis_space.append(y)
            else:
                hypothesis_space.append(list(j))
    return hypothesis_space





