#####################


# FUNCTION 9 OF __

#####################

from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from ChooseBestAction import *
from Softmax import *


def TeachProb(actions, action_space, true_hypothesis, hypothesis_space, Tau, verbose):
    index_counter = 0
    action_prob_list = []
    for action in actions:
        allActions, Values, best_exemplar = ChooseBestAction(action_space,
                                            true_hypothesis,
                                            hypothesis_space,
                                            0,
                                            0)
        softmaxValues = Softmax(Values, Tau)
        actionProb = softmaxValues[allActions.index(action)]
        hypothesis_space = ValueFunction(action,
                                         true_hypothesis,
                                         hypothesis_space,
                                         0,
                                         0)[1]
        if verbose == 1:
            print("allActions: ", allActions)
            print("softmaxValue: ", softmaxValues)
            print("softmaxValue sum: ", sum(softmaxValues))
            print("probability of our action: ", actionProb)
            print("updated hypothesis space: ", hypothesis_space)
             
        action_prob_list.append(actionProb)
    return action_prob_list


