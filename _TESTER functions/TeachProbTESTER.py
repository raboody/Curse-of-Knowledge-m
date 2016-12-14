from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from ChooseBestAction import *
from Softmax import *
from TeachProb import *


machine_blocks = ['A', 'B', 'C', 'D', 'E']
trueHypothesis = ['B', 'E', 'AND']


Teacher1 = [['B', 'E'], ['A', 'B'], ['D', 'E'], ['A', 'B', 'E'], ['A', 'B', 'E'], ['A', 'B', 'C', 'D', 'E', ], ['A', 'C']]
Teacher2 = [['B', 'E'], ['A', 'B', 'E'], ['A'], ['A', 'B', 'D', 'E']] 
Teacher3 = [['B', 'E'], ['A', 'C', 'D'], ['A', 'B', 'C', 'D', 'E']]
Teacher4 = [['B', 'E'], ['A', 'B'], ['D', 'E'], ['A', 'C', 'D', 'E'], ['B', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D'], ['B', 'E']]


print(TeachProb(Teacher3,
                action_space(machine_blocks),
                trueHypothesis,
                ordered_AND_OR(machine_blocks),
                5,
                1
                ))
        
