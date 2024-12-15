import math

# double Ra_old, Rb_old = old rating for fighter A, B
# char winner = 1 for fighter A win, 0 for fighter B win, 0.5 for Draw/No Contest
def EloCalculator (Ra_old, Rb_old, winner, Ka, Kb):
    # Expected scores
    Ea = 1/(1 + pow(10, (Rb_old - Ra_old)/400))
    Eb = 1/(1 + pow(10, (Ra_old - Rb_old)/400))
    # New elos
    Ra_new = Ra_old + Ka * (winner - Ea)
    Rb_new = Rb_old + Kb * ((1 - winner) - Eb)
    return Ra_new, Rb_new

# Exponential decay function for K:
    # Starts at 100, exponentially decays to 25
def ExpDecayK (numA, numB):
    start = 100
    floor = 25
    decayRate = 0.1
    Ka = floor + (start - floor) * math.exp(-decayRate * numA)
    Kb = floor + (start - floor) * math.exp(-decayRate * numB)
    return Ka, Kb