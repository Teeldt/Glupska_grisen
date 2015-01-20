# Glupska grisen
# Teo Elmfeldt
from random import randint
points = []

def rand_dice(n): # generates a random number, remember to put n = 1 when calling
    return randint(n, 6) # six-sided dice
    # to be able to exclude 1 as a possibility


def one_round_strikes(tactic):
    total = rand_dice(2) # t for total
    i = 1
    while i < tactic: # i == amount of strikes
        
        n = rand_dice(1) # save return value of one_strike() to n
        if n == 1: # lose if n == 1
            total = 0
            return 0 # quits the function and returns value 0
        elif n > 1:
            total += n
            i += 1 # loop based on amount of strikes
    return total

def one_round_count(tactic):
    total = rand_dice(2)
    i = 1
    while total < tactic: # loop while the total < tactic
        
        n = rand_dice(1) # save return value of one_strike() to n
        if n == 1: # lose if n == 1
            total = 0
            return 0 # quits the function and returns value 0
        elif n > 1:
            total += n
    return total
        

def save_list(total, points): # called to save the result to list
    points.append(total)
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
        t = one_round_strikes(tactic)
        save_list(t, points)
        i += 1
    
    s = 0
    for count in points:
        s += count
    return s

def run_count(tactic):
    i = 0
    rounds = 10 # rounds set to default
    points = []
    while i < rounds: # runs until specified amount of time
        t = one_round_count(tactic)
        save_list(t, points)
        i += 1
    
    s = 0
    for count in points:
        s += count
    return s