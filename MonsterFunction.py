import random 
from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from CompleteActionSpaceValue import *


def MonsterFunction(action_space, true_hypothesis, hypothesis_space):
    # We want a function that takes the output of the CompleteActionSpaceValue
    # this function should actually SHOW the block this above function recommends
    # then given the updated hypothesis space, it should use the complete function
    # to figure out what the next best block is to show
    # it should show that
    # and so on
