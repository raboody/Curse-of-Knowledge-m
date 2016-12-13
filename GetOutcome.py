######################

# Given a true hypothesis and an action, generates the expected outcome (e.g., machine "ON" or "OFF")
# Supports 1 or multiple True Hypotheses

# FUNCTION 3 OF __

######################

# To think about: am I fully using my memory? Am I combining the info I'm getting?

def GetOutcome(TrueHypothesis, action, verbose):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    if verbose == 1:
        print("True hypothesis is: ", "{}".format(TrueHypothesis))
        print("action is: ", "{}".format(action))
    for j in TrueHypothesis:
        for i in action:
            # if the hypothesis is just 1 letter, just check if that letter is in the action
            # if it is, the machine should turn ON; if it isn't, it should remain OFF
            # That is, if counter1 > 0, machine = ON; else machine = OFF
            if len(TrueHypothesis) <=2:
                if j == i:
                    counter1 += 1
                    
            # if it's an AND hypothesis, check if all TrueHypothesis letters are present in the action
            # if they are all present, machine should be ON; else, should be OFF
            # That is, if counter2 == number of letters in the hypothesis, machine = ON; else machine = OFF
            elif TrueHypothesis[len(TrueHypothesis) - 1] == 'AND':
                if j == i:
                    counter2 += 1

            # if it's an OR hypothesis, check if 1 or more TrueHypothesis letters is in the action
            # if ANY of the letters are in the action, the machine should turn ON
            else:
                if TrueHypothesis[len(TrueHypothesis) - 1] == 'OR':
                    if j == i:
                        counter3 += 1

    if counter1 > 0 or (counter2 == (len(TrueHypothesis) - 1) and len(TrueHypothesis) > 2):
        if verbose == 1:
            print("Outcome is: ")
        return "ON"
    elif counter3 > 0:
        if verbose == 1:
            print("Outcome is: ")
        return "ON"
    elif len(TrueHypothesis) == 0 and action == TrueHypothesis:
        if verbose == 1:
            print("Outcome is: ")
        return "ON"
    else:
        if verbose == 1:
            print("Outcome is: ")
        return "OFF"



    
