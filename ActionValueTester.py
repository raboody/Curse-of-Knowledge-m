import itertools
from HypothesisGenerators import *
from ActionSpaceGenerator import *
from ActionValueFunctions import *


# Testing our value functions on a list of size 3

test_1 = ['ON', 'OFF', 'OFF', 'ON', 'OFF', 'ON', 'ON', 'ON']
test_2 = ['ON', 'OFF', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'ON']
test_3 = ['ON', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'OFF']
test_4 = ['OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ON']


# Testing our value functions on a list of size 4:

#COMING SOON...



# value function names:
    # simple_ordered_value_function
    # simple_unordered_value_function
    # medium_ordered_value_function
    # medium_unordered_value_function
    # most_comlpex_unordered_value_function

# hypothesis space generator names:
    # ordered_AND
most_comlpex_unordered_value_function    # ordered_AND_OR
    # unordered_AND
    # unordered_OR
    # unordered_AND_OR


print(medium_unordered_value_function # here, choose a value function to test
      (action_space(machine_blocks),
       test_2,                          # here, choose a test to run
       unordered_AND(machine_blocks)    # here, choose a hypothesis space generator
      ))




