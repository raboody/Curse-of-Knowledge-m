from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from ChooseBestAction import *
from Softmax import *
from TeachProb import *


machine_blocks = ['A', 'B', 'C', 'D', 'E']
trueHypothesis = ['B', 'E', 'AND']
HypothesisList = [ordered_AND, ordered_AND_OR, unordered_AND, unordered_OR, unordered_AND_OR]

Teacher1 = [['B', 'E'], ['A', 'B'], ['D', 'E'], ['A', 'B', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'C']]
Teacher2 = [['B', 'E'], ['A', 'B', 'E'], ['A'], ['A', 'B', 'D', 'E']] 
Teacher3 = [['B', 'E'], ['A', 'C', 'D'], ['A', 'B', 'C', 'D', 'E']]
Teacher4 = [['B', 'E'], ['A', 'B'], ['D', 'E'], ['A', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D']]
Teacher5 = [['B', 'E'],	['B', 'C', 'D', 'E'], ['A', 'B'], ['A', 'E']]
Teacher6 = [['B', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'C', 'D'], ['A', 'B', 'C', 'D']]
Teacher7 = [['B', 'E'], ['A', 'C', 'D'], ['A', 'B', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'D', 'E']]
Teacher8 = [['B', 'E']]
Teacher9 = [['B', 'E'], ['A', 'B', 'D', 'E']]
Teacher10 = [['B', 'E'], ['B'], ['E'], ['A', 'B', 'E'], ['A', 'B', 'C', 'E'], ['A', 'B', 'C', 'D', 'E']]
Teacher11 = [['B', 'E'], ['E'], ['B'], ['A', 'B', 'E'],	['A', 'E'], ['B', 'C', 'E'], ['B', 'C'], ['B', 'D', 'E'], ['D', 'E']]
Teacher12 = [['A', 'B', 'C', 'D', 'E'], ['B', 'C', 'D', 'E'], ['C', 'D', 'E'], ['B', 'D', 'E'], ['B', 'D'], ['B', 'E'],	['A', 'B', 'E'], ['E'], ['B'], ['A', 'C'], ['C', 'D'], ['A', 'B']]  
Teacher13 = [['B', 'E'], ['A', 'B'], ['A','E']]
Teacher14 = [['B', 'E'], ['B', 'C'], ['D', 'E']]
Teacher15 = [['B', 'E'], ['A', 'B', 'D', 'E'], ['A', 'B', 'D']]
Teacher16 = [['B', 'E']]
Teacher17 = [['B', 'E'], ['A', 'B', 'C'], ['C', 'D', 'E'], ['A', 'D', 'E'], ['A', 'B', 'C', 'D', 'E'], ['B', 'C', 'D', 'E'], ['B', 'D', 'E'], ['E']]
Teacher18 = [['B', 'E'], ['A', 'B', 'E'], ['B', 'C', 'E'], ['B', 'C'], ['A', 'B', 'C', 'D', 'E'], ['C', 'D'], ['B']]
Teacher19 = [['B', 'E'], ['A', 'C', 'D'], ['A', 'B', 'E'], ['A', 'B'], ['A', 'C'], ['A', 'B', 'C', 'D', 'E']]
Teacher20 = [['A', 'B', 'C', 'D'], ['A', 'C', 'D', 'E'], ['B', 'E'], ['A', 'B', 'C', 'D', 'E']]

TeacherList = [Teacher6, Teacher7, Teacher8, Teacher9, Teacher10, Teacher11, Teacher12, Teacher13, Teacher14, Teacher15, Teacher16, Teacher17, Teacher18, Teacher19, Teacher20]

for teacher in TeacherList:
    for i in HypothesisList:
        print(TeachProb(teacher,
                    action_space(machine_blocks),
                    trueHypothesis,
                    i(machine_blocks),
                    5,
                    0
                    ))
        
