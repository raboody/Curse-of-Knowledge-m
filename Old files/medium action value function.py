import itertools
from HypothesisGenerators import *
from ActionSpaceGenerator import *


outcomes = ['ON', 'OFF', 'OFF', 'ON', 'ON', 'OFF', 'ON', 'OFF',]



    

print(simple_value_function
      (action_space(machine_blocks),
       outcomes,
       ordered_AND_OR(machine_blocks)
      ))
