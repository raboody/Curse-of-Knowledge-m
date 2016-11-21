# tests our hypothesis space generators


from HypothesisGenerators import *

# First test: one block

TestA = ['X']

print(ordered_AND(TestA))
print(ordered_AND_OR(TestA))

print(Unordered_AND(TestA))
print(Unordered_OR(TestA))
print(Unordered_AND_OR(TestA))


# Second test: 2 blocks

TestB = ['A', 'B']

print(ordered_AND(TestB))
print(ordered_AND_OR(TestB))

print(Unordered_AND(TestB))
print(Unordered_OR(TestB))
print(Unordered_AND_OR(TestB))


# Third test: pushing a new list directly into the function
print(ordered_AND(['X','Y','Z']))
print(ordered_AND_OR(['X','Y','Z']))

print(Unordered_AND(['X','Y','Z']))
print(Unordered_OR(['X','Y','Z']))
print(Unordered_AND_OR(['X','Y','Z']))
