# Curse-of-Knowledge-m
# File index

# 1.
a) action_space.py – Generates the action space (e.g., list of all possible actions given a set of blocks)
  
b) action_spaceTESTER.py - action_space tester

# 2. 
  # HypothesisGenerators.py: all 5 hypothesis generators (Ordered AND, ordered AND && OR, Unordered AND, Unordered OR, Unordered AND &&                                OR)
  # HypothesisGeneratorTESTER.py: tests to see if hypothesis generators are working as planned

# 3. 
  # GetOutcome.py: given the "rule" that activates the machine & a series of actions, returns whether the machine is "ON" or "OFF" for                       each action
  # GetOutcomeTESTER1.py: Tests the generator with 1 True Hypothesis and 1 action
  # GetOutcomeTESTER2.py: Tests the generator with a hypothesis space & action space of arbitrary size. The function assumes that each                                hypothesis provided is the "TrueHypothesis" in turn (that is, goes through all actions with a TrueHypothesis of                            [], of ['A', 'ANDOR'], etc.)
  # GetoutcomeTESTER3_csv.py: Takes what is basically the output of GetOutcomeTESTER2, but stores it in GetOutcome.csv for easier review.

# 4. 
  # ValueFunction.py - Figures out how many hypotheses an action would delete, given the true hypothesis. Sums up the number of hypotheses                        it deletes to produce an "action value" 
  # ValueFunctionTESTER.py - tests the ValueFunction given an action, a true hypothesis, and a hypothesis space
  # ValueFunctionTESTER2_csv.py - outputs ValueFunction to a csv (includes the true hypothesis, current hypothesis, current action,                                          expected outcome, and the actual outcome)
  
# 5. 
  # ChooseBestAction.py - Uses ValueFunction to generate action values for not just 1 action, but a series of actions. Given each                                   hypothesis space, the function provides the most valuable action (i.e., action that deletes the most hypotheses,                           given our update rule). Returns all possible actions, their values, and the best exemplar given the values. If                             there are multiple actions with the same value, chooses randomly between them to produce the most valuable                                 action.
  # ChooseBestActionTESTER.py - Tests the above function
  # ChooseBestActionTESTER2_csv.py - outputs the results of the ChooseBestAction function to a csv


