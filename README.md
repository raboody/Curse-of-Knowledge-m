# Curse-of-Knowledge-m
# File index

# action_space.py – Generates the action space (e.g., list of all possible actions given a set of blocks)

# action_spaceTESTER.py - action_space tester


# HypothesisGenerators.py: all 5 hypothesis generators (Ordered AND, ordered AND && OR, Unordered AND, Unordered OR, Unordered AND && OR)

# HypothesisGeneratorTESTER.py: tests to see if hypothesis generators are working as planned


# GetOutcome.py: given the "rule" that activates the machine & a series of actions, returns whether the machine is "ON" or "OFF" for                       each action

# GetOutcomeTESTER1.py: Tests the generator with 1 True Hypothesis and 1 action

# GetOutcomeTESTER2.py: Tests the generator with a hypothesis space & action space of arbitrary size

# GetoutcomeTESTER3_csv.py: Takes what is basically the output of GetOutcomeTESTER2, but stores it in GetOutcome.csv for easier review.


# ValueFunction.py - functions to produce the 3 types of action values we spoke about (simple, medium, complex). 

# ActionValueTESTER.py - tests the Action Value Generators

# CompleteActionSpaceValue.py - Uses the Action Value Generator to generate action values for not just 1 action, but a series of actions                        (e.g., what we'd actually see from teacher data)

# CopmleteActionSpaceValueTESTER.py - Tests the Action Value Generator




# OutcomeGeneratorTESTER1: One way to test the outcome generator

# OutcomeGeneratorTESTER2: More comprehensive (but computationally costly) way to test the outcome generator
