#####################

# Can use this to easily apply the Softmax algorithm to any set of numeric data

# FUNCTION 8 OF __

#####################



import numpy as np

def Softmax(ActionValues, Tau):
    Temp = [np.exp(i/Tau) for i in ActionValues]
    ProbDist = [i/sum(Temp) for i in Temp]
    return ProbDist


