# 3 hypothesis space generators
# use "itertools" to produce combinations & permutations of lists

import itertools

machine_blocks = ['A', 'B', 'C'] # available blocks


# 1. Ordered hypothesis list generators (combination):
# 1A: Ordered list + AND

def ordered_AND(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.combinations(block_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j) + ['ANDOR'])
            elif len(j) > 1:
                hypothesis_space.append(list(j) + ['AND'])
    return hypothesis_space

#print(ordered_AND(machine_blocks))


# 1B: Ordered list + AND && OR

def ordered_AND_OR(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.combinations(block_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j))
            elif len(j) > 1:
                x = list(j) + ['AND']
                y = list(j) + ['OR']
                hypothesis_space.append(x)
                hypothesis_space.append(y)
    return hypothesis_space
    
#print(ordered_AND_OR(machine_blocks))

# 2. Unordered hypothesis list generators (permutations)
# 2A. Unordered list + AND

def unordered_AND(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.permutations(block_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j))
            elif len(j) > 1:
                hypothesis_space.append(list(j) + ['AND'])
    return hypothesis_space




# 2B. Unordered list + OR

def unordered_OR(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.permutations(block_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j))
            elif len(j) > 1:
                hypothesis_space.append(list(j) + ['OR'])
    return hypothesis_space


# 2C. Unordered list + AND && OR

def unordered_AND_OR(block_list):
    hypothesis_space = []
    for i in range(0, len(block_list)+1):
        for j in itertools.permutations(block_list, i):
            if len(j) <= 1:
                hypothesis_space.append(list(j))
            elif len(j) > 1:
                x = list(j) + ['AND']
                y = list(j) + ['OR']
                hypothesis_space.append(x)
                hypothesis_space.append(y)
    return hypothesis_space


#print(len(Unordered_AND_OR(machine_blocks)))



