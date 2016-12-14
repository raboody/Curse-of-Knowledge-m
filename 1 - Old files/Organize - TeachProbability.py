from action_space import *
from HypothesisGenerators import *
from GetOutcome import *
from ValueFunction import *
from Softmax import *


def TeachProbability(action_space, true_hypothesis, hypothesis_space):
    ValueList = []
    List = []
    for action in action_space:
        currentValue, newHypothesis = ValueFunction(action, true_hypothesis, hypothesis_space, 0, 0)
        ValueList.append(currentValue)
    teachProb = Softmax(ValueList, 5)
    List = list(zip(ValueList, teachProb)) # for easier debugging pairs the 2
    #return List
    return ValueList, teachProb
    

machine_blocks = ['A', 'B', 'C', 'D', 'E'] 

print(TeachProbability(action_space(machine_blocks),
                       ['B', 'E', 'AND'],
                       ordered_AND(machine_blocks)
                       ))

    
