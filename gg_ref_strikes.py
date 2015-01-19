# Glupska grisen
# Teo Elmfeldt
from random import randint
points = []

def rand_dice(n): # generates a random number, remember to put n = 1 when calling
    return randint(n, 6) # six-sided dice
    # to be able to exclude 1 as a possibility


def one_round(tactic):
    t = rand_dice(2) # t for total
    i = 1
    while i < tactic: # loop as long as you want to
        
        n = rand_dice(1) # save return value of one_strike() to n
        if n == 1: # lose if n == 1
            t = 0
            return 0 # quits the function and returns value 0
        elif n > 1:
            t += n
            i += 1
    return t
        

def save_list(t, points): # called to save the result to list
    points.append(t)
    s = 0
    for count in points:
        s += count
    #print "Points now: ", points
    return s
    #print "Overall total: %d\n" % s


def run_strikes(tactic):
    i = 0
    rounds = 10 # rounds set to default
    points = []
    while i < rounds: # runs until specified amount of time
        t = one_round(tactic)
        save_list(t, points)
        i += 1
    
    s = 0
    for count in points:
        s += count
    return s