######################

# For unordered spaces, sometimes multiple hypotheses are left that are all just
# permutations of one another (e.g., ['B', 'E', 'AND'], ['E', 'B', 'AND'])
# In this case, both of these hypotheses are correct due to our current True Hypothesis
# So we use IsPermutation to check whether all remaining hypotheses are just permutations of one another
# If they are, the function stops (since if they ARE all just permutations of one another, they are ALL true)

# FUNCTION 6 OF __

######################

import random
import itertools
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from ChooseBestAction import *


def IsPermutation(hypothesis_space):
    if len(hypothesis_space[0]) > 0:
        first_hypothesis = hypothesis_space[0]
        operator = []
        if first_hypothesis[len(first_hypothesis) - 1] == 'OR':
            operator = ['OR']
        elif first_hypothesis[len(first_hypothesis) - 1] == 'AND':
            operator = ['AND']
        else:
            operator = ['ANDOR']
        
        first_hypothesis = first_hypothesis[0:(len(first_hypothesis) - 1)]

        comparison_hypotheses = []
        
        for i in range(0, len(first_hypothesis)+1):
            for j in itertools.permutations(first_hypothesis, i):
                if len(j) == len(first_hypothesis):
                    comparison_hypotheses.append(list(j) + operator)


    if hypothesis_space == comparison_hypotheses:
        return True
    else:
        return False




        
