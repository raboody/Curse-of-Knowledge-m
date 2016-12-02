# Outcome generator
# given a true hypothesis and an action, generates the expected outcome
# (e.g., machine "ON" or "OFF")


# add some comments saying that TrueHypothesis will just be 1
# but it supports taking multiple hypotheses and will give you back all the outcomes
# for each one


# BUG: if your current hypothesis is ['A', 'E', 'OR'], it says
# the expected outcome of ['A', 'B', 'C', 'D'] on the machine is ON
# but actually it might be on OR off (if it's A, should be on; if E, should be off
# need to implement a "not sure" value maybe?
# then if we are "not sure" we retain the hypothesis until we can later disprove it conclusively

# also, am I fully using my memory? Am I combining the info I'm getting?

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
            
            else:
                # if it's an OR hypothesis, check if 1 or more of the letters is in the action
                # if ALL of the letters are in the action, the machine should turn ON
                # If 1 or more, but not ALL, are in the action, the machine *could* be OFF 
                # That is, if counter1 > 0, machine = ON; else machine = OFF
                if TrueHypothesis[len(TrueHypothesis) - 1] == 'OR':
                    if j == i:
                        counter3 += 1
                # if it's an AND hypothesis, check if all hypothesis letters are present in the action
                # if they are all present, machine should be ON; else, should be OFF
                # That is, if counter2 == number of letters in the hypothesis, machine = ON; else machine = OFF
                elif TrueHypothesis[len(TrueHypothesis) - 1] == 'AND':
                    if j == i:
                        counter2 += 1
    #print("counter 1 is: ", "{}".format(counter1)) #for debugging
    #print("counter 2 is: ", "{}".format(counter2)) #for debugging
    if counter1 > 0 or (counter2 == (len(TrueHypothesis) - 1) and len(TrueHypothesis) > 2):
        if verbose == 1:
            print("Outcome is: ")
        return "ON"
    elif counter3 > 0 and counter3 == len(TrueHypothesis) - 1:
        return "ON"
    elif counter3 > 0 and counter3 != len(TrueHypothesis) - 1:
        return "unsure"
    else:
        if verbose == 1:
            print("Outcome is: ")
        return "OFF"



    
