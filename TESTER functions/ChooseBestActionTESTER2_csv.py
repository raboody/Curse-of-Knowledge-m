######################

# Prints the output of ChooseBestAction to a csv for easier review
# Prints the action values of all 5 hypothesis spaces one after the other. 

######################

import csv
from ChooseBestAction import *

machine_blocks = ['A', 'B', 'C', 'D', 'E'] 


AllHypothesisSpaces = [ordered_AND, ordered_AND_OR, unordered_AND, unordered_OR, unordered_AND_OR]


with open ('ChooseBestAction.csv', 'w', newline = '') as myfile:
    writer = csv.writer(myfile)
    for i in AllHypothesisSpaces:
        actions, values, best_exemplar = ChooseBestAction(action_space(machine_blocks),   # all possible actions (action space)
        ['B', 'E', 'AND'],                    # true hypothesis (from ActionValueTESTER)
        i(machine_blocks), # hypothesis space (all possible hypotheses)
        0,  # verbose (0 = off, 1 = on)
        0   # verbose2 (0 = off, 1 = on)
        )
        writer.writerow(actions)
        writer.writerow(values)
        writer.writerow(best_exemplar)
        writer.writerow("")




