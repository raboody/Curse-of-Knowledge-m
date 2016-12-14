import itertools
from HypothesisGenerators import *
from ActionSpaceGenerator import *


outcomes = ['ON', 'OFF', 'OFF', 'ON', 'OFF', 'ON', 'ON', 'ON',]


# Simple value function for ordered AND

def simple_value_function(action_list, outcome_list, hypothesis_space):
    print("Action list is: ")
    print(action_list)
    print("Outcome list is: ")
    print(outcome_list)
    print("Hypothesis space is: ")
    print(hypothesis_space)

    print("Blocks to remove are: ")
    current_length = len(hypothesis_space)
    for x, y in zip(action_list, outcome_list):
        if y == 'OFF':
            print(x)
            if len(x) <= 1:
                hypothesis_space.remove(list(x))
            elif len(x) > 1:
                a = list(x) + ['AND']
                b = list(x) + ['OR']
                if a in hypothesis_space:
                    hypothesis_space.remove(list(a))
                if b in hypothesis_space:
                    hypothesis_space.remove(list(b))
    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space
    


# Simple value function for ordered AND_OR
# a separate function is needed because the AND_OR hypothesis space
# produces an extra set of brackets around each hypothesis. If this extra
# set is not included in the code that tells the program what to remove, it
# messes up. Maybe there's a better solution? 


def simple_value_function_two(action_list, outcome_list, hypothesis_space):
    print("Action list is: ")
    print(action_list)
    print("Outcome list is: ")
    print(outcome_list)
    print("Hypothesis space is: ")
    print(hypothesis_space)

    print("Blocks to remove are: ")
    current_length = len(hypothesis_space)
    for x, y in zip(action_list, outcome_list):
        if y == 'OFF':
            print(x)
            if len(x) <= 1:
                hypothesis_space.remove(list(x))
            elif len(x) > 1:
                a = [list(x) + ['AND']]
                b = [list(x) + ['OR']]
                if a in hypothesis_space:
                    hypothesis_space.remove(list(a))
                if b in hypothesis_space:
                    hypothesis_space.remove(list(b))
    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space



# Medium complexity value function

def medium_value_function(action_list, outcome_list, hypothesis_space):
    print("Action list is: ")
    print(action_list)
    print("Outcome list is: ")
    print(outcome_list)
    print("Hypothesis space is: ")
    print(hypothesis_space)
    print("Blocks to remove are: ")
    
    current_length = len(hypothesis_space)
    for x, y in zip(action_list, outcome_list):
        if y == 'OFF':
            print(x)
            print(len(x))
            print(len(machine_blocks))
            
            if len(x) <= 1:
                if x in hypothesis_space:
                    hypothesis_space.remove(list(x))
            elif len(x) > 1 and len(x) < len(machine_blocks):
                a = [list(x) + ['AND']]
                if a in hypothesis_space:
                    hypothesis_space.remove(a)

                    
            elif len(x) == len(machine_blocks):
                a = list(x) + ['AND']
                b = list(x) + ['OR']
                if a in hypothesis_space:
                    hypothesis_space.remove(list(a))
                if b in hypothesis_space:
                    hypothesis_space.remove(list(b))
    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space




print(simple_value_function
      (action_space(machine_blocks),
       outcomes,
       ordered_AND(machine_blocks)
      ))
