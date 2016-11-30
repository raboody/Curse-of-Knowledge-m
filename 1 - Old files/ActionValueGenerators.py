import itertools
from HypothesisGenerators import *
from ActionSpaceGenerator import *
from OutcomeGenerator import *



# Simple value function for ordered lists
# for both ordered AND, ordered AND && OR


# give me a set of blocks
# if a block (or set) of blocks doesn't turn the machine on, remove it
# if it activates the machine, do nothing

def OrderedValueFunction1(action_list, outcome_list, hypothesis_space):
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



# Simple value function for ordered & unordered lists
# works for any of our 5 hypothesis spaces

def UnorderedValueFunction1(action_list, outcome_list, hypothesis_space):
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
            if len(x) <= 1:
                print(x)
                hypothesis_space.remove(list(x))
            elif len(x) > 1:
                for i in range(0, len(x) + 1):
                    for j in itertools.permutations(x, i):
                        if len(j) == len(x):
                            a = list(j) + ['AND']
                            b = list(j) + ['OR']
                            print(a, b)
                            if a in hypothesis_space:
                                hypothesis_space.remove(list(a))
                            if b in hypothesis_space:
                                hypothesis_space.remove(list(b))                                         
    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space



# Medium value function for ordered lists
# Given a hypothesis space & actions, checks if hypothesis is consistent with the
# observed action & outcome
# for both ordered AND, ordered AND && OR

def OrderedValueFunction2(action_list, outcome_list, hypothesis_space):
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
                if x in hypothesis_space:
                    hypothesis_space.remove(list(x))
            elif len(x) > 1 and len(x) < len(machine_blocks):
                a = list(x) + ['AND']
                b = list(x) + ['OR']
                if a in hypothesis_space:
                    hypothesis_space.remove(a)
                if b in hypothesis_space:
                    hypothesis_space.remove(b)
            elif len(x) == len(machine_blocks):
                a = list(x) + ['AND']
                b = list(x) + ['OR']
                if a in hypothesis_space:
                    hypothesis_space.remove(a)
                if b in hypothesis_space:
                    hypothesis_space.remove(b)
    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space




# Medium value function for ordered & unordered lists
# works for any of our 5 hypothesis spaces

def UnorderedValueFunction2(action_list, outcome_list, hypothesis_space):
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
            if len(x) <= 1:
                if x in hypothesis_space:
                    print(x)
                    hypothesis_space.remove(list(x))
            elif len(x) > 1: 
                for i in range(0, len(x) + 1):
                    for j in itertools.permutations(x, i):
                        if len(j) == len(x) and len(x) < len(machine_blocks):
                            a = list(j) + ['AND']
                            b = list(j) + ['OR']
                            print(a)
                            if a in hypothesis_space:
                                hypothesis_space.remove(a)
                            if b in hypothesis_space:
                                hypothesis_space.remove(b)
                        elif len(j) == len(x) and len(x) == len(machine_blocks):
                            a = list(j) + ['AND']
                            b = list(j) + ['OR']
                            print(a,b)
                            if a in hypothesis_space:
                                hypothesis_space.remove(a)
                            if b in hypothesis_space:
                                hypothesis_space.remove(b)

    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space





# Most complex value function for ordered & unordered lists
# Same as above models, but also deletes hypotheses less complex than the
# simplest set of blocks that succeeds in turning the machine on. 
# works for any of our 5 hypothesis spaces

def UnorderedValueFunction3(action_list, outcome_list, hypothesis_space):
    print("Action list is: ")
    print(action_list)
    print("Outcome list is: ")
    print(outcome_list)
    print("Hypothesis space is: ")
    print(hypothesis_space)
    print("Blocks to remove are: ")
    
    original_action_space = action_list
    current_length = len(hypothesis_space)
    for x, y in zip(action_list, outcome_list):
        if y == 'OFF':
            if len(x) <= 1:
                if x in hypothesis_space:
                    print(x)
                    hypothesis_space.remove(list(x))
            elif len(x) > 1: 
                for i in range(0, len(x) + 1):
                    for j in itertools.permutations(x, i):
                        if len(j) == len(x) and len(x) < len(machine_blocks):
                            a = list(j) + ['AND']
                            b = list(j) + ['OR']
                            print(a,b)
                            if a in hypothesis_space:
                                hypothesis_space.remove(a)
                            if b in hypothesis_space:
                                hypothesis_space.remove(b)
                        elif len(j) == len(x) and len(x) == len(machine_blocks):
                            a = list(j) + ['AND']
                            b = list(j) + ['OR']
                            print(a,b)
                            if a in hypothesis_space:
                                hypothesis_space.remove(a)
                            if b in hypothesis_space:
                                hypothesis_space.remove(b)
        elif y == 'ON':
            if len(x) > 1:
                print('delete blocks smaller than: ')
                print(x)
                print('Thus, we also delete: ')
                
                for h in original_action_space:
                    if len(h) > 1:
                        for i in range(0, len(h) + 1):
                            for j in itertools.permutations(h, i):
                                if len(j) > 1 and len(j) < len(x):
                                    a = list(j) + ['AND']
                                    b = list(j) + ['OR']
                                    print(a,b)
                                    if a in hypothesis_space:
                                        hypothesis_space.remove(a)
                                    if b in hypothesis_space:
                                        hypothesis_space.remove(b)
    action_value = current_length - len(hypothesis_space)
    print("Action value & updated hypothesis space: ")
    return action_value, hypothesis_space




