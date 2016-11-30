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
    # OrderedValueFunction1 (simple ordered value function)
    # UnorderedValueFunction1 (simple unordered value function)
    # OrderedValueFunction2 (medium_ordered_value_function)
    # UnorderedValueFunction2 (medium_unordered_value_function)
    # UnorderedValueFunction3 (most_comlpex_unordered_value_function)

# hypothesis space generator names:
    # ordered_AND
    # ordered_AND_OR
    # unordered_AND
    # unordered_OR
    # unordered_AND_OR


print(UnorderedValueFunction2           # here, choose a value function to test
      (action_space(machine_blocks),
       test_2,                          # here, choose a test to run
       unordered_AND(machine_blocks)    # here, choose a hypothesis space generator
      ))




