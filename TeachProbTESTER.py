from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from ChooseBestAction import *
from Softmax import *
from TeachProb import *


machine_blocks = ['A', 'B', 'C', 'D', 'E']
trueHypothesis = ['B', 'E', 'AND']

print(TeachProb([['B', 'E'], ['B'], ['E'], ['A', 'B']],
                action_space(machine_blocks),
                trueHypothesis,
                ordered_AND(machine_blocks),
                5,
                0
                ))
        
