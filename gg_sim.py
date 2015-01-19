# Glupska Grisen
# Teo Elmfeldt
from __future__ import division
from gg_ref_strikes import run_strikes
from gg_ref_count import run_count
import operator
result = {} # where I will store all data

# part for running based on amount of strikes
def test_strikes(tactic, times): # simulates the specified amount of loops for each test
    i = 0
    saved = 0
    while i < times:
        saved += run_strikes(tactic) # adds the points from simulated session
        i += 1
    saved /= times # to get an average as output
    return saved

def test_all_strikes(max_test, times): # loops through each variation
    tactic = 1
    print "Testing %d..." % tactic
    while tactic <= max_test:
        test = test_strikes(tactic, times)
        result[tactic] = test # adds the new result to the dictionary
        print "Average result:", test
        tactic += 1 # add one to the tested value and repeat
        if tactic <= max_test:
            print "Testing %d..." % tactic
        else:
            print "Done! Thank you for your patience."

# part for running based on points, practically a clone of above functions
def test_countto(tactic, times):
    i = 0
    saved = 0
    while i < times:
        saved += run_count(tactic)
        i += 1
    saved /= times
    return saved

def test_all_countto(max_test, times):
    tactic = 1
    print "Testing %d..." % tactic
    while tactic <= max_test:
        test = test_countto(tactic, times)
        result[tactic] = test
        print "Average result:", test
        tactic += 1
        if tactic <= max_test:
            print "Testing %d..." % tactic
        else:
            print "Done! Thank you for your patience."

print """Which strategy do you want to test?
1: Finish after a certain number of strikes with the die.
2: Finish when a certain number is reached."""
which_one = raw_input()
if which_one == '1':
    times = int(raw_input("How many times do you want to simulate? "))
    test_all_strikes(15, times) # change from default 15 in first argument to change scope
elif which_one == '2':
    times = int(raw_input("How many times do you want to simulate? "))
    test_all_countto(35, times) # change from default 35 in first argument to change scope
else:
    print "Please give me '1' or '2'"
    quit()

highest = max(result.iteritems(), key=operator.itemgetter(1)) [0]
print "The highest average of: %f\nis received with number: %d\nusing setting: %s" % (result[highest], highest, which_one)