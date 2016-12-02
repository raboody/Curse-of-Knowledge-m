import random
import itertools
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *
from ActionSpaceUpdater import *


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

                
    #return comparison_hypotheses
    
#    for hypothesis in hypothesis_space:




print(IsPermutation([['B', 'E', 'AND'], ['E', 'B', 'AND']]))
        
