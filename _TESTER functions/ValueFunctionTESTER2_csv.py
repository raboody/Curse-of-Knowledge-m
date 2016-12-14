######################

# Prints the output of ValueFunction to a csv for easier review

######################

import csv
from ValueFunction import *


machine_blocks = ['A', 'B', 'C', 'D', 'E']


def ValueFunctionTESTER3_csv(ValueFunction):
    with open ('ValueFunction.csv', 'w', newline = '') as myfile:
        writer = csv.writer(myfile)
        for i in ValueFunction:
            writer.writerow(i)


ValueFunctionTESTER3_csv(ValueFunction(
    ['B', 'D'],     # action
    ['B', 'E', 'AND'],  # true hypothesis
    unordered_OR(machine_blocks),    # hypothesis space
    0,   # verbose (0 = off, 1 = on)
    1   # verbose2 (0 = off, 1 = on)
    ))
