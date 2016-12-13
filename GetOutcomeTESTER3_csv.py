######################

# Tests GetOutcome; takes a hypothesis space & action space of any size
# Outputs the results of the actions & hypotheses to a csv called "GetOutcome.csv"
# ATTN: GetOutcome.csv is overwritten every time you run this function!

######################

import csv
from GetOutcome import *
from HypothesisGenerators import *
from action_space import *

blocks = ['A', 'B', 'C', 'D', 'E']


def printfunction(Hypotheses, Actions, verbose):
    with open ('GetOutcome.csv', 'w', newline = '') as myfile:
        writer = csv.writer(myfile)
        listofpossibilities = []
        action_list = ["And the Action is: "]
        outcome_list = ["The outcome will be: "]
        hypothesis_list = ["If the True Hypothesis is: "]

        for hypothesis in Hypotheses:
            for action in Actions:
                hypothesis_list.append(hypothesis)
                action_list.append(action)
                outcome_list.append(GetOutcome(hypothesis, action, 0))

        writer.writerow(hypothesis_list)
        writer.writerow(action_list)
        writer.writerow(outcome_list)


printfunction(ordered_AND_OR(blocks), action_space(blocks), 0)
                


